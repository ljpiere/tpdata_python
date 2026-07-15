---
inclusion: manual
---

# Sprint 3 – Notebook 4: Conceptos Importantes de Tests Estadísticos

## Archivo
`DS/Sprint 3/DS_Sprint3_class4_Conceptos_de_Tests_Estadisticos.ipynb`

## Sprint
**SPRINT 3 – Manipulación de Datos (Data Wrangling)**

## Webinar Fuente
`complements/TripleTen/Webinars/DA-DS/S3/Webinar 3.4 - Conceptos importantes de test estadísticos.md`

## Tema
Conceptos Importantes de Tests Estadísticos y A/B Testing

## Estado
✅ **CREADO**

## Objetivos de Aprendizaje
- Comprender el **valor esperado** y su cálculo con ejemplos de monedas
- Entender qué es una **distribución de probabilidad**
- Aplicar el **Teorema Central del Límite** intuitivamente con simulación visual
- Diferenciar entre **tests de una cola y dos colas**
- Aplicar **A/B testing** a un caso real de negocio (Amazon)

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 min |
| 2 | Valor esperado y distribuciones de probabilidad | 25 min |
| 3 | Teorema Central del Límite | 20 min |
| 4 | Tests de una cola vs dos colas | 20 min |
| 5 | Caso real: A/B testing en Amazon | 25 min |
| 6 | Tips y buenas prácticas | 5 min |
| 7 | Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo saber si el resultado de un experimento es real o producto del azar?
2. **Valor esperado** – moneda justa vs cargada; E[X] = Σ x·P(x); simulación 1000 lanzamientos
3. **TCL** – demostración visual: distribución uniforme → medias muestrales → normal; 6 subplots con n=1,5,10,30,50,100
4. **Tests de una/dos colas** – tabla H₀/H₁; visualización de regiones de rechazo (3 subplots)
5. **A/B Testing Amazon** – botón azul vs naranja; `proportions_ztest`; visualización tasas + distribución Z; decisión de negocio
6. **Breakout Rooms** – A/B test de email marketing (asunto A vs B)
7. **Kahoot** – 5 preguntas

## Librerías Clave
`numpy`, `scipy.stats`, `matplotlib`, `statsmodels`

## Notas de Estilo
- Business context for every example
- Visual-first: distributions shown before formulas
- Amazon case makes A/B testing immediately applicable

---
