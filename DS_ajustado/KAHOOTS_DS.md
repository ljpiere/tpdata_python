# Kahoots de las clases de Data Science

Cada sección corresponde a un archivo `.ipynb`. Se incluyen cuatro preguntas por clase; la opción correcta está marcada con ✅.

**Total:** 39 Kahoots y 156 preguntas.

## Sprint 1 — Sesión de Inducción a Data Science

**Fuente:** `DS/Sprint 1/DS_Sprint1_class1_Sesion_de_Induccion_a_Data_Science.ipynb`

1. ¿Qué hizo el clustering en la actividad de clase?

- Predijo las edades
- Agrupó perfiles similares ✅
- Eliminó datos faltantes
- Dibujó gráficos al azar

2. ¿Qué combinación de cualidades destaca la clase para un Data Scientist?

- Curiosidad, resiliencia y trabajo en equipo ✅
- Memorización, velocidad y trabajo individual
- Diseño gráfico, ventas y contabilidad
- Solo conocimientos avanzados de matemáticas

3. ¿Qué herramienta se usa principalmente para el análisis interactivo?

- Git
- GitHub
- Jupyter Notebook ✅
- PowerPoint

4. ¿Cuál es una finalidad de las visualizaciones en Data Science?

- Ocultar valores atípicos
- Comunicar patrones presentes en los datos ✅
- Reemplazar la limpieza de datos
- Evitar formular preguntas

## Sprint 1 — ABC de Python

**Fuente:** `DS/Sprint 1/DS_Sprint1_class2_ABC_de_Python.ipynb`

1. ¿Qué almacena una variable?

- Funciones

- Datos ✅

- Pantallas

2. ¿Cuál es un número entero?

- "25"

- 25 ✅

- "edad"

3. print() sirve para…

- Guardar datos

- Mostrar información ✅

- Crear variables

4. "Hola" es tipo…

- int

- str ✅

- float

## Sprint 2 — Bucles y Data Preprocessing

**Fuente:** `DS/Sprint 2/DS_Sprint2_class1_Bucles_y_Preprocesamiento.ipynb`

1. ¿Qué hace `for i in range(3)`?

- Itera 3 veces con i = 1, 2, 3
- Itera infinitamente
- Genera un error
- **Itera 3 veces con i = 0, 1, 2** ✅

2. ¿Cuándo usar `while` en lugar de `for`?

- Siempre que sea posible
- Cuando la lista tiene más de 100 elementos
- Cuando quieres iterar sobre una lista
- **Cuando no sabes cuántas iteraciones necesitas** ✅

3. ¿Qué hace `break` dentro de un bucle?

- Salta a la siguiente iteración
- Reinicia el bucle desde el principio
- Pausa el bucle temporalmente
- **Sale del bucle completamente** ✅

4. ¿Qué hace `df.isnull().sum()`?

- Elimina todos los valores nulos
- Rellena los nulos con cero
- Muestra las primeras filas del DataFrame
- **Cuenta los valores nulos por columna** ✅

## Sprint 2 — Funciones en Python

**Fuente:** `DS/Sprint 2/DS_Sprint2_class2_Funciones_en_Python.ipynb`

1. ¿Qué palabra clave se utiliza para definir una función en Python?


- function

- def ✅

- func

- create

2. ¿Qué hace una función en programación?

- Ejecuta código una sola vez

- Guarda datos permanentemente

- Agrupa código reutilizable para realizar una tarea específica ✅

- Solo imprime texto

3. ¿Qué imprimirá el siguiente código?
```
def saludar():
    print("Hola")

saludar()
```
- Error

- Nada

- Hola ✅

- saludar

4. ¿Qué son los parámetros en una función?

- Valores que recibe la función ✅

- Comentarios dentro de la función

- Librerías de Python

- Variables globales

## Sprint 3 — Introducción a Pandas

**Fuente:** `DS/Sprint 3/DS_Sprint3_class1_Introduccion_a_Pandas.ipynb`

1. ¿Qué librería de Python usamos principalmente para manipular datos en esta clase?

- NumPy  
- Matplotlib  
- Pandas ✅  
- Scikit-learn

2. ¿Qué estructura de datos principal usamos en Pandas para trabajar con tablas?

- Array  
- DataFrame ✅  
- Lista  
- Diccionario

3. ¿Qué función se utiliza para leer un archivo CSV en Pandas?

- `pd.read_excel()`  
- `pd.read_csv()` ✅  
- `pd.load_csv()`  
- `pd.import_csv()`

4. ¿Qué método permite ver las primeras filas de un DataFrame?

- `df.first()`  
- `df.start()`  
- `df.head()` ✅  
- `df.top()`

## Sprint 3 — Preprocesamiento de Datos

**Fuente:** `DS/Sprint 3/DS_Sprint3_class2_Preprocesamiento_de_Datos.ipynb`

1. ¿Qué hace df.isnull().sum()?

- Elimina todos los valores nulos del DataFrame
- Rellena los nulos con cero
- Muestra las primeras filas del DataFrame
- Cuenta los valores nulos por columna ✅

