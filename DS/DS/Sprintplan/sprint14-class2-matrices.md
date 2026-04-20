---
inclusion: manual
---

# Sprint 14 – Notebook 2: Matrices en N-Dimensiones

## Archivo (to be created)
`DS/Sprint 14/DS_Sprint14_class2_matrices.ipynb`

## Sprint
**SPRINT 14 – Álgebra Lineal**

## Tema
Matrices en N-Dimensiones

## Objetivos de Aprendizaje
- Operar con **matrices** en múltiples dimensiones usando NumPy
- Comprender la **multiplicación de matrices** y su significado geométrico
- Calcular e interpretar la **matriz inversa** y la **transpuesta**
- Aplicar la **descomposición de matrices** (eigenvalues, eigenvectors) con intuición
- Conectar matrices con **PCA** y **reducción de dimensionalidad**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Operaciones matriciales con NumPy | 25 mins |
| 3 | Matriz inversa y transpuesta | 20 mins |
| 4 | Eigenvalues y eigenvectors: intuición | 20 mins |
| 5 | PCA: reducción de dimensionalidad | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo puede una transformación matemática revelar la estructura oculta de los datos?
2. **Operaciones matriciales** – `np.dot()`, `@` operator, `np.matmul()`; shapes y broadcasting; `np.zeros()`, `np.eye()`
3. **Transpuesta e inversa** – `A.T`, `np.linalg.inv()`; cuándo existe la inversa; `np.linalg.solve()` para sistemas de ecuaciones
4. **Eigenvalues y eigenvectors** – qué son (vectores que no cambian dirección bajo transformación); `np.linalg.eig()`; intuición geométrica con animación
5. **PCA** – qué hace PCA (encuentra los eigenvectors de la matriz de covarianza); `sklearn.decomposition.PCA`; explained variance ratio; visualización 2D de datos de alta dimensión
6. **Aplicaciones en DS** – PCA para visualización, compresión, eliminación de multicolinealidad; SVD en sistemas de recomendación
7. **Actividad práctica – Breakout Rooms** – students apply PCA to a high-dimensional dataset and visualize the result; spinner to pick presenter
8. **Tips y buenas prácticas** – always standardize before PCA, check explained variance, PCA loses interpretability
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`numpy`, `sklearn.decomposition`, `matplotlib`, `seaborn`

## Notas de Estilo
- Connects to Sprint 14 class1 (vectors) and Sprint 15 (gradient descent uses matrix operations)
- PCA demo: use Iris or a face dataset for visual impact
- Eigenvalue intuition: "directions that survive the transformation"

---
