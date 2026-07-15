---
inclusion: manual
---

# Sprint 6 – Notebook 2: Cómo se Trabaja con SQL y Otros Tipos de Datos en la Vida Real

## Archivo (to be created)
`DS/Sprint 6/DS_Sprint6_class2_sql.ipynb`

## Sprint
**SPRINT 6 – Herramientas de Desarrollo de Software** *(maps to DA-DS S6)*

## Webinar Fuente
`complements/TripleTen/Webinars/DA-DS/S6/Webinar 6.2 - Cómo se trabaja con SQL y otros tipos de datos en la vida real.md`

## Tema
Cómo se Trabaja con SQL y Otros Tipos de Datos en la Vida Real

## Objetivos de Aprendizaje
- Comprender la **complejidad algorítmica** (Big O) y su impacto en queries SQL
- Conocer los **8 paradigmas de bases de datos** y cuándo usar cada uno
- Conectar **Python/Pandas con bases de datos SQL** de forma parametrizable
- Entender el formato **Parquet** y otras formas rápidas de leer datos
- Conocer herramientas modernas: **Polars, PySpark, data.table**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Complejidad algorítmica y tablas intermedias | 20 mins |
| 3 | DBMS, ERD y paradigmas de bases de datos | 25 mins |
| 4 | Python + SQL: queries parametrizables | 20 mins |
| 5 | Parquet y herramientas de datos rápidos | 20 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo trabajan realmente los equipos de datos con bases de datos en producción?
2. **Complejidad algorítmica** – Big O notation: O(1), O(n), O(n²); por qué importa en SQL; tablas intermedias para reducir complejidad; utilidad general más allá de SQL
3. **DBMS y ERD** – qué es un DBMS; qué es un ERD (Entity-Relationship Diagram); cómo leer un ERD; herramientas para crear ERDs (Lucidchart, DBeaver)
4. **8 paradigmas de bases de datos** – Key-value (Redis), Wide Column (Cassandra), Document (MongoDB), Relational (PostgreSQL), Graph (Neo4j), Search Engine (Elasticsearch), Multimodel, Vectorial; cuándo usar cada uno en DS
5. **Diferencias entre DBMS** – MySQL vs PostgreSQL vs SQLite vs otros; cuándo usar cada uno; herramientas de interfaz (DBeaver, pgAdmin, TablePlus)
6. **Python + SQL** – `sqlite3`, `pd.read_sql()`, `SQLAlchemy`; crear queries parametrizables con Python o R; ejemplo con DBeaver y SQLite
7. **Formato Parquet** – qué es y por qué es útil (columnar, comprimido, rápido); `pd.read_parquet()`, `df.to_parquet()`
8. **Herramientas de datos rápidos** – `data.table` (R), `polars` (Python), `PySpark`; cuándo usar cada uno vs pandas
9. **Actividad práctica – Breakout Rooms** – students connect Python to a SQLite database and run parametrized queries; spinner to pick presenter
10. **Tips y buenas prácticas** – use Parquet for large datasets, parametrize queries to avoid SQL injection, use DBeaver for exploration
11. **Cierre y Kahoot**

## Librerías Clave / Tools
`sqlite3`, `pandas`, `sqlalchemy`, `pyarrow`/`fastparquet`, DBeaver

## Notas de Estilo
- "How real teams work" framing — not just textbook SQL
- 8 paradigms overview: breadth over depth, just enough to know what exists
- Polars/PySpark: mention as "when pandas is not enough"

---
