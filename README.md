# tpdata_python

Repositorio de material docente para los bootcamps de **Data Analytics (DA)** y **Data Science (DS)** en Python: notebooks de clase (versiones tutor y estudiante), datasets, planes de sprint, imágenes, material de Kahoot y scripts de apoyo.

## Subcarpetas

- [`DA/`](./DA/README.md) — Material vigente del programa de Data Analytics.
- [`DS/`](./DS/README.md) — Notebooks del programa de Data Science en versión estudiante, organizados por sprint (1 a 19).
- [`DS_ajustado/`](./DS_ajustado/README.md) — Versión revisada y reestructurada del programa de Data Science: notebooks tutor (`DS/`) y estudiante (`DS_students/`), imágenes, planes de clase (`Sprintplan/`), informes de auditoría e implementación, preguntas Kahoot y archivos de dependencias.
- [`backup/`](./backup/README.md) — Copias de respaldo de versiones anteriores del material de DA y DS.
- [`images/`](./images/README.md) — Imágenes generales usadas en notebooks y presentaciones del repositorio.
- [`kahoot_material/`](./kahoot_material/README.md) — Preguntas y respuestas para Kahoots de repaso (`kahoot_questions_responses.ipynb`) e imágenes asociadas.
- [`md/`](./md/README.md) — Notas de referencia rápida, como `pandas_tips.md` (uso de `.loc[]` y otros tips de Pandas).
- [`other/`](./other/README.md) — Scripts y archivos auxiliares: `scraper.py` (scraping de BizBuySell con Playwright), `scan_notebooks.py` y `apply_notebook_updates.py` (revisión y actualización masiva de notebooks), `scan_results.json`, datasets de ejemplo (`bizbuysell_data.csv`, `resenas_texto_sinteticas.csv`) y un notebook de ML con textos.

## Archivos

| Archivo | Tipo | Descripción |
|---|---|---|
| `.gitignore` | Configuración | Archivos y carpetas excluidos de Git (p. ej. `.venv/`) |
| `S5 ladb_mobility_economy_project_student (1).ipynb` | Notebook | Proyecto de estudiante del Sprint 5 (movilidad y economía) |
| `prueba1.ipynb` | Notebook | Notebook de pruebas |
| `requirements.txt` | Dependencias | Paquetes de Python necesarios para ejecutar los notebooks |

## Uso

1. Crear un entorno virtual: `python -m venv .venv` y activarlo.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Abrir los notebooks con Jupyter (`jupyter lab`) o VS Code.
