---
inclusion: manual
---

# Sprint 15 – Notebook 2: Introducción a las Redes Neuronales Artificiales (ANN)

## Archivo (to be created)
`DS/Sprint 15/DS_Sprint15_class2.ipynb`

## Sprint
**SPRINT 15 – Métodos Numéricos**

## Tema
Introducción a las Redes Neuronales Artificiales (ANN)

## Objetivos de Aprendizaje
- Comprender la **arquitectura de una red neuronal**: capas de entrada, ocultas y salida
- Entender el rol de las **funciones de activación** (ReLU, sigmoid, softmax)
- Comprender el proceso de **forward propagation** y **backpropagation** intuitivamente
- Construir y entrenar una **red neuronal básica** con Keras/TensorFlow
- Conectar las ANN con el **Gradient Descent** del notebook anterior

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Arquitectura de una ANN | 20 mins |
| 3 | Funciones de activación | 15 mins |
| 4 | Forward y backpropagation: intuición | 20 mins |
| 5 | Implementación con Keras | 25 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo aprende una red neuronal a reconocer patrones complejos?
2. **Arquitectura** – neurona artificial (perceptrón); capas: input, hidden, output; pesos y biases; `tensorflow.playground` demo
3. **Funciones de activación** – ReLU (hidden layers), sigmoid (binary output), softmax (multi-class); por qué son necesarias (non-linearity)
4. **Forward propagation** – cómo fluye la información de entrada a salida; cálculo matricial; predicción
5. **Backpropagation** – cómo se ajustan los pesos; chain rule intuitiva; conexión con Gradient Descent
6. **Implementación con Keras** – `Sequential`, `Dense`, `compile()` (optimizer, loss, metrics), `fit()`, `evaluate()`, `predict()`; callbacks básicos
7. **Ejemplo práctico** – clasificación binaria o multi-clase con un dataset tabular; comparar con Random Forest
8. **Actividad práctica – Breakout Rooms** – students build and train a simple ANN; spinner to pick presenter
9. **Tips y buenas prácticas** – start simple, use dropout for regularization, monitor val_loss, normalize inputs
10. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`tensorflow`/`keras`, `numpy`, `pandas`, `matplotlib`, `sklearn`

## Notas de Estilo
- TensorFlow Playground as interactive hook before any code
- Connects directly to Sprint 15 class1 (Gradient Descent)
- Keep architecture simple: 2–3 layers max for the first example

---
