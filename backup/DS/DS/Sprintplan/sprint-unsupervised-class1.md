---
inclusion: manual
---

# Sprint * – Notebook 1: Aprendizaje No Supervisado (Clustering)

## Archivo (to be created)
`DS/Sprint Unsupervised/DS_SprintUnsupervised_class1.ipynb`

## Sprint
**SPRINT * – Aprendizaje No Supervisado**

## Tema
Estudio de ML Enfocado a Tareas de Clustering

## Nota
This is a special sprint (marked with * in the planning document). It covers unsupervised learning and may be placed between Sprints 10–12 or as a standalone module depending on the curriculum schedule.

## Objetivos de Aprendizaje
- Comprender la diferencia entre **aprendizaje supervisado y no supervisado**
- Aplicar el algoritmo **K-Means** para segmentación de datos
- Determinar el número óptimo de clusters con el **método del codo** y la **silueta**
- Aplicar **clustering jerárquico** y leer dendrogramas
- Interpretar y comunicar los resultados del clustering en contexto de negocio

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Aprendizaje no supervisado: conceptos | 15 mins |
| 3 | K-Means: algoritmo e implementación | 30 mins |
| 4 | Número óptimo de clusters | 20 mins |
| 5 | Clustering jerárquico | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo encontrar grupos naturales en datos sin etiquetas?
2. **Aprendizaje no supervisado** – sin etiquetas; clustering vs dimensionality reduction; casos de uso: segmentación de clientes, detección de anomalías, compresión
3. **K-Means** – algoritmo paso a paso (inicialización, asignación, actualización de centroides); `KMeans` de sklearn; visualización de clusters; inertia
4. **Número óptimo de clusters** – método del codo (elbow method); silhouette score; `silhouette_samples()`; visualización
5. **Clustering jerárquico** – agglomerative clustering; dendrograma; `scipy.cluster.hierarchy`; cuándo usar vs K-Means
6. **Interpretación de negocio** – cómo describir cada cluster; perfiles de segmentos; acciones de negocio por segmento
7. **Actividad práctica – Breakout Rooms** – students segment customers using K-Means and describe each segment; spinner to pick presenter
8. **Tips y buenas prácticas** – always scale before clustering, K-Means assumes spherical clusters, validate with domain knowledge
9. **Cierre y Kahoot**

## Imágenes Utilizadas
- Connects to `../Images/S1_DS_no_idea.jpeg` (Sprint 1 used KMeans as a demo — this sprint explains it properly)

## Librerías Clave
`sklearn` (KMeans, AgglomerativeClustering, silhouette_score), `scipy.cluster.hierarchy`, `pandas`, `numpy`, `matplotlib`, `seaborn`

## Notas de Estilo
- Connects back to Sprint 1 class1 where KMeans was used as a "magic demo" — now students understand it
- Customer segmentation is the most relatable business use case
- Elbow method visualization is the key "aha moment"

---
