---
inclusion: manual
---

# Sprint 14 – Notebook 1: Introducción al Álgebra Vectorial

## Archivo (to be created)
`DS/Sprint 14/DS_Sprint14_class1_algebra.ipynb`

## Sprint
**SPRINT 14 – Álgebra Lineal**

## Tema
Introducción al Álgebra Vectorial y Distancias Vectoriales

## Objetivos de Aprendizaje
- Representar y operar con **vectores** en 2D y 3D
- Comprender la **base unitaria** del espacio y las combinaciones lineales
- Calcular **distancias vectoriales**: norma L1, L2 (Euclidiana), coseno
- Entender las **matrices como transformaciones lineales**
- Conectar el álgebra lineal con **modelos de ML** (regresión lineal, KNN, PCA)

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Vectores: representación y operaciones | 25 mins |
| 3 | Distancias vectoriales | 20 mins |
| 4 | Matrices como transformaciones | 20 mins |
| 5 | Conexión con ML | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Qué tienen en común un punto en un mapa y una fila de un dataset?
2. **Vectores** – representación como tuplas; base unitaria (î, ĵ); suma, resta, escalar; visualización con matplotlib arrows
3. **Combinaciones lineales** – span de vectores; dependencia e independencia lineal; intuición geométrica
4. **Distancias vectoriales** – norma L1 (Manhattan), L2 (Euclidiana), coseno; `numpy.linalg.norm()`; cuándo usar cada una en ML (KNN, NLP)
5. **Matrices como transformaciones** – rotación, escala, reflexión; composición de matrices; matriz identidad; `numpy` matrix operations
6. **Conexión con ML** – regresión lineal como sistema de ecuaciones; KNN usa distancias; PCA usa eigenvectors; embeddings en NLP
7. **Actividad práctica – Breakout Rooms** – students compute distances between data points and interpret results; spinner to pick presenter
8. **Tips y buenas prácticas** – always normalize before computing distances, understand what distance metric your model uses
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet (consider adding vector diagrams)

## Librerías Clave
`numpy`, `matplotlib`, `scipy.spatial.distance`

## Notas de Estilo
- "Point on a map = row in a dataset" analogy bridges abstract math to DS
- 3Blue1Brown Essence of Linear Algebra series as recommended resource
- Visual-first: every concept shown geometrically before algebraically

---
