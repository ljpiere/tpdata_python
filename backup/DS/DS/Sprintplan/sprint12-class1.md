---
inclusion: manual
---

# Sprint 12 – Notebook 1: Análisis por Embudo de Eventos y Pruebas A/B

## Archivo (to be created)
`DS/Sprint 12/DS_Sprint12_class1.ipynb`

## Sprint
**SPRINT 12 – Aprendizaje Automático en Negocios**

## Tema
Análisis por Embudo de Eventos y Pruebas A/B

## Objetivos de Aprendizaje
- Construir y analizar un **embudo de conversión (funnel)** para identificar puntos de abandono
- Diseñar y ejecutar una **prueba A/B** correctamente
- Calcular el **tamaño de muestra** necesario para una prueba A/B válida
- Interpretar resultados de pruebas A/B con **significancia estadística**
- Conectar el análisis de negocio con herramientas de ML

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Análisis por embudo de eventos | 25 mins |
| 3 | Diseño de pruebas A/B | 25 mins |
| 4 | Análisis estadístico de resultados A/B | 20 mins |
| 5 | Actividad práctica – Breakout Rooms | 15 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber qué cambio en un producto realmente mejora el negocio?
2. **Embudo de conversión** – qué es un funnel; etapas (awareness → consideration → conversion → retention); calcular tasas de conversión por etapa; visualización con barras apiladas o Sankey
3. **Análisis de abandono** – dónde se pierden más usuarios; hipótesis sobre causas; priorización de mejoras
4. **Diseño de prueba A/B** – hipótesis nula y alternativa; grupo control vs tratamiento; randomización; duración mínima; tamaño de muestra (`statsmodels.stats.power`)
5. **Análisis de resultados** – z-test para proporciones; p-value e intervalo de confianza; significancia práctica vs estadística
6. **Errores comunes en A/B** – peeking problem, multiple testing, Simpson's paradox, novelty effect
7. **Actividad práctica – Breakout Rooms** – students analyze a provided A/B test dataset and make a recommendation; spinner to pick presenter
8. **Tips y buenas prácticas** – pre-register your hypothesis, run the full duration, report effect size
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet (consider adding funnel visualization)

## Librerías Clave
`pandas`, `numpy`, `scipy.stats`, `statsmodels`, `matplotlib`, `seaborn`

## Notas de Estilo
- E-commerce or app context makes funnels immediately relatable
- Emphasize that A/B testing is hypothesis testing applied to business
- Breakout Room: students play the role of a product analyst

---
