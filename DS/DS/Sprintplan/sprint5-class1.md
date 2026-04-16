---
inclusion: manual
---

# Sprint 5 – Notebook 1: Introducción a la Estadística

## Archivo (to be created)
`DS/Sprint 5/DS_Sprint5_class1.ipynb`

## Sprint
**SPRINT 5 – Análisis Estadístico de Datos**

## Tema
Introducción a la Estadística e Introducción a la Probabilidad

## Objetivos de Aprendizaje
- Comprender los conceptos fundamentales de **estadística descriptiva** e inferencial
- Diferenciar entre **población y muestra**, parámetros y estadísticos
- Calcular e interpretar **medidas de tendencia central** (media, mediana, moda) y **dispersión** (varianza, desviación estándar, IQR)
- Comprender qué es una **variable aleatoria** y los tipos de distribuciones
- Aplicar la **Ley de Grandes Números** y el **Teorema Central del Límite** intuitivamente

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Estadística descriptiva: medidas de tendencia y dispersión | 25 mins |
| 3 | Distribuciones de probabilidad | 25 mins |
| 4 | LLN y CLT: intuición visual | 20 mins |
| 5 | Actividad práctica – Breakout Rooms | 15 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber si lo que observamos en los datos es real o solo ruido?
2. **Estadística descriptiva** – media, mediana, moda; varianza, desviación estándar, IQR; `df.describe()`; visualización con histogramas y boxplots
3. **Población vs muestra** – parámetros (μ, σ) vs estadísticos (x̄, s); sesgo de muestreo
4. **Variables aleatorias** – discretas vs continuas; PDF y CDF; distribución normal, binomial, Poisson
5. **LLN y CLT** – simulación visual con Python: lanzar monedas N veces, mostrar convergencia; distribución de medias muestrales
6. **Actividad práctica – Breakout Rooms** – students compute and interpret descriptive stats on a real dataset; spinner to pick presenter
7. **Tips y buenas prácticas** – always visualize before computing, report median for skewed data, check for outliers first
8. **Cierre y Kahoot**

## Imágenes Utilizadas
- `../Images/S_DS_para_normal_dist.png` (normal distribution reference)

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy.stats`

## Notas de Estilo
- Simulation-first: show LLN/CLT visually before defining them formally
- Connect to Sprint 3 (descriptive stats were introduced with `df.describe()`)
- Emphasize intuition over formulas

---