2. ¿Cuándo usar la mediana en lugar de la media para rellenar nulos?

- Siempre, la mediana es siempre mejor
- Cuando la columna tiene datos categoricos
- Cuando todos los valores son iguales
- Cuando hay outliers que distorsionarian la media ✅

3. ¿Qué es el IQR?

- El promedio de todos los valores
- La diferencia entre el maximo y el minimo
- Un tipo de grafico estadistico
- La diferencia entre el tercer y primer cuartil, Q3 - Q1✅

4. ¿Qué hace MinMaxScaler?

- Elimina los outliers del dataset
- Convierte variables categoricas en numericas
- Calcula la media y desviacion estandar
- Escala los valores entre 0 y 1 ✅

## Sprint 4 — Manejo Avanzado de Datos

**Fuente:** `DS/Sprint 4/DS_Sprint4_class1_Manejo_Avanzado_de_Datos.ipynb`

1. ¿Cuál es la diferencia entre `loc` e `iloc`?

- Son exactamente lo mismo
- `loc` usa etiquetas, `iloc` usa posición numérica ✅
- `loc` es más rápido que `iloc`
- `iloc` incluye el último elemento, `loc` no

2. ¿Qué hace `INNER JOIN`?

- Devuelve todas las filas de ambas tablas
- Solo devuelve filas con coincidencias en ambas tablas ✅
- Devuelve todas las filas de la tabla izquierda
- Devuelve todas las filas de la tabla derecha

3. ¿Para qué sirve `pivot_table()`?

- Para resumir datos multidimensionales con agregaciones ✅
- Para unir dos DataFrames
- Para limpiar valores nulos
- Para ordenar el DataFrame

4. ¿Qué hace `str.contains()`?

- Cuenta cuántas veces aparece un patrón
- Reemplaza un patrón por otro
- Verifica si un string contiene un patrón ✅
- Divide el string en una lista

## Sprint 4 — Gráficos de Visualización

**Fuente:** `DS/Sprint 4/DS_Sprint4_class2_Graficos_de_Visualizacion.ipynb`

1. ¿Por qué evitar los gráficos de pastel (pie charts)?

- Porque los humanos somos malos comparando ángulos ✅
- Porque son difíciles de programar
- Porque no funcionan en todos los navegadores
- Porque usan demasiada memoria

2. ¿Qué gráfico usar para mostrar tendencias en el tiempo?

- Histograma
- Gráfico de líneas ✅
- Boxplot
- Scatter plot

3. ¿Qué hace `sns.boxplot()`?

- Crea un gráfico de barras
- Muestra la correlación entre dos variables
- Muestra la distribución con cuartiles y outliers ✅
- Muestra la distribución de una variable continua

4. ¿Qué es el storytelling con datos?

- Inventar historias con los datos
- Comunicar hallazgos con una narrativa clara y convincente ✅
- Hacer gráficos animados
- Usar muchos colores en los gráficos

## Sprint 5 — Introducción a la Estadística y Probabilidad

**Fuente:** `DS/Sprint 5/DS_Sprint5_class1_Introduccion_a_la_Estadistica.ipynb`

1. ¿Qué medida de tendencia central es más robusta ante outliers?

- Media
- Moda
- Mediana ✅
- Varianza

2. ¿Qué dice el Teorema Central del Límite?

- Que todos los datos son normales
- Que la distribución de medias muestrales tiende a ser normal ✅
- Que la media siempre es 0
- Que necesitamos n > 1000

3. ¿Qué distribución usarías para modelar el número de emails spam por hora?

- Normal
- Poisson ✅
- Binomial
- Exponencial

4. Si la media es mucho mayor que la mediana, la distribución está...

- Sesgada a la izquierda
- Simétrica
- Sesgada a la derecha ✅
- Bimodal

## Sprint 5 — Ejercicios de Probabilidades: Bayes, Conjuntos y Entrevistas

**Fuente:** `DS/Sprint 5/DS_Sprint5_class2_Ejercicios_de_Probabilidades.ipynb`

1. ¿En el Problema de Monty Hall, deberías cambiar de puerta?

- No, la probabilidad es la misma en ambas puertas
- Sí, cambiar aumenta la probabilidad a 66.7% ✅
- No, es mejor quedarse con la elección original
- Solo si el presentador te lo sugiere

2. ¿Qué es el Teorema de Bayes?

- Una fórmula para calcular promedios
- Una forma de actualizar probabilidades con nueva evidencia ✅
- Un método para detectar outliers
- Una técnica de visualización de datos

3. ¿Cuál es la diferencia entre estadística frecuentista y bayesiana?

- La frecuentista usa más datos
- La bayesiana incorpora conocimiento previo (prior) ✅
- La bayesiana es más antigua
- La frecuentista es más precisa

4. ¿Qué son los outliers según el método IQR?

- Valores fuera de Q1 - 1.5 × IQR o Q3 + 1.5 × IQR ✅
- Valores iguales a la media
- Valores en el primer cuartil
- Valores entre Q1 y Q3

