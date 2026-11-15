---
inclusion: manual
---

# Sprint 8 – Notebook 1: SQL Avanzado

## Archivo (to be created)
`DS/Sprint 8/DS_Sprint8_class1.ipynb`

## Sprint
**SPRINT 8 – Recopilación y Almacenamiento de Datos**

## Tema
SQL Avanzado

## Objetivos de Aprendizaje
- Escribir consultas SQL **complejas**: JOINs múltiples, subconsultas, CTEs
- Comprender el **orden de ejecución** de una query SQL
- Aplicar **buenas prácticas** de SQL para eficiencia y legibilidad
- Usar **índices** y entender su impacto en el rendimiento
- Conectar Python con bases de datos SQL usando **SQLite / SQLAlchemy**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Repaso rápido de SQL básico | 10 mins |
| 3 | JOINs múltiples y subconsultas | 25 mins |
| 4 | CTEs y Window Functions | 20 mins |
| 5 | Índices y optimización | 15 mins |
| 6 | Python + SQL (SQLite/SQLAlchemy) | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo extraer exactamente los datos que necesitas de una base de datos real?
2. **Repaso SQL básico** – SELECT, FROM, WHERE, GROUP BY, ORDER BY, LIMIT; orden de ejecución (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT)
3. **JOINs múltiples** – INNER, LEFT, RIGHT, FULL OUTER; self-joins; múltiples tablas; analogía con `pd.merge()`
4. **Subconsultas y CTEs** – subconsultas en WHERE y FROM; `WITH` CTEs para legibilidad; cuándo usar tablas intermedias
5. **Window Functions** – `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()`; casos de uso en análisis de negocio
6. **Índices** – qué son, cuándo crearlos, impacto en rendimiento; `CREATE INDEX`
7. **Python + SQL** – `sqlite3`, `pd.read_sql()`, `SQLAlchemy` básico; DBeaver como herramienta visual
8. **Actividad práctica – Breakout Rooms** – students answer business questions using SQL on a provided database; spinner to pick presenter
9. **Tips y buenas prácticas** – use CTEs over nested subqueries, index foreign keys, avoid SELECT *, use EXPLAIN
10. **Cierre y Kahoot**

## Requerimientos
- SQLite (built into Python)
- DBeaver (optional, for visual exploration)
- Provided `.db` file with sample data

## Librerías Clave / Tools
`sqlite3`, `pandas`, `sqlalchemy`, DBeaver

## Notas de Estilo
- Note: some tutors may use different SQL tools — this notebook uses SQLite as the standard
- Analogy: SQL JOINs ↔ pandas merge (students already know this)
- Business questions drive every example

---
