---
inclusion: manual
---

# Sprint 12 – Notebook 2: SKLearn Avanzado para Negocios

## Archivo (to be created)
`DS/Sprint 12/DS_Sprint12_class2.ipynb`

## Sprint
**SPRINT 12 – Aprendizaje Automático en Negocios**

## Tema
SKLearn Avanzado para Negocios

## Objetivos de Aprendizaje
- Aplicar modelos de ML a **problemas de negocio reales** con interpretación de resultados
- Usar **Random Forest, Gradient Boosting y XGBoost** para clasificación y regresión
- Interpretar la **importancia de características** para comunicar resultados a stakeholders
- Construir **pipelines completos** con preprocesamiento + modelo + evaluación
- Conectar predicciones de ML con **decisiones de negocio**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Ensemble methods: Random Forest y Gradient Boosting | 25 mins |
| 3 | Interpretabilidad: feature importance y SHAP básico | 20 mins |
| 4 | Pipeline completo con sklearn | 20 mins |
| 5 | Actividad práctica – Breakout Rooms | 20 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo convencer a un gerente de que tu modelo es útil?
2. **Ensemble methods** – bagging (Random Forest) vs boosting (Gradient Boosting, XGBoost); intuición: "wisdom of crowds"; cuándo usar cada uno
3. **Random Forest** – `RandomForestClassifier/Regressor`; n_estimators, max_depth; OOB score
4. **Gradient Boosting** – `GradientBoostingClassifier`, `XGBClassifier`; learning rate, n_estimators; early stopping
5. **Interpretabilidad** – `feature_importances_`; SHAP values (intro); partial dependence plots; cómo comunicar a no-técnicos
6. **Pipeline completo** – `Pipeline` + `ColumnTransformer` + model; `cross_val_score`; `GridSearchCV`
7. **Decisiones de negocio** – traducir predicciones a acciones; ROI de un modelo; threshold optimization
8. **Actividad práctica – Breakout Rooms** – students build a complete pipeline for a business problem and present findings; spinner to pick presenter
9. **Tips y buenas prácticas** – interpretability > accuracy for business, document assumptions, version your models
10. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`sklearn`, `xgboost`, `shap` (optional), `pandas`, `numpy`, `matplotlib`

## Notas de Estilo
- Business framing throughout: every model decision justified by business impact
- "Wisdom of crowds" analogy for ensemble methods
- Breakout Room: students present to a "business stakeholder" (another student)

---
