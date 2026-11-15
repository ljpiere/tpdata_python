# Informe de auditoría de notebooks de Data Science

## 1. Alcance

Se revisaron los 78 notebooks activos de `DS` contra `DA/GUIA_EVALUACION_NOTEBOOKS_CURSO_DATA.md`:

- 39 notebooks de tutor en `DS/DS`;
- 39 versiones de estudiante en `DS/DS_students`.

No se encontraron notebooks en carpetas `backup` o `.ipynb_checkpoints` dentro de este alcance. La revisión fue estática: estructura JSON, metadatos, celdas, Markdown, código, outputs guardados, errores guardados, rutas, recursos y correspondencia tutor/estudiante. No equivale a certificar `Restart/Run All`, porque no se ejecutaron los 39 flujos ni sus operaciones externas.

## 2. Resultado ejecutivo

**Todos los notebooks requieren al menos una actualización antes de considerarse plenamente conformes con la guía.** La severidad no es la misma:

- **2 pares tienen bloqueos críticos** y no deberían publicarse hasta corregirlos.
- **21 notebooks de tutor con código no muestran evidencia de ejecución**; requieren prueba en kernel limpio.
- **36 de 39 notebooks de tutor no declaran prerrequisitos** de forma explícita.
- **35 de 39 no declaran entregable o resultado esperado** de forma explícita.
- **18 de 39 no incluyen ayuda, soporte o recursos de cierre** identificables.
- **26 de 39 notebooks de tutor** carecen de IDs en una o más celdas.
- **Las 39 versiones de estudiante** tienen al menos algunas celdas sin ID.
- **Las 39 versiones de estudiante cumplen la limpieza básica:** cero outputs, cero `execution_count` y cero errores guardados.
- Los 78 archivos se pudieron interpretar como JSON de notebook; no se detectó corrupción estructural básica.

La colección tiene fortalezas claras: todos los notebooks incluyen objetivos, agenda, contexto o pregunta guía, actividades o validación y un cierre reconocible. Las versiones de estudiante agregan instrucciones de uso, notas y espacios de trabajo.

## 3. Bloqueos críticos

### 3.1 Sprint 2, clase 2 — Funciones en Python

Archivos afectados:

- `DS/DS/Sprint 2/DS_Sprint2_class2_Funciones_en_Python.ipynb`
- `DS/DS_students/Sprint 2/DS_Sprint2_class2_Funciones_en_Python_students_version.ipynb`

El notebook del tutor guarda un `NameError`: se llama a `calcular_promedio(datos)` sin que la función esté definida en el estado ejecutado. Debe definirse antes de usarla, comprobar el orden de celdas y ejecutar el notebook completo desde un kernel limpio. Después debe revisarse o regenerarse la versión estudiante para mantener la correspondencia.

### 3.2 Sprint 3, clase 1 — Introducción a pandas

Archivos afectados:

- `DS/DS/Sprint 3/DS_Sprint3_class1_Introduccion_a_Pandas.ipynb`
- `DS/DS_students/Sprint 3/DS_Sprint3_class1_Introduccion_a_Pandas_students_version.ipynb`

Ambos contienen `pd.read_excel("data.xlsx")`, pero ese archivo no existe en la carpeta `DS`. El tutor guarda un `FileNotFoundError` y un traceback que expone una ruta local del autor. Se debe agregar un archivo de ejemplo con ruta relativa estable, generar el DataFrame dentro del notebook o convertir el fragmento en ejemplo no ejecutable. Luego hay que ejecutar el tutor sin errores y limpiar/sincronizar la versión estudiante.

## 4. Cambios transversales requeridos

### 4.1 En los 39 pares

1. Añadir un bloque inicial uniforme con:
   - audiencia y tipo de sesión;
   - prerrequisitos técnicos y conceptuales;
   - dependencias o referencia explícita a `DS/requirements.txt`;
   - entregable o resultado observable;
   - instrucciones de ejecución y duración.
2. Añadir criterios de logro para cada actividad principal.
3. Asegurar que el cierre responda la pregunta guía e incluya limitaciones y siguientes pasos.
4. Normalizar el notebook a `nbformat` 4 con IDs válidos en todas las celdas.
5. Mantener la misma consigna y criterio de aceptación en tutor y estudiante.

### 4.2 En los notebooks de tutor

1. Ejecutar `Restart Kernel and Run All` en el entorno soportado.
2. Corregir errores y advertencias relevantes; no publicar tracebacks ni rutas privadas.
3. Guardar outputs útiles y manejables que funcionen como referencia del resultado esperado.
4. Incluir solución razonada o criterio verificable para toda actividad obligatoria.
5. Documentar semillas, fuentes de datos y operaciones externas cuando apliquen.

