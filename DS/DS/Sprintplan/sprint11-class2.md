---
inclusion: manual
---

# Sprint 11 – Notebook 2: Métricas de Evaluación

## Archivo (to be created)
`DS/Sprint 11/DS_Sprint11_class2.ipynb`

## Sprint
**SPRINT 11 – Aprendizaje Supervisado**

## Tema
Métricas de Evaluación de Modelos

## Objetivos de Aprendizaje
- Seleccionar la **métrica correcta** según el tipo de problema y el contexto de negocio
- Interpretar y calcular métricas de **clasificación**: accuracy, precision, recall, F1, ROC-AUC
- Interpretar y calcular métricas de **regresión**: MAE, MSE, RMSE, R²
- Comprender el **trade-off precision-recall** y cuándo priorizar cada uno
- Construir e interpretar **matrices de confusión** y **curvas ROC**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Métricas de clasificación | 30 mins |
| 3 | Métricas de regresión | 20 mins |
| 4 | Curvas ROC y AUC | 20 mins |
| 5 | Actividad práctica – Breakout Rooms | 20 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cuándo un modelo "bueno" puede ser peligroso?
2. **Métricas de clasificación** – accuracy (cuándo engaña con clases desbalanceadas), precision (FP cost), recall (FN cost), F1-score; `classification_report()`; matriz de confusión visual
3. **Trade-off precision-recall** – médico vs spam filter analogy; precision-recall curve; threshold tuning
4. **Métricas de regresión** – MAE (interpretable), MSE (penaliza outliers), RMSE (same units), R² (explained variance); cuándo usar cada una
5. **Curvas ROC y AUC** – qué mide AUC; cómo construir la curva; comparar modelos con ROC; `roc_auc_score()`
6. **Clases desbalanceadas** – oversampling (SMOTE), undersampling, `class_weight='balanced'`; por qué accuracy falla
7. **Actividad práctica – Breakout Rooms** – students evaluate two models on a business problem and recommend one with justification; spinner to pick presenter
8. **Tips y buenas prácticas** – always define the business cost of FP vs FN before choosing a metric
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet (consider adding confusion matrix visual and ROC curve diagram)

## Librerías Clave
`sklearn` (metrics, roc_curve, classification_report, confusion_matrix), `matplotlib`, `seaborn`, `imblearn` (optional)

## Notas de Estilo
- Medical diagnosis analogy for precision vs recall is universally relatable
- Always frame metrics in business terms: "what does a false positive cost?"
- Breakout Room: students must justify their model choice to a "business stakeholder"

---
