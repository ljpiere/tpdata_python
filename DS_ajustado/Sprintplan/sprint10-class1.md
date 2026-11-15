---
inclusion: manual
---

# Sprint 10 – Notebook 1: Métricas de Evaluación de Modelos

## Archivo
`DS/Sprint 10/DS_Sprint10_class1_Metricas_de_Evaluacion.ipynb`

## Sprint
**SPRINT 10 – Aprendizaje Supervisado: Clasificación**

## Tema
Métricas de Evaluación de Modelos de Clasificación

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/ML/ML_errors_models.ipynb`
- `complements/TripleTen/Webinars/DS/S7/Webinar DS 7.2 - Métricas de evaluación de modelos de clasificación.md`

## Objetivos de Aprendizaje
- Comprender por qué **accuracy no es suficiente** para evaluar modelos
- Interpretar y calcular **precision, recall, F1-score** y su trade-off
- Construir e interpretar **matrices de confusión**
- Graficar y analizar **curvas ROC y AUC**
- Elegir la **métrica correcta** según el contexto de negocio (costo de FP vs FN)

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
¿Por qué accuracy engaña? El problema del desbalance | 20 min |
Precision, Recall y F1-score | 25 min |
Matriz de confusión visual | 15 min |
Curvas ROC y AUC | 20 min |
Actividad práctica – Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cuándo un modelo con 95% de accuracy puede ser peligroso?
2. **Accuracy engaña** – Ejemplo: detector de fraudes con 99% accuracy que nunca detecta fraudes
3. **Precision y Recall** – Analogía médica (FP = alarma falsa, FN = enfermedad no detectada); trade-off
4. **F1-score** – Media armónica; cuándo usarlo; threshold tuning
5. **Matriz de confusión** – Visualización con seaborn heatmap; interpretar cada cuadrante
6. **ROC y AUC** – Qué mide la curva; comparar modelos; `roc_auc_score()`
7. **Elegir la métrica** – Tabla: contexto → métrica recomendada (spam, fraude, médico, marketing)
8. **Breakout Rooms** – Evaluar dos modelos y recomendar uno con justificación de negocio
9. **Kahoot** – 6 preguntas

## Librerías Clave
`sklearn` (metrics, confusion_matrix, roc_curve, classification_report), `matplotlib`, `seaborn`