### 4.3 En las versiones de estudiante

1. Conservar outputs y contadores limpios, como ya ocurre.
2. Revisar que cada espacio de trabajo tenga una consigna concreta; una celda vacía no basta.
3. Usar `TODO estudiante` de forma consistente en ejercicios de código. Actualmente algunos notebooks tienen espacios de trabajo, pero ningún `TODO` explícito.
4. Regenerar o sincronizar cada versión después de modificar su notebook tutor.
5. Comprobar que no queden soluciones evaluadas dentro de demostraciones aparentemente neutrales.

## 5. Convenciones usadas en la revisión por archivo

- **Bloqueado:** existe una falla crítica observable.
- **Alta:** falta evidencia de ejecución completa o hay warnings/deprecaciones guardadas.
- **Media:** el flujo parece utilizable, pero faltan elementos de la guía.
- **T:** cambio en el notebook tutor.
- **E:** cambio en la versión estudiante.
- **Ambos:** el cambio de contenido debe reflejarse en las dos versiones.

En la tabla, el nombre base representa estos dos archivos:

- tutor: `DS/DS/Sprint N/<nombre>.ipynb`;
- estudiante: `DS/DS_students/Sprint N/<nombre>_students_version.ipynb`.

## 6. Revisión de cada par de notebooks