## Sprint 5 — Intro a Git: Qué es, para qué sirve y comandos básicos

**Fuente:** `DS/Sprint 5/DS_Sprint5_class3_Intro_a_Git_comandos_basicos.ipynb`

1. ¿Qué hace `git init`?

- Sube el repositorio a GitHub
- Hace un commit con todos los archivos
- Descarga un repositorio remoto
- **Inicializa un repositorio Git local** ✅

2. ¿Qué hace `git add .`?

- Hace un commit de todos los archivos
- Sube los archivos a GitHub
- Descarga cambios del remoto
- **Agrega todos los archivos al staging area** ✅

3. ¿Cuál es la diferencia entre Git y GitHub?

- Son exactamente lo mismo
- GitHub es más antiguo que Git
- Git es solo para proyectos grandes
- **Git es la herramienta local, GitHub es el servicio web** ✅

4. ¿Qué es un commit?

- Un error en el código
- Una rama del repositorio
- Un archivo de configuración
- **Una foto del estado del proyecto en un momento** ✅

## Sprint 6 — Simulación de Proyecto Alternativo

**Fuente:** `DS/Sprint 6/DS_Sprint6_class1_Simulacion_de_Proyecto_Modulo_1.ipynb`

1. ¿Cuál es el orden general del flujo practicado en el proyecto?

- Datos → limpieza → EDA → test → conclusiones ✅
- Test → conclusiones → datos → limpieza
- Visualización → datos → hipótesis → limpieza
- Conclusiones → EDA → recolección → test

2. ¿Cuándo deben formularse H₀ y H₁?

- Después de conocer el p-value
- Antes de ejecutar el test estadístico ✅
- Solo si el resultado no es significativo
- Después de redactar las conclusiones

3. ¿Qué decisión sobre valores nulos exige la actividad?

- Eliminarlos siempre
- Imputarlos siempre con cero
- Eliminar o imputar, justificando la decisión ✅
- Ignorarlos sin revisar su impacto

4. ¿Qué debe lograr una buena conclusión del proyecto?

- Enumerar todo el código utilizado
- Responder la pregunta de negocio con evidencia ✅
- Repetir únicamente las estadísticas descriptivas
- Presentar solo resultados técnicos

## Sprint 7 — Ambientes Virtuales, Reproducibilidad y Pull Requests

**Fuente:** `DS/Sprint 7/DS_Sprint7_class1_Ambientes_Virtuales_y_Pull_Requests.ipynb`

1. ¿Para qué sirve `requirements.txt`?

- Para documentar el proyecto
- Para reproducir el ambiente de un proyecto ✅
- Para configurar Git
- Para guardar los datos del proyecto

2. ¿Qué es un Pull Request?

- Una descarga de cambios del remoto
- Un tipo de commit especial
- Una solicitud para fusionar cambios de una rama a otra ✅
- Una rama de desarrollo

3. ¿Por qué usar ambientes virtuales?

- Para hacer el código más rápido
- Para aislar las dependencias de cada proyecto ✅
- Para ahorrar espacio en disco
- Para compartir librerías entre proyectos

4. ¿Qué debe ir en `.gitignore`?

- El archivo `README.md`
- El ambiente virtual, secretos y datos grandes ✅
- El archivo `requirements.txt`
- Los notebooks de Jupyter

## Sprint 7 — Git Avanzado

**Fuente:** `DS/Sprint 7/DS_Sprint7_class2_Git_Avanzado.ipynb`

1. ¿Cuál es la regla de oro del rebase?

- Siempre hacer rebase antes de cada commit
- Nunca hacer rebase de commits que ya están en una rama compartida ✅
- Solo hacer rebase en la rama main
- Hacer rebase después de cada push

2. ¿Qué hace `git cherry-pick`?

- Elimina un commit del historial
- Copia un commit específico a tu rama actual ✅
- Crea una rama nueva desde un commit
- Resuelve conflictos automáticamente

3. ¿Cuándo ocurre un conflicto de merge?

- Cuando haces push sin hacer pull primero
- Cuando dos personas modifican la misma línea del mismo archivo ✅
- Cuando borras una rama que alguien más está usando
- Siempre que haces rebase

4. ¿Qué estrategia de branching usa ramas muy cortas y merge frecuente?

- GitFlow
- Trunk-Based Development ✅
- Feature Branching largo
- Release Branching

## Sprint 7 — Programación Orientada a Objetos (OOP)

**Fuente:** `DS/Sprint 7/DS_Sprint7_class3_Programacion_Orientada_a_Objetos.ipynb`

1. ¿Qué es una instancia en OOP?

- Una clase abstracta
- Un objeto concreto creado a partir de una clase ✅
- Un método estático
- Un módulo de Python

2. ¿Qué hace el método `__init__`?

- Destruye el objeto cuando ya no se usa
- Inicializa los atributos al crear el objeto ✅
- Imprime el objeto en pantalla
- Hereda de otra clase automáticamente

