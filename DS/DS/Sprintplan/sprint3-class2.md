---
inclusion: manual
---

# Sprint 3 – Notebook 2: Preprocesamiento de Datos

## Archivo
`DS/Sprint 3/DS_Sprint3_class2_Preprocesamiento_de_Datos.ipynb`

## Sprint
**SPRINT 3 – Manipulación de Datos (Data Wrangling)**

## Tema
Preprocesamiento de Datos

## Estado
✅ **CREADO**

## Objetivos de Aprendizaje
- Identificar y manejar **valores faltantes** (NaN) con distintas estrategias
- Detectar y tratar **valores atípicos (outliers)** con IQR
- Aplicar técnicas de **transformación de datos**: normalización, estandarización, encoding
- Comprender el impacto del preprocesamiento en la calidad de los modelos
- Construir un **pipeline básico de limpieza** reutilizable

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 min |
| 2 | Valores faltantes: detección y estrategias | 25 min |
| 3 | Outliers: detección y tratamiento | 20 min |
| 4 | Transformaciones: normalización y encoding | 20 min |
| 5 | Actividad práctica (Breakout Rooms) | 20 min |
| 6 | Tips y buenas prácticas | 5 min |
| 7 | Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Por qué los datos sucios generan conclusiones peligrosas?
2. **Valores faltantes** – `isnull().sum()`, porcentaje de nulos; tabla de estrategias (drop, media, mediana, moda, Unknown, interpolación)
3. **Outliers con IQR** – Q1, Q3, IQR, límites teóricos; boxplot + histograma con límites; cuándo eliminar vs conservar
4. **Transformaciones** – MinMaxScaler, StandardScaler; One-Hot Encoding con `pd.get_dummies()`
5. **Breakout Rooms** – pipeline completo: nulos → outliers → normalización → encoding → guardar
6. **Kahoot** – 5 preguntas

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn` (preprocessing)

## Notas de Estilo
- "Datos sucios = conclusiones peligrosas" as the motivating hook
- Always work with `.copy()` — emphasized throughout
- Penguin dataset used (publicly available, has NaN values)

---
