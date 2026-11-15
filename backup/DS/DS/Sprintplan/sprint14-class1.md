---
inclusion: manual
---

# Sprint 14 – Notebook 1: Gradient Descent y Función de Costo

## Archivo
`DS/Sprint 14/DS_Sprint14_class1_Gradiente_Descendiente_y_Funcion_de_Costo.ipynb`

## Sprint
**SPRINT 14 – Métodos Numéricos**

## Tema
Gradiente Descendiente y Función de Costo

## Objetivos de Aprendizaje
- Comprender la intuición del algoritmo de Gradient Descent como método de optimización en ML
- Entender el concepto de función de costo y su importancia para evaluar el desempeño de un modelo
- Explicar la regla de actualización y cómo el algoritmo ajusta los parámetros paso a paso
- Visualizar la trayectoria del algoritmo sobre funciones de costo MSE y BCE mediante gráficas
- Implementar paso a paso Gradient Descent para regresión lineal con dos variables usando un dataset real
- Interpretar cómo los cambios en el learning rate afectan la convergencia

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | ¿Recordando cómo aprenden los modelos? | 10 mins |
| 2 | Intuición del Gradient Descent | 15 mins |
| 3 | Función de costo (MSE y BCE) | 15 mins |
| 4 | Regla de actualización y derivada (intuición) | 25 mins |
| 5 | Visualización del descenso de gradiente | 25 mins |
| 6 | Tips y buenas prácticas | 10 mins |
| 7 | Cierre + Kahoot + dudas | 20 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo sabe un modelo que está mejorando?
2. **Recap** – How models learn (connects to Sprint 9); image `S14_DS_mountain.png`
3. **Intuición del Gradient Descent** – Mountain analogy (walking downhill); image `S14_DS_falling.gif`; image `S14_DS_Gradient_descent.gif`
4. **Función de costo** – MSE for regression, BCE for classification; formula intuition without heavy math
5. **Regla de actualización** – θ = θ − α·∇J(θ); learning rate α explained visually; derivative as "slope direction"
6. **Visualización** – 3D surface plot of cost function; animated gradient descent path; effect of different learning rates (too small, too large, just right)
7. **Implementación paso a paso** – Manual GD for linear regression with two variables on a real dataset; compare with sklearn result
8. **Tips y buenas prácticas** – Choosing learning rate, convergence criteria, feature scaling importance
9. **Cierre + Kahoot + dudas**

## Imágenes Utilizadas
- `../Images/S14_DS_mountain.png`
- `../Images/S14_DS_falling.gif`
- `../Images/S14_DS_Gradient_descent.gif`
- `../Images/S_DS_para_normal_dist.png` (possibly used for BCE section)

## Librerías Clave
`numpy`, `matplotlib`, `pandas`, `sklearn` (for comparison)

## Notas de Estilo
- Math-heavy topic made accessible through mountain/hiking analogy
- GIF animations used to build intuition before equations
- Manual implementation before sklearn to show what's happening under the hood

---