| Sprint | Notebook base | Prioridad | Archivos a cambiar | Cambios principales |
|---:|---|---|---|---|
| 1 | `DS_Sprint1_class1_Sesion_de_Induccion_a_Data_Science` | Media | Ambos | Añadir prerrequisitos y entregable; completar IDs de las celdas nuevas de estudiante; verificar nuevamente el tutor en kernel limpio. |
| 1 | `DS_Sprint1_class2_ABC_de_Python` | Media | Ambos | Añadir prerrequisitos y entregable; convertir espacios de práctica en consignas verificables; completar IDs de estudiante. |
| 2 | `DS_Sprint2_class1_Bucles_y_Preprocesamiento` | Media | Ambos | Añadir prerrequisitos y entregable; uniformar los `TODO`; completar IDs de estudiante y confirmar ejecución limpia del tutor. |
| 2 | `DS_Sprint2_class2_Funciones_en_Python` | **Bloqueado** | **T y luego E** | Corregir `NameError` de `calcular_promedio`, ejecutar de principio a fin, conservar el entregable ya existente y sincronizar la versión estudiante. |
| 3 | `DS_Sprint3_class1_Introduccion_a_Pandas` | **Bloqueado** | **T y E** | Resolver `data.xlsx`, eliminar el traceback y la ruta privada, añadir prerrequisitos/entregable y ejecutar en limpio. |
| 3 | `DS_Sprint3_class2_Preprocesamiento_de_Datos` | Media | Ambos | Añadir prerrequisitos, entregable y recursos de cierre; hacer explícitos los criterios de validación de la limpieza; completar IDs de estudiante. |
| 4 | `DS_Sprint4_class1_Manejo_Avanzado_de_Datos` | Media | Ambos | Añadir prerrequisitos, entregable y recursos; documentar controles posteriores a joins/agregaciones; completar IDs de estudiante. |
| 4 | `DS_Sprint4_class2_Graficos_de_Visualizacion` | Alta | Ambos | Corregir o limpiar `UserWarning`/`FutureWarning`, evitar rutas privadas en outputs, etiquetar todas las gráficas, añadir prerrequisitos/entregable/recursos. |
| 5 | `DS_Sprint5_class1_Introduccion_a_la_Estadistica` | Media | Ambos | Añadir prerrequisitos, entregable y recursos; explicitar supuestos e interpretación; normalizar IDs en tutor y estudiante. |
| 5 | `DS_Sprint5_class2_Ejercicios_de_Probabilidades` | Media | Ambos | Añadir prerrequisitos, entregable y recursos; declarar semilla en simulaciones; completar IDs de estudiante. |
| 5 | `DS_Sprint5_class3_Intro_a_Git_comandos_basicos` | Media | Ambos | Añadir prerrequisitos y entregable verificable; indicar evidencia a entregar (comandos, repo o captura); completar IDs de estudiante. |
| 6 | `DS_Sprint6_class1_Simulacion_de_Proyecto_Modulo_1` | Alta | Ambos | El tutor tiene código sin evidencia de ejecución; añadir prerrequisitos, entregable, recursos y criterios de aceptación del proyecto; normalizar IDs. |
| 7 | `DS_Sprint7_class1_Ambientes_Virtuales_y_Pull_Requests` | Media | Ambos | Aunque no requiere ejecución Python, debe declarar prerrequisitos, entregable y recursos; pedir evidencia verificable del entorno/PR; completar IDs de estudiante. |
| 7 | `DS_Sprint7_class2_Git_Avanzado` | Alta | Ambos | Conserva prerrequisitos, pero falta entregable; validar la celda de código no ejecutada, definir evidencia de ramas/rebase y normalizar IDs. |
| 7 | `DS_Sprint7_class3_Programacion_Orientada_a_Objetos` | Media | Ambos | Añadir prerrequisitos, entregable y recursos; incluir pruebas o criterios para las clases creadas; completar IDs. |
| 8 | `DS_Sprint8_class1_Web_Scraping` | Media | Ambos | Añadir prerrequisitos y entregable; documentar red, robots/términos, selectores frágiles y alternativa offline; normalizar IDs faltantes. |
| 8 | `DS_Sprint8_class2_SQL_Avanzado` | Media | Ambos | Añadir prerrequisitos, entregable y recursos; agregar checks de resultados y portabilidad del motor SQL; completar IDs. |
| 9 | `DS_Sprint9_class1_Modelos_de_Aprendizaje_Automatico` | Media | Ambos | Añadir prerrequisitos y entregable; explicitar semilla, partición de datos y baseline; completar IDs de estudiante. |
| 9 | `DS_Sprint9_class2_Primer_Modelo_y_KNN` | Alta | Ambos | Actualizar el uso de `boxplot(labels=...)` a la API vigente, eliminar warnings/rutas privadas, añadir prerrequisitos, entregable y recursos; normalizar IDs. |
| 10 | `DS_Sprint10_class1_Metricas_de_Evaluacion` | Alta | Ambos | Ejecutar y validar las cinco celdas del tutor; añadir prerrequisitos, entregable y recursos; justificar elección de métricas; normalizar IDs. |
| 10 | `DS_Sprint10_class2_Comparacion_y_Cross_Validation` | Alta | Ambos | Ejecutar el tutor; añadir prerrequisitos, entregable y recursos; documentar estrategia de CV, leakage y semilla; normalizar IDs. |
| 11 | `DS_Sprint11_class1_Datos_Desbalanceados` | Alta | Ambos | Ejecutar el tutor; añadir prerrequisitos y entregable; justificar remuestreo/métrica y evitar leakage; normalizar IDs. |
| 11 | `DS_Sprint11_class2_Feature_Engineering` | Alta | Ambos | Ejecutar el tutor; añadir prerrequisitos y entregable; distinguir transformaciones aprendidas solo con train; normalizar IDs. |
| 12 | `DS_Sprint12_class1_Bootstrapping_y_Pipelines` | Alta | Ambos | Ejecutar el tutor; añadir prerrequisitos y entregable; declarar semillas e interpretación del intervalo; normalizar IDs. |
| 12 | `DS_Sprint12_class2_Modularizacion` | Alta | Ambos | Conserva entregable; ejecutar tutor, añadir prerrequisitos y recursos, definir pruebas de funciones/módulos y normalizar IDs. |
| 13 | `DS_Sprint13_class1_Simulacro_Proyecto_ML` | Alta | Ambos | Ejecutar el tutor; añadir prerrequisitos, entregable y rúbrica del simulacro; validar dataset, métrica y reproducibilidad; normalizar IDs. |
| 14 | `DS_Sprint14_class1_Algebra_Lineal` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos y entregable; validar dimensiones/unidades y conectar cálculos con interpretación; normalizar IDs. |
| 14 | `DS_Sprint14_class1_Gradiente_Descendiente_y_Funcion_de_Costo` | Media | Ambos | Añadir prerrequisitos, entregable y recursos; verificar que outputs correspondan a ejecución limpia; aclarar la coexistencia de dos archivos `class1`; completar IDs de estudiante. |
| 14 | `DS_Sprint14_class2_Matrices_y_PCA` | Alta | Ambos | Ya declara requisitos; ejecutar tutor, añadir entregable y recursos, justificar escalado/PCA y varianza explicada; normalizar IDs. |
| 15 | `DS_Sprint15_class1_Introduccion_a_ANN` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos y entregable; declarar semilla, costo computacional y criterio de evaluación; normalizar IDs. |
| 15 | `DS_Sprint15_class2_Gradient_Descent_Avanzado` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos y entregable; validar convergencia, learning rate y semillas; normalizar IDs. |
| 16 | `DS_Sprint16_class1_Series_de_Tiempo_Descomposicion` | Alta | Ambos | Conserva requisitos; ejecutar tutor, añadir entregable y documentar frecuencia, orden temporal y ausencia de leakage; normalizar IDs. |
| 16 | `DS_Sprint16_class2_ARIMA_y_Prediccion` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos, entregable y recursos; documentar estacionariedad, horizonte y validación temporal; normalizar IDs. |
| 17 | `DS_Sprint17_class1_Introduccion_a_NLP` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos y entregable; documentar descargas de NLTK, idioma, semilla y evaluación; normalizar IDs. |
| 17 | `DS_Sprint17_class2_Embeddings_y_LLMs` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos y entregable; reemplazar el patrón `api_key="tu-api-key"` por variable de entorno/ejemplo seguro y ofrecer alternativa sin API; normalizar IDs. |
| 18 | `DS_Sprint18_class1_Redes_Neuronales_y_CNN` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos, entregable y recursos; declarar hardware/tiempo, semillas y alternativa liviana; normalizar IDs. |
| 18 | `DS_Sprint18_class2_Aprendizaje_No_Supervisado` | Alta | Ambos | Ejecutar tutor; añadir prerrequisitos y entregable; justificar escalado, número de clusters y métricas; normalizar IDs. |
| 19 | `DS_Sprint19_class1_Metodologias_de_Trabajo` | Alta | Ambos | Conserva entregable; ejecutar tutor, añadir prerrequisitos y recursos; definir evidencia del proceso y criterios de revisión; normalizar IDs. |
| 19 | `DS_Sprint19_class2_Proyecto_Final` | Alta | Ambos | Conserva entregable; ejecutar tutor, añadir prerrequisitos, rúbrica, fuente/diccionario de datos y checks del proyecto; normalizar IDs. |

