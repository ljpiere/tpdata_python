---
inclusion: manual
---

# Sprint 5 – Notebook 3: Conceptos Importantes de Tests Estadísticos

## Archivo (to be created)
`DS/Sprint 5/DS_Sprint5_class3.ipynb`

## Sprint
**SPRINT 5 – Análisis Estadístico de Datos**

## Webinar Fuente
`complements/TripleTen/Webinars/DA-DS/S3/Webinar 3.4 - Conceptos importantes de test estadísticos.md`

## Tema
Conceptos Importantes de Tests Estadísticos y A/B Testing

## Objetivos de Aprendizaje
- Comprender el **valor esperado** y su cálculo
- Entender qué es una **distribución de probabilidad** con ejemplos concretos (monedas)
- Aplicar el **Teorema Central del Límite** en contextos prácticos
- Diferenciar entre **tests de una cola y dos colas**
- Interpretar gráficos de distribución para **tomar decisiones de negocio**
- Aplicar **A/B testing** a un caso real de negocio

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Valor esperado y distribuciones de probabilidad | 25 mins |
| 3 | Teorema Central del Límite | 20 mins |
| 4 | Tests de una cola vs dos colas | 20 mins |
| 5 | Caso real: A/B testing en Amazon | 25 mins |
| 6 | Tips y buenas prácticas | 5 mins |
| 7 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber si el resultado de un experimento es real o producto del azar?
2. **Valor esperado** – cálculo con monedas cargadas y no cargadas; intuición: "promedio a largo plazo"; fórmula E[X] = Σ x·P(x)
3. **Distribuciones de probabilidad** – ejemplo con monedas; distribución binomial; visualización con histogramas; qué información nos da la forma de la distribución
4. **Teorema Central del Límite** – simulación visual: lanzar monedas N veces, mostrar cómo la distribución de medias se vuelve normal; por qué importa para los tests estadísticos
5. **Tests de una cola vs dos colas** – cuándo usar cada uno; visualización de las regiones de rechazo; relación con H₀ y H₁
6. **Cómo usar H₀ y H₁** – definición correcta; errores comunes; cómo formular la hipótesis antes de ver los datos
7. **Caso real: A/B testing en Amazon** – contexto del problema (inventado pero realista); definir H₀ y H₁; calcular el test; interpretar el resultado; tomar la decisión de negocio; cómo interpretar gráficos de distribución para determinar qué opción es más rentable
8. **Tips y buenas prácticas** – define H₀ before looking at data, use two-tailed unless you have a strong prior, report effect size not just p-value
9. **Cierre y Kahoot**

## Archivos de Apoyo del Complemento
- Board images: `S4_DS_Q&A_0_1.png` through `S4_DS_Q&A_0_6.png` (whiteboard photos from the webinar)

## Librerías Clave
`numpy`, `scipy.stats`, `matplotlib`, `seaborn`

## Notas de Estilo
- Amazon A/B testing case makes the content immediately applicable to business
- Whiteboard-style explanations with visual distributions
- Connects to Sprint 3 class1 (Pandas) — use a DataFrame to store the A/B test data

---
