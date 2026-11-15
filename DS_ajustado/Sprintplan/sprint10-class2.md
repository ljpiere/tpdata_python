---
inclusion: manual
---

# Sprint 10 – Notebook 2: Comparación de Modelos y Cross-Validation

## Archivo
`DS/Sprint 10/DS_Sprint10_class2_Comparacion_y_Cross_Validation.ipynb`

## Sprint
**SPRINT 10 – Aprendizaje Supervisado: Clasificación**

## Tema
Comparación Sistemática de Modelos y Validación Cruzada

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/ML/Cross_validation.ipynb`
- `complements/ML/ML_models_comparisson.ipynb`

## Objetivos de Aprendizaje
- Aplicar **k-Fold Cross-Validation** y Stratified k-Fold para evaluar modelos de forma robusta
- Comparar **Decision Trees, Random Forest y Logistic Regression** de forma sistemática
- Usar **GridSearchCV** para optimización de hiperparámetros
- Construir una **tabla comparativa** de modelos con múltiples métricas
- Entender el **bias-variance trade-off** y cómo detectar sobre/subajuste

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
Cross-Validation: k-Fold y Stratified | 25 min |
Comparación de modelos: DT vs RF vs LR | 25 min |
GridSearchCV: optimización de hiperparámetros | 20 min |
Bias-Variance trade-off | 10 min |
Actividad práctica – Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber si tu modelo es realmente bueno o solo tuvo suerte con los datos de test?
2. **Cross-Validation** – Por qué un solo split no basta; k-Fold; Stratified; `cross_val_score()`
3. **Comparación de modelos** – Tabla sistemática con accuracy, F1, ROC-AUC para 3 modelos
4. **GridSearchCV** – Qué son hiperparámetros vs parámetros; búsqueda exhaustiva; `best_params_`
5. **Bias-Variance** – Modelo simple (bias alto) vs complejo (varianza alta); curvas de aprendizaje
6. **Breakout Rooms** – Comparar 3 modelos con CV y presentar recomendación
7. **Kahoot** – 6 preguntas

## Librerías Clave
`sklearn` (cross_val_score, GridSearchCV, DecisionTreeClassifier, RandomForestClassifier, LogisticRegression)
