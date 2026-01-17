import os
import json
import glob

def scan_notebooks(directory):
    notebooks = glob.glob(os.path.join(directory, "*.ipynb"))
    results = []

    for nb_path in notebooks:
        with open(nb_path, 'r', encoding='utf-8') as f:
            try:
                nb = json.load(f)
            except json.JSONDecodeError:
                results.append(f"Error reading {os.path.basename(nb_path)}")
                continue

        filename = os.path.basename(nb_path)
        cierre_content = None
        next_steps_content = None
        headers = []

        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = "".join(cell.get('source', []))
                
                # Check for Cierre
                if "## Cierre" in source or "# Cierre" in source:
                    cierre_content = source
                
                # Check for Siguientes Pasos
                if "## Siguientes Pasos" in source or "# Siguientes Pasos" in source or "Siguientes Pasos" in source: # looser check
                     if "Siguientes Pasos" in source and len(source) < 500: # heuristic
                        next_steps_content = source

                # Extract headers for context
                for line in source.split('\n'):
                    if line.startswith('#'):
                        headers.append(line.strip())

        results.append({
            "filename": filename,
            "has_cierre": cierre_content is not None,
            "cierre_snippet": cierre_content[:100] if cierre_content else "",
            "has_next_steps": next_steps_content is not None,
            "next_steps_snippet": next_steps_content[:100] if next_steps_content else "",
            "headers": headers[:10] # just first 10 headers
        })

    return results

if __name__ == "__main__":
    results = scan_notebooks(r"c:\Users\jeanp\Downloads\Proyectos\tpdata_python\DA")
    with open("scan_results.json", "w", encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print("Results saved to scan_results.json")
