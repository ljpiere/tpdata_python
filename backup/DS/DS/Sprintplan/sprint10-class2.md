---
inclusion: manual
---

# Sprint 10 – Notebook 2: ML Avanzado – Diseño Profesional de Modelos

## Archivo (to be created)
`DS/Sprint 10/DS_Sprint10_class2.ipynb`

## Sprint
**SPRINT 10 – Introducción al Machine Learning**

## Tema
ML Avanzado: Diseño Profesional de Modelos

## Objetivos de Aprendizaje
- Aplicar un **flujo profesional de ML**: split → train → evaluate → tune → deploy
- Comprender y aplicar **validación cruzada (cross-validation)**
- Usar **GridSearchCV y RandomizedSearchCV** para optimización de hiperparámetros
- Interpretar métricas de evaluación: **accuracy, precision, recall, F1, ROC-AUC**
- Identificar y mitigar **data leakage** en pipelines de ML

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Flujo profesional de ML | 20 mins |
| 3 | Validación cruzada | 20 mins |
| 4 | Métricas de evaluación | 20 mins |
| 5 | Optimización de hiperparámetros | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 20 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber si tu modelo es realmente bueno o solo tiene suerte?
2. **Flujo profesional** – train/val/test split; por qué no usar solo train/test; `Pipeline` de sklearn
3. **Validación cruzada** – k-fold CV; `cross_val_score()`; stratified k-fold para clases desbalanceadas
4. **Métricas de evaluación** – accuracy (cuándo engaña), precision vs recall trade-off, F1-score, ROC curve, AUC; `classification_report()`; matriz de confusión
5. **Optimización de hiperparámetros** – `GridSearchCV`, `RandomizedSearchCV`; qué son los hiperparámetros vs parámetros
6. **Data leakage** – qué es, cómo ocurre, cómo evitarlo; `Pipeline` como solución
7. **Actividad práctica – Breakout Rooms** – students build a full ML pipeline with CV and hyperparameter tuning; spinner to pick presenter
8. **Tips y buenas prácticas** – always use CV, report multiple metrics, document your pipeline
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`sklearn` (Pipeline, cross_val_score, GridSearchCV, metrics), `pandas`, `numpy`, `matplotlib`

## Notas de Estilo
- Connects directly to Sprint 10 class1 (intro to ML)
- Emphasize that "accuracy alone is not enough" with a class imbalance example
- Pipeline demo shows how to prevent data leakage

---