3. ¿Qué principio OOP permite que `.fit()` funcione en cualquier modelo de sklearn?

- Encapsulación
- Abstracción
- Herencia
- Polimorfismo ✅

4. ¿Qué significa `self` en un método?

- La clase completa
- La instancia actual del objeto ✅
- El módulo donde está definida la clase
- El constructor de la clase padre

## Sprint 8 — Web Scraping con Python

**Fuente:** `DS/Sprint 8/DS_Sprint8_class1_Web_Scraping.ipynb`

1. ¿Qué librería se usa para hacer peticiones HTTP en Python?

- urllib
- requests ✅
- http
- socket

2. ¿Qué hace `soup.find_all('a')`?

- Encuentra el primer link de la página
- Encuentra todos los links de la página ✅
- Crea un nuevo link en el HTML
- Elimina todos los links

3. ¿Qué status code significa "Too Many Requests"?

- 200
- 403
- 404
- 429 ✅

4. ¿Qué archivo indica qué partes de un sitio se pueden scrapear?

- index.html
- robots.txt ✅
- sitemap.xml
- .htaccess

## Sprint 8 — SQL Avanzado

**Fuente:** `DS/Sprint 8/DS_Sprint8_class2_SQL_Avanzado.ipynb`

1. ¿Qué hace una Window Function que GROUP BY no puede?

- Filtrar filas antes de agrupar
- Calcular agregados sin colapsar las filas originales ✅
- Crear tablas temporales
- Hacer JOINs entre más de 2 tablas

2. ¿Qué es una CTE en SQL?

- Un tipo de índice para acelerar queries
- Una tabla temporal definida con WITH al inicio de la query ✅
- Un JOIN especial para tablas grandes
- Una constraint de integridad referencial

3. ¿Cómo evitas SQL injection en Python?

- Usando f-strings con validación manual
- Con queries parametrizadas usando ? o %s ✅
- Con try/except alrededor de la query
- Usando .format() con escape de caracteres

4. ¿Qué función de Pandas ejecuta una query SQL y devuelve un DataFrame?

- pd.query()
- pd.read_sql() ✅
- pd.from_sql()
- pd.execute()

## Sprint 9 — Modelos de Aprendizaje automático

**Fuente:** `DS/Sprint 9/DS_Sprint9_class1_Modelos_de_Aprendizaje_Automatico.ipynb`

1. ¿Qué es Machine Learning?

- Programar reglas manualmente  
- Aprender patrones a partir de datos ✅  
- Dibujar gráficos  
- Guardar información

2. ¿Cuál de estos es un problema de clasificación?

- Predecir el precio de una casa  
- Agrupar clientes  
- Detectar spam en correos ✅  
- Calcular promedio

3. ¿Qué es una frontera de decisión?

- Una línea que separa clases ✅  
- Un tipo de dataset  
- Una métrica  
- Un algoritmo

4. ¿Qué mide el accuracy?

- Cantidad de datos  
- Porcentaje de aciertos ✅  
- Tiempo de entrenamiento  
- Número de variables

## Sprint 9 — Primer Modelo y KNN

**Fuente:** `DS/Sprint 9/DS_Sprint9_class2_Primer_Modelo_y_KNN.ipynb`

1. ¿Qué tipo de algoritmo es KNN?

- Paramétrico y eager learner
- No paramétrico y lazy learner ✅
- Paramétrico y lazy learner
- No paramétrico y eager learner

2. ¿Qué distancia mide el ángulo entre vectores en lugar de su magnitud?

- Euclidiana
- Manhattan
- Coseno ✅
- Chebyshev

3. ¿Qué pasa si usamos k=1 en KNN?

- El modelo se vuelve demasiado simple
- El modelo memoriza el ruido de los datos ✅
- El modelo no puede hacer predicciones
- El modelo siempre predice la clase mayoritaria

4. ¿Por qué es importante usar StandardScaler con KNN?

- Porque KNN requiere datos categóricos
- Porque las features con mayor escala dominan el cálculo de distancias ✅
- Porque reduce el número de features
- Porque elimina los outliers automáticamente

## Sprint 10 — Métricas de Evaluación

**Fuente:** `DS/Sprint 10/DS_Sprint10_class1_Metricas_de_Evaluacion.ipynb`

1. Un modelo de detección de fraude tiene 99% accuracy pero 0% recall. ¿Qué está pasando?

- El modelo es excelente y no necesita mejoras
- El dataset está balanceado y el modelo funciona bien
- El modelo predice siempre "no fraude" en un dataset desbalanceado ✅
- El modelo tiene overfitting severo

2. ¿Qué mide el Recall?

- De todos los que marqué positivos, ¿cuántos lo eran realmente?
- De todos los que realmente son positivos, ¿cuántos detecté? ✅
- El porcentaje total de aciertos del modelo
- La proporción de falsos positivos

3. Para un sistema de detección de incendios, ¿qué métrica priorizarías?

- Accuracy
- Precision
- Recall ✅
- Specificity

