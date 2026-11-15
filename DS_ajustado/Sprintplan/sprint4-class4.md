---
inclusion: manual
---

# Sprint 4 – Notebook 4: Ambientes Virtuales, Reproducibilidad y Pull Requests

## File
`DS/Sprint 4/DS_Sprint4_class4_Ambientes_Virtuales_y_Pull_Requests.ipynb`

## Sprint
**SPRINT 4 – Manipulación de Datos (Data Wrangling) Continuación**

## Source Webinar
`complements/TripleTen/Webinars/DA-DS/S4/Webinar 4.3 - Ambientes virtuales, reproducibilidad y pull requests.md`

## Topic
Ambientes Virtuales, Reproducibilidad y Pull Requests

## Status
✅ **CREATED**

## Learning Objectives
- Crear, activar y gestionar **ambientes virtuales** de Python
- Generar y usar `requirements.txt` para **reproducibilidad de proyectos**
- Aplicar un **flujo de trabajo colaborativo con Git**: ramas, `.gitignore`, `README.md`
- Crear y revisar **pull requests** en GitHub
- Organizar proyectos con una **estructura de carpetas** profesional

## Agenda (2 hours)
| Block | Activity | Duration |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 min |
| 2 | Ambientes virtuales: creación y gestión | 25 min |
| 3 | pip freeze y requirements.txt | 15 min |
| 4 | Estructura de proyecto y .gitignore | 20 min |
| 5 | Pull requests y trabajo colaborativo | 20 min |
| 6 | Actividad práctica – Breakout Rooms | 20 min |
| 7 | Tips y buenas prácticas | 5 min |
| 8 | Cierre | 5 min |

## Sections & Content Summary
1. **Pregunta Guía** – ¿Cómo garantizar que tu proyecto funcione en el equipo de otra persona?
2. **Ambientes virtuales** – por qué son necesarios (conflicto de versiones); `python3 -m venv .venv`; activar/desactivar; seleccionar en VSCode
3. **pip freeze y requirements.txt** – `pip freeze > requirements.txt`; `pip install -r requirements.txt`; flujo de reproducción
4. **Estructura de proyecto** – árbol de carpetas: `data/`, `notebooks/`, `src/`, `tests/`; `.gitignore` completo para DS
5. **Pull Requests** – diagrama de flujo main→feature→PR→merge; pasos: `checkout -b`, `push`, crear PR en GitHub; Streamlit brief mention
6. **Breakout Rooms** – en parejas: fork, rama, cambio, PR, review, merge
7. **Tips** – siempre venv, commit requirements.txt, rutas relativas, README

## Key Libraries / Tools
`venv`, `pip`, `git`, `github.com`, `pathlib`

---
