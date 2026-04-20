---
inclusion: manual
---

# Sprint 18 – Notebook 1: Visión Artificial – Introducción a CNN

## Archivo (to be created)
`DS/Sprint 18/DS_Sprint18_class1.ipynb`

## Sprint
**SPRINT 18 – Visión Artificial**

## Tema
Introducción a Redes Neuronales Convolucionales (CNN)

## Objetivos de Aprendizaje
- Comprender cómo se representan las **imágenes** como tensores numéricos
- Entender qué es la **convolución** y cómo las CNNs detectan patrones visuales
- Construir y entrenar una **CNN básica** con Keras para clasificación de imágenes
- Interpretar la **arquitectura CNN**: capas convolucionales, pooling, flatten, dense
- Evaluar el modelo con **accuracy y matriz de confusión multi-clase**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Imágenes como tensores | 15 mins |
| 3 | Convolución: intuición y operación | 20 mins |
| 4 | Arquitectura CNN con Keras | 25 mins |
| 5 | Entrenamiento y evaluación | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 20 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo puede una computadora "ver" y entender una imagen?
2. **Imágenes como tensores** – píxeles como números (0–255); RGB = 3 canales; shape `(height, width, channels)`; `numpy.reshape()`; visualización con `plt.imshow()`
3. **Convolución** – qué es un filtro/kernel; barrido de la imagen; detección de bordes, texturas, formas; animación de convolución
4. **Pooling** – max pooling; reducción de dimensión; intuición: "resumen de una región"
5. **Arquitectura CNN** – `Conv2D` → `MaxPooling2D` → `Flatten` → `Dense`; `Sequential` model; `relu` en capas ocultas, `softmax` en output
6. **Preprocesamiento** – normalización de píxeles (÷255); `to_categorical()` para labels; train/test split
7. **Entrenamiento** – `compile()` (adam, categorical_crossentropy, accuracy), `fit()`, `evaluate()`; curvas de aprendizaje
8. **Evaluación** – accuracy, matriz de confusión multi-clase; `classification_report()`
9. **Actividad práctica – Breakout Rooms** – students train a CNN on Sign Language MNIST; spinner to pick presenter
10. **Tips y buenas prácticas** – normalize inputs, use data augmentation for small datasets, monitor val_loss for overfitting
11. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet (consider adding convolution animation diagram)

## Librerías Clave
`tensorflow`/`keras`, `numpy`, `matplotlib`, `sklearn`, `pandas`

## Requerimientos
- Sign Language MNIST dataset (Kaggle): `https://www.kaggle.com/datasets/datamunge/sign-language-mnist`
- TensorFlow/Keras installed

## Notas de Estilo
- TensorFlow Playground as opening hook (connects to Sprint 15)
- Convolution animation before any code — visual intuition first
- Sign Language MNIST: engaging, multi-class, real-world application

---