4. ¿Qué significa un AUC de 0.5?

- El modelo es perfecto
- El modelo es tan bueno como tirar una moneda al azar ✅
- El modelo siempre acierta la clase positiva
- El modelo tiene precisión perfecta

## Sprint 10 — Comparación de Modelos y Cross-Validation

**Fuente:** `DS/Sprint 10/DS_Sprint10_class2_Comparacion_y_Cross_Validation.ipynb`

1. ¿Cuántas veces se entrena un modelo en 5-Fold Cross-Validation?

- 1 vez
- 5 veces ✅
- 10 veces
- Depende del dataset

2. ¿Qué ventaja tiene Stratified k-Fold sobre k-Fold regular?

- Es más rápido de calcular
- Mantiene la proporción de clases en cada fold ✅
- Usa menos memoria RAM
- Elimina outliers automáticamente

3. Si train_score=0.99 y test_score=0.65, tu modelo probablemente tiene:

- High bias (underfitting)
- High variance (overfitting) ✅
- Buen equilibrio
- Un bug en el código

4. GridSearchCV combina:

- Solo búsqueda de hiperparámetros
- Solo cross-validation
- Búsqueda de hiperparámetros + cross-validation ✅
- Entrenamiento con todo el dataset sin validación

## Sprint 11 — Tratamiento de Datos Desbalanceados

**Fuente:** `DS/Sprint 11/DS_Sprint11_class1_Datos_Desbalanceados.ipynb`

1. ¿Qué hace un DummyClassifier con strategy='most_frequent'?

- Predice aleatoriamente
- Predice siempre la clase mayoritaria ✅
- Usa un árbol de decisión simple
- Predice la clase con mayor F1

2. ¿Qué problema tiene usar accuracy como métrica en datos desbalanceados?

- Es muy lenta de calcular
- No funciona con más de 2 clases
- Puede ser alta sin detectar la clase minoritaria ✅
- Siempre da valores menores a 0.5

3. ¿Qué hace SMOTE?

- Elimina datos de la clase mayoritaria
- Duplica exactamente los datos minoritarios
- Genera puntos sintéticos interpolando entre vecinos de la clase minoritaria ✅
- Ajusta los pesos internos del modelo

4. ¿Cuándo se debe aplicar SMOTE?

- Antes de hacer train_test_split
- Solo al conjunto de test
- Solo al conjunto de entrenamiento ✅
- A todo el dataset completo

## Sprint 11 — Feature Engineering, Encoding y Selección de Características

**Fuente:** `DS/Sprint 11/DS_Sprint11_class2_Feature_Engineering.ipynb`

1. ¿Cuándo se debe usar One-Hot Encoding?

- Cuando las categorías tienen un orden natural
- Cuando las categorías son nominales (sin orden) ✅
- Solo cuando hay más de 10 categorías
- Solo para variables numéricas

2. ¿Qué hace np.log1p(x)?

- Calcula la raíz cuadrada de x
- Calcula log(x + 1), útil para reducir sesgo en distribuciones ✅
- Normaliza x entre 0 y 1
- Eleva x a la potencia e

3. ¿Qué mide la correlación de Pearson?

- Cualquier tipo de relación entre variables
- Solo relaciones lineales entre dos variables ✅
- La importancia de un feature para el modelo
- La distancia entre dos puntos

4. ¿Qué hace SelectKBest?

- Selecciona las k muestras más representativas
- Elimina las k columnas más correlacionadas
- Selecciona los k features con mejor score estadístico ✅
- Aplica PCA para reducir a k dimensiones

## Sprint 12 — Bootstrapping, Data Leakage y Pipelines Profesionales

**Fuente:** `DS/Sprint 12/DS_Sprint12_class1_Bootstrapping_y_Pipelines.ipynb`

1. ¿Qué es bootstrapping?

- Un método para limpiar datos
- Muestreo con reemplazo para estimar distribuciones de estadísticas ✅
- Una técnica de regularización
- Un tipo de cross-validation

2. ¿Cuál es un ejemplo de target leakage?

- Usar datos del futuro en series temporales
- Usar una variable que se genera DESPUÉS del evento a predecir ✅
- Hacer fit del scaler en todo el dataset
- No usar cross-validation

3. ¿Qué previene automáticamente un sklearn Pipeline?

- Overfitting
- Train-test contamination en preprocesamiento ✅
- Que el modelo sea muy lento
- Que haya valores nulos

4. ¿Qué red flag indica posible data leakage?

- Accuracy baja en train y test
- El modelo tarda mucho en entrenar
- Rendimiento sospechosamente alto que cae en producción ✅
- Features con muchos valores nulos

## Sprint 12 — Modularización y Estructura Profesional de Proyectos

**Fuente:** `DS/Sprint 12/DS_Sprint12_class2_Modularizacion.ipynb`

1. ¿Dónde se guardan los datos crudos en un proyecto profesional?

- En la carpeta output/
- En la carpeta input/ (sin modificarlos nunca) ✅
- En la carpeta models/
- En el mismo archivo que el código

