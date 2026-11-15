---
inclusion: manual
---

# Sprint 11 – Notebook 1: Herramientas y Metodologías para Optimización de Modelos

## Archivo (to be created)
`DS/Sprint 11/DS_Sprint11_class1.ipynb`

## Sprint
**SPRINT 11 – Aprendizaje Supervisado**

## Tema
Herramientas y Metodologías Adicionales para Optimización de Modelos

## Objetivos de Aprendizaje
- Aplicar **Feature Engineering** avanzado para mejorar el rendimiento de modelos
- Comprender y aplicar técnicas de **selección de características** (feature selection)
- Usar **Pipelines de sklearn** para construir flujos reproducibles
- Aplicar **regularización** (L1/Lasso, L2/Ridge) para evitar sobreajuste
- Comparar múltiples modelos de forma sistemática

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Feature Engineering avanzado | 25 mins |
| 3 | Selección de características | 20 mins |
| 4 | Regularización L1 y L2 | 20 mins |
| 5 | Actividad práctica – Breakout Rooms | 20 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo exprimir el máximo rendimiento de un modelo sin sobreajustarlo?
2. **Feature Engineering avanzado** – binning, log transform, one-hot encoding, grouping operations, feature split, scaling, date extraction; impacto en modelos
3. **Selección de características** – correlación, importancia de features (Random Forest), `SelectKBest`, `RFE`; curse of dimensionality
4. **Regularización** – L1 (Lasso, sparse solutions), L2 (Ridge, shrinkage); `ElasticNet`; cuándo usar cada uno; visualización del efecto
5. **Pipelines de sklearn** – `Pipeline`, `ColumnTransformer`; por qué son esenciales para evitar data leakage
6. **Comparación de modelos** – systematic comparison with CV; `pd.DataFrame` of results; choosing the right model
7. **Actividad práctica – Breakout Rooms** – students improve a baseline model using feature engineering and regularization; spinner to pick presenter
8. **Tips y buenas prácticas** – feature engineering > model selection, always scale before regularization, document every transformation
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`sklearn` (Pipeline, ColumnTransformer, SelectKBest, Lasso, Ridge, ElasticNet), `pandas`, `numpy`, `matplotlib`, `seaborn`

## Notas de Estilo
- Connects to Sprint 10 (ML intro) and Sprint 14 (linear algebra behind regularization)
- Chess-board example from complement material shows why feature engineering matters for tree models

---
