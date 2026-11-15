---
inclusion: manual
---

# Sprint 11 – Notebook 2: Feature Engineering y Encoding

## Archivo
`DS/Sprint 11/DS_Sprint11_class2_Feature_Engineering.ipynb`

## Sprint
**SPRINT 11 – Aprendizaje Supervisado: Optimización**

## Tema
Feature Engineering, Encoding y Selección de Características

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/ML/OHEvsOE.ipynb`
- `complements/ML/OneHotEncoding.ipynb`
- `complements/TripleTen/Webinars/DS/S12/Webinar DS 12.1 - Feature Engineering y correlación entre variables.md`

## Objetivos de Aprendizaje
- Aplicar **One-Hot Encoding** y **Ordinal Encoding** correctamente según el tipo de variable
- Realizar **Feature Engineering** avanzado: binning, log transform, interacciones, extracción de fechas
- Comprender la **correlación lineal vs no-lineal** y su impacto en modelos
- Aplicar técnicas de **selección de características**: importancia, RFE, SelectKBest
- Construir **ColumnTransformer** para pipelines con diferentes transformaciones por columna

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
OHE vs Ordinal Encoding: cuándo usar cada uno | 20 min |
Feature Engineering: crear mejores features | 25 min |
Correlación y selección de características | 20 min |
ColumnTransformer: pipelines profesionales | 15 min |
Actividad práctica – Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo hacer que un modelo mediocre se vuelva excelente sin cambiar el algoritmo?
2. **Encoding** – OHE para nominales, Ordinal para ordinales; errores comunes; get_dummies vs OneHotEncoder
3. **Feature Engineering** – Binning (pd.cut), log transform, ratios, extracción de fecha (día semana, mes)
4. **Correlación** – Pearson (lineal) vs distance correlation (no-lineal); por qué árboles hacen cortes unidimensionales
5. **Selección** – feature_importances_, SelectKBest, RFE; curse of dimensionality
6. **ColumnTransformer** – Aplicar diferentes transformaciones a diferentes columnas en un solo pipeline
7. **Breakout Rooms** – Mejorar un modelo baseline aplicando FE y encoding
8. **Kahoot** – 6 preguntas

## Librerías Clave
`sklearn` (OneHotEncoder, OrdinalEncoder, ColumnTransformer, SelectKBest, RFE), `pandas`, `numpy`