2. ¿Qué contiene params.py?

- Las funciones de preprocesamiento
- Los datos de entrenamiento
- Los parámetros y configuración centralizada del proyecto ✅
- Las predicciones del modelo

3. ¿Qué librería se recomienda para guardar modelos de sklearn?

- pickle (siempre)
- json
- joblib (más eficiente para arrays numpy) ✅
- csv

4. ¿Qué se guarda con joblib.dump(pipeline, path)?

- Solo los pesos del modelo
- Solo el preprocesamiento
- El Pipeline completo (preprocesamiento + modelo entrenado) ✅
- Solo los hiperparámetros

## Sprint 13 — Simulacro de Proyecto Integrado de Machine Learning

**Fuente:** `DS/Sprint 13/DS_Sprint13_class1_Simulacro_Proyecto_ML.ipynb`

1. ¿Cuál es la métrica más apropiada cuando queremos minimizar falsos negativos?

- Precision
- Recall ✅
- Accuracy
- F1-Score

2. ¿Qué componente de sklearn permite combinar preprocesamiento numérico y categórico?

- Pipeline
- ColumnTransformer ✅
- GridSearchCV
- StandardScaler

3. ¿Por qué es importante hacer feature engineering antes de entrenar?

- Para que el modelo tenga más columnas siempre
- Para crear relaciones que el modelo no descubriría solo ✅
- Para eliminar todas las columnas originales
- Porque sklearn lo requiere obligatoriamente

4. ¿Qué significa un recall de 0.90 en un modelo de churn?

- El modelo acierta 90% de todas las predicciones
- De los clientes que sí se van, detecta al 90% ✅
- Solo 10% de predicciones positivas son correctas
- El modelo tiene 90% de accuracy

## Sprint 14 — Intuición del Álgebra Lineal: Vectores, Distancias y Transformaciones

**Fuente:** `DS/Sprint 14/DS_Sprint14_class1_Algebra_Lineal.ipynb`

1. ¿Qué mide el producto punto de dos vectores?

- La distancia entre ellos
- Su alineación o similitud direccional ✅
- El ángulo exacto en grados
- La suma de sus componentes

2. ¿Cuál distancia mide "caminar por cuadras" (solo horizontal y vertical)?

- L2 (Euclidiana)
- Coseno
- L1 (Manhattan) ✅
- Minkowski

3. ¿Qué hace una matriz de rotación cuando multiplica un vector?

- Lo escala
- Lo refleja
- Lo gira un ángulo sin cambiar su magnitud ✅
- Lo elimina

4. ¿Por qué la similitud coseno ignora la magnitud de los vectores?

- Porque normaliza dividiendo por las normas ✅
- Porque solo usa la primera componente
- Porque resta los vectores antes de comparar
- Porque usa valor absoluto

## Sprint 14 — Gradiente descendiente y función de costo

**Fuente:** `DS/Sprint 14/DS_Sprint14_class1_Gradiente_Descendiente_y_Funcion_de_Costo.ipynb`

1. ¿Cuál es el objetivo de Gradient Descent?

- Maximizar el error  
- Minimizar la función de costo ✅  
- Dibujar gráficas  
- Normalizar datos

2. ¿Qué representa la función de costo?

- El tamaño del dataset  
- El error del modelo ✅  
- El número de variables  
- El learning rate

3. ¿Qué ocurre si el learning rate es demasiado grande?

- El modelo converge más rápido  
- El algoritmo puede divergir ✅  
- El error siempre baja  
- No pasa nada

4. ¿Qué ocurre si el learning rate es muy pequeño?

- El entrenamiento es más lento ✅  
- El modelo falla siempre  
- El error aumenta  
- No afecta el resultado

## Sprint 14 — Matrices, Eigenvalues y Reducción de Dimensionalidad (PCA)

**Fuente:** `DS/Sprint 14/DS_Sprint14_class2_Matrices_y_PCA.ipynb`

1. ¿Qué es un eigenvector de una matriz A?

- Un vector que A hace cero
- Un vector que A solo escala (no rota) ✅
- El vector más largo de A
- La diagonal de A

2. ¿Qué maximiza PCA al elegir componentes principales?

- La distancia entre clases
- La varianza explicada de los datos ✅
- El accuracy de un modelo
- El número de features

3. Si las primeras 2 PCs capturan 95% de varianza de un dataset de 50 features, ¿qué implica?

- Los datos tienen estructura lineal de baja dimensión ✅
- El dataset tiene errores
- Se necesitan las 50 features para el modelo
- PCA no es aplicable

4. ¿Por qué es OBLIGATORIO escalar antes de PCA?

- Porque PCA solo funciona con datos entre 0 y 1
- Porque features con mayor escala dominarían las componentes ✅
- Porque sklearn da error sin escalar
- Porque los eigenvectors requieren datos positivos

## Sprint 15 — Introducción a las Redes Neuronales Artificiales (ANN)

