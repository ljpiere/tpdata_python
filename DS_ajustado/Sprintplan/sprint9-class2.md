---
inclusion: manual
---

# Sprint 9 – Notebook 2: Primer Modelo de Clasificación y KNN

## Archivo
`DS/Sprint 9/DS_Sprint9_class2_Primer_Modelo_y_KNN.ipynb`

## Sprint
**SPRINT 9 – Introducción al Machine Learning**

## Tema
Primer Modelo de Clasificación y K-Nearest Neighbors (KNN)

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/ML/knn.ipynb`
- `complements/ML/Tipos_de_distancias_analiticas.ipynb`
- `complements/TripleTen/Webinars/DS/S7/Webinar DS 7.1 - Un primer modelo de clasificación.md`

## Objetivos de Aprendizaje
- Entrenar un **primer modelo de clasificación** completo con train/test split
- Comprender el algoritmo **K-Nearest Neighbors (KNN)** y su intuición geométrica
- Conocer los **tipos de distancia** (Euclidiana, Manhattan, Coseno) y cuándo usar cada una
- Evaluar un modelo con **accuracy** y entender sus limitaciones
- Visualizar las **fronteras de decisión** de KNN con diferentes valores de k

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
Flujo completo de un modelo: train/test split | 20 min |
KNN: intuición y algoritmo | 25 min |
Tipos de distancias analíticas | 20 min |
Efecto de k en las fronteras de decisión | 15 min |
Actividad práctica – Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo puede una máquina clasificar datos nuevos basándose en ejemplos anteriores?
2. **Flujo completo** – Cargar datos → split → entrenar → predecir → evaluar; `train_test_split()`
3. **KNN: intuición** – "Dime con quién andas y te diré quién eres"; votar entre los k vecinos más cercanos
4. **Tipos de distancias** – Euclidiana (L2), Manhattan (L1), Coseno; tabla comparativa; cuándo usar cada una
5. **Efecto de k** – k=1 (sobreajuste), k grande (subajuste); visualización de fronteras; elbow method para k
6. **Normalización** – Por qué escalar features antes de KNN; `StandardScaler`
7. **Breakout Rooms** – Entrenar KNN con diferentes k, comparar accuracy, visualizar fronteras
8. **Kahoot** – 6 preguntas

## Librerías Clave
`sklearn` (KNeighborsClassifier, train_test_split, StandardScaler), `pandas`, `numpy`, `matplotlib`
