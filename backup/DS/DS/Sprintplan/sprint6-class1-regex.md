---
inclusion: manual
---

# Sprint 6 – Notebook 1: Cómo Aprender RegEx y Buenas Prácticas de SQL

## Archivo (to be created)
`DS/Sprint 6/DS_Sprint6_class1_regex.ipynb`

## Sprint
**SPRINT 6 – Herramientas de Desarrollo de Software** *(maps to DA-DS S6)*

## Webinar Fuente
`complements/TripleTen/Webinars/DA-DS/S6/Webinar 6.1 - Cómo aprender RegEx y buenas prácticas de SQL.md`

## Tema
Cómo Aprender RegEx y Buenas Prácticas de SQL

## Objetivos de Aprendizaje
- Usar **regex101.com** para aprender y testear expresiones regulares
- Dominar los **tokens más relevantes de RegEx**: `.`, `*`, `+`, `[]`, `{}`, `^`, `$`, `()`, `|`
- Aplicar RegEx en **VSCode** (buscar, reemplazar, refactorizar) y en **Pandas** (`str.contains`, `str.extract`)
- Comprender el **orden de ejecución de SQL** y cómo afecta el rendimiento
- Aplicar **buenas prácticas de SQL**: indexación, tablas intermedias, `CREATE TABLE`

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | RegEx: tokens y regex101.com | 30 mins |
| 3 | RegEx en VSCode y Pandas | 20 mins |
| 4 | SQL: orden de ejecución y buenas prácticas | 25 mins |
| 5 | DBeaver y herramientas de exploración | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo extraer exactamente lo que necesitas de texto y bases de datos?
2. **RegEx con regex101.com** – secciones de la página; tokens: `.` (cualquier char), `*` (0+), `+` (1+), `[]` (conjunto), `{}` (repetición), `[A-Za-z]` (rango), `^` (inicio), `$` (fin), `()` (grupo), `|` (alternativa); escapado: `\n`, `\t`, `\s`, `\-`; tabla ASCII
3. **RegEx en VSCode** – reemplazar separadores; refactorización; encontrar contenido específico; ejemplos prácticos
4. **RegEx en Pandas** – `str.contains()`, `str.extract()`, `str.replace()`, `str.findall()`; ejemplos con datasets reales
5. **SQL: orden de ejecución** – FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT; por qué importa para el rendimiento
6. **Buenas prácticas de SQL** – indexación y su utilidad; `CREATE TABLE`; tablas intermedias (CTEs); 8 formas de optimizar queries
7. **DBeaver** – setear conexiones; descarga de drivers; ejemplo con SQLite; creación de esquema ER; exploración del DDL; PowerBI como alternativa
8. **Herramientas de estudio** – HackerRank para SQL; ChatGPT integrado en Edge
9. **Actividad práctica – Breakout Rooms** – students write RegEx patterns for a text cleaning task and optimize a SQL query; spinner to pick presenter
10. **Tips y buenas prácticas** – test RegEx in regex101 before using in code, use CTEs over nested subqueries, index foreign keys
11. **Cierre y Kahoot**

## Librerías Clave / Tools
`re`, `pandas` (str methods), SQLite, DBeaver, regex101.com, HackerRank

## Notas de Estilo
- regex101.com as the primary learning tool — interactive and visual
- SQL optimization framed as "making your queries faster and cheaper"
- DBeaver demo: create a simple SQLite database and explore it visually

---
