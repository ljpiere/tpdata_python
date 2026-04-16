---
inclusion: manual
---

# Sprint 9 – Notebook 1: Modelos de Aprendizaje Automático

## Archivo
`DS/Sprint 9/DS_Sprint9_class1_Modelos_de_Aprendizaje_Automatico.ipynb`

## Sprint
**SPRINT 9 – Introducción al Machine Learning**

## Tema
Modelos de Aprendizaje Automático

## Objetivos de Aprendizaje
- Introducir los conceptos fundamentales del Machine Learning (ML) y cómo se utiliza en Data Science
- Diferenciar los principales tipos de aprendizaje automático: clasificación, regresión y clustering
- Comprender de forma visual cómo los modelos generan fronteras de decisión para resolver problemas de clasificación
- Comparar la toma de decisiones manual vs automática
- Conocer qué es el sobreajuste y cómo evitarlo
- Ejecutar un primer ejemplo práctico de ML

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Ejemplo visual: cómo aprende un modelo | 20 mins |
| 2 | Introducción al Machine Learning | 15 mins |
| 3 | Tipos de aprendizaje automático (clasificación, regresión, clustering) | 20 mins |
| 4 | Fronteras de decisión y clasificación | 20 mins |
| 5 | Evitar el sobreajuste en modelos de ML | 20 mins |
| 6 | Ejercicio práctico guiado | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo aprende una máquina?
2. **Ejemplo visual** – Image `S9_DS_rule_based_vs_ml.png`; rule-based vs ML comparison; image `S9_DS_netflix.jpg` (Netflix recommendation)
3. **Introducción al ML** – Definition, when to use ML vs traditional programming
4. **Tipos de aprendizaje automático** – Classification, regression, clustering with visual examples; image `S9_DS_good_choice.jpg`
5. **Fronteras de decisión** – Visual demo with scatter plots and decision boundaries using sklearn
6. **Sobreajuste** – Image `S9_DS_overfitting.jpg`; what it is, why it happens, how to detect and avoid it (train/test split, cross-validation)
7. **Ejercicio práctico guiado** – Instructor-led: load dataset, train a classifier, evaluate; Perceptron visual training (`DS_Sprint9_Perceptron_visual_training.py`)
8. **Tips y buenas prácticas** – Model selection, evaluation metrics overview
9. **Cierre y Kahoot**

## Imágenes Utilizadas
- `../Images/S9_DS_rule_based_vs_ml.png`
- `../Images/S9_DS_netflix.jpg`
- `../Images/S9_DS_good_choice.jpg`
- `../Images/S9_DS_overfitting.jpg`

## Supporting Files
- `DS/Sprint 9/DS_Sprint9_Perceptron_visual_training.py` – animated Perceptron training visualization

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `sklearn` (train_test_split, classifiers, metrics)

## Notas de Estilo
- Visual-first approach: decision boundaries shown graphically before math
- Perceptron animation used as a hook to show how models learn
- Overfitting explained with analogy before code

---