**Fuente:** `DS/Sprint 15/DS_Sprint15_class1_Introduccion_a_ANN.ipynb`

1. ¿Qué función de activación se usa por defecto en capas ocultas?

- Sigmoid
- Softmax
- ReLU ✅
- Lineal

2. ¿Qué hace Dropout en una red neuronal?

- Agrega más neuronas
- Desactiva neuronas al azar para prevenir overfitting ✅
- Aumenta el learning rate
- Normaliza los datos de entrada

3. ¿Qué es backpropagation?

- Cuando los datos fluyen de entrada a salida
- El proceso de ajustar pesos propagando el error hacia atrás ✅
- Una función de activación especial
- Un tipo de regularización

4. ¿Cuántas neuronas de salida necesitas para clasificar 5 clases?

- 1
- 2
- 5 ✅
- 10

## Sprint 15 — Gradient Descent Avanzado: Learning Rate, Momentum y Adam

**Fuente:** `DS/Sprint 15/DS_Sprint15_class2_Gradient_Descent_Avanzado.ipynb`

1. ¿Qué pasa si el learning rate es demasiado grande?

- El modelo converge más rápido
- El modelo diverge: la pérdida sube ✅
- No tiene ningún efecto
- El modelo hace underfitting

2. ¿Qué variante de GD usa UN solo dato por paso?

- Batch Gradient Descent
- Mini-batch Gradient Descent
- Stochastic Gradient Descent (SGD) ✅
- Adam

3. ¿Cuál es la intuición detrás de "momentum"?

- Usar gradientes de segundo orden
- Acumular velocidad como una bola rodando ✅
- Multiplicar el gradiente por un número grande
- Cambiar el learning rate en cada paso

4. ¿Por qué el feature scaling ayuda a gradient descent?

- Hace la superficie de pérdida más "redonda" y facilita la convergencia ✅
- Porque sklearn lo requiere obligatoriamente
- Porque reduce el número de features
- Porque convierte datos categóricos a numéricos

## Sprint 16 — Series de Tiempo: Descomposición de Señal

**Fuente:** `DS/Sprint 16/DS_Sprint16_class1_Series_de_Tiempo_Descomposicion.ipynb`

1. ¿Cuáles son los tres componentes de una serie de tiempo?

- Media, varianza y covarianza
- Tendencia, estacionalidad y residuos ✅
- Promedio, mediana y moda
- Señal, ruido y frecuencia

2. ¿Qué modelo de descomposición usamos cuando la amplitud estacional crece con la tendencia?

- Aditivo
- Logarítmico
- Multiplicativo ✅
- Exponencial

3. ¿Qué indica un p-value < 0.05 en el test ADF?

- La serie tiene tendencia
- La serie NO es estacionaria
- La serie ES estacionaria ✅
- El modelo es significativo

4. ¿Qué función nos ayuda a identificar el parámetro p de un modelo AR?

- ACF
- PACF ✅
- ADF
- Seasonal decompose

## Sprint 16 — Modelos ARIMA y Predicción Temporal

**Fuente:** `DS/Sprint 16/DS_Sprint16_class2_ARIMA_y_Prediccion.ipynb`

1. ¿Qué representa el parámetro "d" en ARIMA(p,d,q)?

- Número de componentes autoregresivos
- Número de diferenciaciones para estacionariedad ✅
- Grado del promedio móvil
- Dimensión del modelo

2. ¿Cómo debe hacerse el split train/test en series de tiempo?

- Aleatorio con random_state=42
- Estratificado por valores
- Cronológico: pasado entrena, futuro evalúa ✅
- 50/50 alternando filas

3. ¿Qué criterio usa auto_arima para elegir el mejor modelo?

- RMSE
- R²
- AIC (Akaike Information Criterion) ✅
- Accuracy

4. ¿Qué agrega SARIMA respecto a ARIMA?

- Más datos de entrenamiento
- Componentes estacionales (P, D, Q, m) ✅
- Mejor optimización numérica
- Datos exógenos

## Sprint 17 — Introducción al Procesamiento de Lenguaje Natural (NLP)

**Fuente:** `DS/Sprint 17/DS_Sprint17_class1_Introduccion_a_NLP.ipynb`

1. ¿Qué es la tokenización en NLP?

- Traducir texto a otro idioma
- Dividir el texto en unidades (palabras, oraciones) ✅
- Eliminar palabras repetidas
- Convertir texto a números

2. ¿Qué son las stopwords?

- Palabras con errores ortográficos
- Palabras muy frecuentes que no aportan significado ✅
- Palabras en inglés dentro de texto en español
- Palabras con más de 10 letras

3. ¿Qué ventaja tiene TF-IDF sobre Bag of Words?

- Es más rápido de calcular
- Produce vectores más pequeños
- Penaliza palabras muy comunes y destaca las discriminantes ✅
- No necesita preprocesamiento

4. ¿Por qué LogisticRegression funciona bien para clasificación de texto?

- Porque maneja bien features de alta dimensión ✅
- Porque es un modelo no lineal
- Porque no necesita datos de entrenamiento
- Porque entiende gramática