## 7. Archivos que deben actualizarse primero

### Prioridad 0 — antes de cualquier publicación

1. `DS_Sprint2_class2_Funciones_en_Python.ipynb` y su versión estudiante.
2. `DS_Sprint3_class1_Introduccion_a_Pandas.ipynb` y su versión estudiante.

### Prioridad 1 — ejecutar y corregir

1. `DS_Sprint4_class2_Graficos_de_Visualizacion.ipynb` y su versión estudiante.
2. `DS_Sprint9_class2_Primer_Modelo_y_KNN.ipynb` y su versión estudiante.
3. Los 21 tutores marcados con prioridad **Alta** por no tener evidencia de ejecución, junto con la sincronización posterior de sus versiones estudiante.

### Prioridad 2 — estandarización pedagógica y técnica

El resto de los pares: agregar prerrequisitos, entregable, recursos cuando falten, criterios de logro e IDs de celda; luego ejecutar el tutor y volver a limpiar la versión estudiante.

## 8. Hallazgos sobre archivos auxiliares

Aunque no son notebooks, conviene actualizar también:

- `DS/Sprintplan/notebooks-index.md`: conserva estados “Missing” para notebooks que ya existen, no representa los 39 notebooks actuales y dice que las imágenes están en `../Images/`, mientras los notebooks usan correctamente `../../Images/` desde sus carpetas de sprint.
- `DS/DS_students/MANIFEST_students_versions.md`: debe regenerarse después de las correcciones para mantener conteos de celdas, `TODO` y espacios de trabajo.
- `DS/requirements.txt`: está fijado a versiones muy específicas; debe probarse como entorno completo y distinguir dependencias del curso de dependencias internas de Jupyter. Faltan paquetes importados por los notebooks: `imbalanced-learn` (Sprint 11), `tensorflow` (Sprints 15 y 18), `nltk` (Sprint 17) y `openai` (Sprint 17).

## 9. Criterio de aceptación para cerrar la actualización

Un par se considerará listo cuando:

- el tutor ejecute desde kernel limpio sin errores ni warnings no justificados;
- todos los recursos y datos necesarios estén disponibles;
- existan prerrequisitos, entregable y criterios de logro explícitos;
- la solución del tutor corresponda uno a uno con las consignas;
- la versión estudiante no revele soluciones y tenga outputs/contadores limpios;
- ambos notebooks tengan IDs de celda válidos y metadatos coherentes;
- imágenes, enlaces, APIs y exportaciones hayan sido verificados;
- el manifiesto refleje la versión final.
