---
inclusion: manual
---

# Sprint 11 – Notebook 1: Tratamiento de Datos Desbalanceados

## Archivo
`DS/Sprint 11/DS_Sprint11_class1_Datos_Desbalanceados.ipynb`

## Sprint
**SPRINT 11 – Aprendizaje Supervisado: Optimización**

## Tema
Tratamiento de Datos Desbalanceados y Dummy Models

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/ML/Pruebas_estadisticas_ML.ipynb`
- `complements/TripleTen/Webinars/DS/S8/Webinar DS 8.1 - Tratamiento de datos desbalanceados.md`
- `complements/TripleTen/Webinars/DS/S8/Dummy models.md`

## Objetivos de Aprendizaje
- Identificar cuándo un dataset tiene **clases desbalanceadas** y por qué es un problema
- Aplicar técnicas de **oversampling (SMOTE)** y **undersampling**
- Usar **class_weight='balanced'** en modelos de sklearn
- Construir **Dummy Models** como baseline para comparación
- Elegir la **métrica correcta** para problemas desbalanceados

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
El problema del desbalance de clases | 20 min |
Dummy Models como baseline | 15 min |
Técnicas de resampling: SMOTE y undersampling | 25 min |
class_weight y threshold tuning | 15 min |
Actividad práctica – Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Qué pasa cuando tu modelo tiene 99% accuracy pero no detecta ningún fraude?
2. **El problema** – Accuracy engaña; modelo "perezoso"; ejemplo con dataset de fraudes (1% positivos)
3. **Dummy Models** – DummyClassifier(strategy='most_frequent'|'stratified'); baseline obligatoria
4. **SMOTE** – Generar muestras sintéticas de la clase minoritaria; `imblearn`; cuándo sí y cuándo no
5. **Undersampling** – Reducir la clase mayoritaria; RandomUnderSampler; trade-off con pérdida de info
6. **class_weight** – Alternativa sin cambiar los datos; ajuste interno del modelo; threshold tuning
7. **Breakout Rooms** – Dataset de churn desbalanceado: aplicar SMOTE + class_weight + evaluar con F1
8. **Kahoot** – 6 preguntas

## Librerías Clave
`sklearn`, `imblearn` (SMOTE, RandomUnderSampler), `pandas`, `matplotlib`