## Sprint 17 — Embeddings, Modelos Pre-entrenados e Introducción a LLMs

**Fuente:** `DS/Sprint 17/DS_Sprint17_class2_Embeddings_y_LLMs.ipynb`

1. ¿Qué problema de BoW/TF-IDF resuelven los embeddings?

- La velocidad de entrenamiento
- La captura de significado semántico ✅
- El tamaño del dataset
- La privacidad de los datos

2. ¿Qué resultado produce la analogía king - man + woman en Word2Vec?

- king
- man
- queen ✅
- woman

3. ¿Cuál es la idea central de Word2Vec?

- Palabras frecuentes son más importantes
- Palabras en contextos similares tienen significados similares ✅
- Las palabras largas son más informativas
- El orden de las palabras no importa

4. ¿Qué ventaja tienen los embeddings contextuales (BERT) sobre Word2Vec?

- Son más rápidos
- El vector de una palabra cambia según el contexto ✅
- Usan menos memoria
- No necesitan entrenamiento

## Sprint 18 — Redes Neuronales Artificiales (ANN) y CNN para Imágenes

**Fuente:** `DS/Sprint 18/DS_Sprint18_class1_Redes_Neuronales_y_CNN.ipynb`

1. ¿Qué hace una capa convolucional (Conv2D)?

- Reduce el tamaño de la imagen
- Aplica filtros que detectan patrones locales ✅
- Conecta todas las neuronas entre sí
- Aplana la imagen a un vector

2. ¿Cuál es la función de activación recomendada para capas ocultas?

- Sigmoid
- Softmax
- ReLU ✅
- Lineal

3. ¿Qué hace MaxPooling2D?

- Aumenta la resolución de la imagen
- Reduce la dimensión espacial tomando el máximo ✅
- Agrega más filtros
- Normaliza los valores

4. ¿Qué función de activación usamos en la capa de salida para clasificación multi-clase?

- ReLU
- Sigmoid
- Softmax ✅
- Tanh

## Sprint 18 — Aprendizaje No Supervisado: Clustering y PCA

**Fuente:** `DS/Sprint 18/DS_Sprint18_class2_Aprendizaje_No_Supervisado.ipynb`

1. ¿Cuál es la principal diferencia entre aprendizaje supervisado y no supervisado?

- La cantidad de datos necesarios
- Si los datos tienen etiquetas o no ✅
- La velocidad del algoritmo
- El lenguaje de programación usado

2. ¿Qué criterio usa K-Means para asignar puntos a clusters?

- Similitud coseno
- Correlación de Pearson
- Distancia euclídea al centroide más cercano ✅
- Frecuencia de aparición

3. ¿Qué indica el "codo" en el método del codo?

- Que el modelo está sobreajustado
- El k donde agregar más clusters ya no mejora significativamente ✅
- Que hay un error en los datos
- El punto de convergencia del algoritmo

4. ¿Qué rango de valores tiene el silhouette score?

- 0 a 100
- -1 a 1 ✅
- 0 a 1
- -infinito a infinito

## Sprint 19 — Metodologías de Trabajo en Data Science

**Fuente:** `DS/Sprint 19/DS_Sprint19_class1_Metodologias_de_Trabajo.ipynb`

1. ¿Con qué fase comienza CRISP-DM?

- Modelado
- Entendimiento del negocio ✅
- Preparación de datos
- Despliegue

2. ¿Por qué CRISP-DM es una metodología iterativa?

- Porque obliga a repetir siempre el modelado
- Porque los hallazgos pueden requerir volver a fases anteriores ✅
- Porque elimina la documentación final
- Porque cada fase pertenece a un equipo distinto

3. ¿Qué propone Agile para entregar valor temprano en Data Science?

- Esperar hasta tener el modelo perfecto
- Crear un baseline o MVP e iterar con feedback ✅
- Evitar mostrar resultados parciales
- Trabajar sin backlog ni prioridades

4. ¿Qué práctica favorece la reproducibilidad?

- Usar rutas absolutas del equipo personal
- Modificar directamente los datos raw
- Fijar seeds y registrar versiones de dependencias ✅
- Ejecutar las celdas del notebook fuera de orden

## Sprint 19 — Proyecto Final: Simulación, Peer Review y Cierre

**Fuente:** `DS/Sprint 19/DS_Sprint19_class2_Proyecto_Final.ipynb`

1. ¿Cuántas fases tiene CRISP-DM?

- 4
- 5
- 6 ✅
- 8

2. ¿Qué fase de CRISP-DM consume más tiempo en la práctica?

- Business Understanding
- Data Preparation ✅
- Modeling
- Deployment

3. ¿Cuál es la métrica más apropiada cuando tienes clases desbalanceadas?

- Accuracy
- F1-score ✅
- R²
- MSE

4. ¿Qué archivo es el MÁS importante en un repositorio de proyecto de DS?

- model.pkl
- data.csv
- README.md ✅
- requirements.txt
