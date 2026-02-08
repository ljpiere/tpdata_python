import os
import pandas as pd

# Define the directory containing the CSV files
# Using relative path assuming script is run from project root or DA folder
# Adjusting based on file location: script will be in DA/
DATAWAR_PATH = os.path.join(os.path.dirname(__file__), 'datasets', 'duckdb')

def convert_csv_to_parquet():
    if not os.path.exists(DATAWAR_PATH):
        print(f"Directory not found: {DATAWAR_PATH}")
        return

    files = [f for f in os.listdir(DATAWAR_PATH) if f.endswith('.csv')]
    
    if not files:
        print(f"No CSV files found in {DATAWAR_PATH}")
        return

    print(f"Found {len(files)} CSV files in {DATAWAR_PATH}. Starting conversion...")

    for filename in files:
        csv_path = os.path.join(DATAWAR_PATH, filename)
        parquet_filename = filename.replace('.csv', '.parquet')
        parquet_path = os.path.join(DATAWAR_PATH, parquet_filename)

        try:
            print(f"Converting {filename} to {parquet_filename}...")
            df = pd.read_csv(csv_path)
            df.to_parquet(parquet_path, index=False)
            print(f"Successfully converted {filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    convert_csv_to_parquet()
