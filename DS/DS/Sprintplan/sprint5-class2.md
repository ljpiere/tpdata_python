---
inclusion: manual
---

# Sprint 5 – Notebook 2: Prueba de Hipótesis

## Archivo (to be created)
`DS/Sprint 5/DS_Sprint5_class2.ipynb`

## Sprint
**SPRINT 5 – Análisis Estadístico de Datos**

## Tema
Prueba de Hipótesis

## Objetivos de Aprendizaje
- Formular correctamente **hipótesis nula (H₀) y alternativa (H₁)**
- Comprender el concepto de **p-value**, nivel de significancia (α) y región de rechazo
- Diferenciar entre **errores Tipo I y Tipo II**
- Aplicar los tests más comunes: **Z-test, t-test, chi-cuadrado**
- Saber **cuándo usar cada test** según el tipo de datos y la pregunta de negocio

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Lógica de la prueba de hipótesis | 20 mins |
| 3 | p-value, α y errores Tipo I/II | 20 mins |
| 4 | Z-test, t-test y chi-cuadrado | 25 mins |
| 5 | Actividad práctica – Breakout Rooms | 20 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber si una diferencia en los datos es real o producto del azar?
2. **Lógica de la prueba** – H₀ vs H₁; "inocente hasta que se demuestre culpable"; analogía con juicio
3. **p-value y α** – qué significa p < 0.05; nivel de confianza; región de rechazo; visualización de la distribución con zona de rechazo sombreada
4. **Errores Tipo I y II** – falsos positivos vs falsos negativos; trade-off; ejemplos médicos y de negocio
5. **Tests estadísticos** – Z-test (media conocida), t-test (una muestra, dos muestras, pareado), chi-cuadrado (variables categóricas); `scipy.stats`
6. **Cómo elegir el test correcto** – árbol de decisión: tipo de variable, número de grupos, distribución
7. **Actividad práctica – Breakout Rooms** – students run a hypothesis test on a business question; spinner to pick presenter
8. **Tips y buenas prácticas** – statistical significance ≠ practical significance; always check assumptions; report effect size
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet (consider adding decision tree for test selection)

## Librerías Clave
`pandas`, `numpy`, `scipy.stats`, `matplotlib`, `seaborn`

## Notas de Estilo
- Court analogy for H₀/H₁ makes the logic intuitive
- Visualize the p-value on the distribution curve
- Business context for every test example

---
