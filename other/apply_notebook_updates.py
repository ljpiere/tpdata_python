import json
import os

CONTENT_MAP = {
    "Sprint0_Webinar00_Intro.ipynb": {
        "cierre": """## Cierre de la sesión 0
**Kahoot de repaso (5 min)**
- Identificamos expectativas del curso y del rol de Data Analyst.
- Revisamos la logística y herramientas clave (Discord, plataforma, etc.).

**Reflexión:**
- ¿Qué te motiva más de iniciar este camino en Data Analytics?
- ¿Qué hábito de estudio te comprometes a mantener durante el bootcamp?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 1 - Introducción teórica a la profesión y herramientas.
- **Participación:** Preséntate en el canal de Discord si aún no lo has hecho.
- **Recordatorios:** Revisa el material preparatorio para el Sprint 1."""
    },
    "Sprint1_Webinar01_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Entendimos el rol del DA en diferentes organizaciones.
- Repasamos el flujo de trabajo: Pregunta -> Datos -> Análisis -> Acción.

**Reflexión:**
- ¿Cómo diferenciarías un rol de Data Analyst de un Data Scientist?
- ¿Por qué es importante entender el negocio antes de tocar los datos?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 1 - Práctica de limpieza básica en Sheets.
- **Participación:** Revisa los datasets de ejemplo en la carpeta de recursos.
- **Recordatorios:** La grabación estará disponible pronto."""
    },
    "Sprint1_Webinar02_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Practicamos normalización de fechas, textos y números en Sheets.
- Identificamos la importancia de la calidad de datos.

**Reflexión:**
- ¿Qué te ayudó más a entender los errores en los datos: verlos visualmente o usar fórmulas?
- ¿Por qué "limpiar" datos consume tanto tiempo en un proyecto real?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 2 - Formulación de preguntas de negocio.
- **Participación:** Intenta limpiar el dataset de práctica adicional por tu cuenta.
- **Recordatorios:** Sube tu ejercicio práctico si es requerido."""
    },
    "Sprint2_Webinar03_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Aprendimos a formular preguntas de negocio accionables.
- Diferenciamos métricas *Leading* vs *Lagging*.

**Reflexión:**
- ¿Por qué una pregunta vaga ("¿cómo vamos?") es peligrosa para un analista?
- ¿Qué ventaja tiene definir los KPIs antes de empezar a analizar?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 2 - Limpieza avanzada y KPIs en el proyecto Walmart.
- **Participación:** Comparte en Discord una pregunta de negocio que se te ocurra para tu trabajo actual.
- **Recordatorios:** Revisa las lecturas sobre KPIs sugeridas."""
    },
    "Sprint2_Webinar04_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Aplicamos limpieza y estandarización a datos de retail (Walmart).
- Preparamos el dataset para calcular KPIs clave.

**Reflexión:**
- ¿Qué desafío encontraste al manejar fechas o categorías mal escritas?
- ¿Cómo asegurarías que estos pasos de limpieza sean reproducibles?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 2 - PivotTables y Visualización inicial.
- **Participación:** Termina de normalizar las columnas restantes del ejercicio.
- **Recordatorios:** Agenda un 1:1 si tuviste problemas con las fórmulas de texto."""
    },
    "Sprint2_Webinar05_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Exploramos el poder de las Tablas Dinámicas (PivotTables) para resumir datos.
- Vimos cómo filtrar, ordenar y agrupar para encontrar insights rápidos.

**Reflexión:**
- ¿En qué situaciones preferirías una Tabla Dinámica sobre una fórmula manual?
- ¿Qué riesgo existe si interpretamos mal un promedio en una tabla resumen?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 2 - Warm-up y práctica intensiva del Proyecto Walmart.
- **Participación:** Experimenta creando 3 tablas dinámicas diferentes con el mismo dataset.
- **Recordatorios:** Practica los atajos de teclado para crear tablas dinámicas."""
    },
    "Sprint2_Webinar06_Práctico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Consolidamos la limpieza y análisis exploratorio del caso Walmart.
- Preparamos el terreno para visualizaciones más complejas.

**Reflexión:**
- ¿Qué patrón interesante descubriste en los datos de ventas durante la práctica?
- ¿Te sentiste más cómodo con la limpieza o con el análisis hoy?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 3 - Introducción a SQL y Bases de Datos.
- **Participación:** Asegúrate de tener acceso a la herramienta de SQL para la próxima semana.
- **Recordatorios:** Cierra tu Sprint 2 revisando los objetivos de aprendizaje."""
    },
    "Sprint3_Webinar07_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Introdujimos SQL y el modelo relacional.
- Identificamos Primary Keys (PK) y Foreign Keys (FK).

**Reflexión:**
- ¿Por qué las bases de datos relacionales son el estándar en la industria?
- ¿Cómo cambia tu mentalidad de "celdas" (Excel) a "tablas y filas" (SQL)?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 3 - Práctica de consultas básicas (SELECT, WHERE, ORDER BY).
- **Participación:** Instala o configura tu entorno SQL según las instrucciones.
- **Recordatorios:** Repasa los conceptos de diagrama ER (Entidad-Relación)."""
    },
    "Sprint3_Webinar08_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Ejecutamos nuestras primeras queries: SELECT, WHERE, ORDER BY.
- Empezamos a ver agregaciones simples.

**Reflexión:**
- ¿Cuál fue el error de sintaxis más común que cometiste hoy?
- ¿Por qué es importante el orden de ejecución de las cláusulas en SQL?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 3 - KPIs financieros con SQL (Agregaciones y JOINs).
- **Participación:** Resuelve los ejercicios extra de SQLZoo o plataforma similar.
- **Recordatorios:** Comparte tus dudas de sintaxis en el canal de #sql."""
    },
    "Sprint3_Webinar09_Teórico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Definimos KPIs financieros: Margen, ROI, Revenue.
- Tradujimos fórmulas de negocio a consultas SQL con GROUP BY.

**Reflexión:**
- ¿Cómo te aseguras de que tu query calcula lo que el negocio pidió?
- ¿Qué ventaja tiene calcular KPIs en SQL vs exportar a Excel y calcular allí?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 3 - Práctica intensiva de KPIs y validación de resultados.
- **Participación:** Intenta reconstruir una métrica financiera compleja por pasos.
- **Recordatorios:** Revisa la documentación de funciones de agregación."""
    },
    "Sprint3_Webinar10_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Practicamos JOINs para cruzar tablas de ventas y productos.
- Calculamos ROI por campaña/canal.

**Reflexión:**
- ¿Qué pasa si hacemos un JOIN incorrecto (duplicidad de datos)?
- ¿Cómo validaste que tus números fueran coherentes hoy?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 4 - Funnels y User Journey.
- **Participación:** Asiste al Sprint Focus para resolver dudas de SQL avanzado.
- **Recordatorios:** Guarda tus scripts de SQL para usarlos como plantilla."""
    },
    "Sprint4_Webinar11_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Entendimos el concepto de User Journey y Funnels de conversión.
- Preparamos CTEs para limpiar eventos antes de analizar.

**Reflexión:**
- ¿Por qué el análisis de funnels es crítico para productos digitales?
- ¿Qué ventaja tienen las CTEs (Common Table Expressions) para organizar tu código?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 4 - Práctica de construcción de Funnels en SQL.
- **Participación:** Visualiza un funnel de un producto que uses (ej. Netflix, Amazon).
- **Recordatorios:** Repasa la sintaxis de `WITH` (CTE)."""
    },
    "Sprint4_Webinar12_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Construimos un Funnel paso a paso usando SQL.
- Analizamos tiempos entre etapas y cuellos de botella.

**Reflexión:**
- ¿Dónde detectaste la mayor caída de usuarios en el ejercicio?
- ¿Qué hipótesis de negocio podrías plantear para mejorar esa conversión?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 4 - A/B Testing y Segmentación en funnels.
- **Participación:** Intenta añadir una etapa más al funnel por tu cuenta.
- **Recordatorios:** La grabación te servirá para repasar la lógica de las queries largas."""
    },
    "Sprint4_Webinar13_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Revisamos la teoría de A/B Testing aplicada a funnels.
- Aprendimos a segmentar usuarios para encontrar comportamientos heterogéneos.

**Reflexión:**
- ¿Por qué un promedio global puede ocultar la verdad sobre un segmento de usuarios?
- ¿Qué requisitos debe tener un A/B test para ser válido?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 4 - Práctica final de análisis de comportamiento.
- **Participación:** Lee sobre "Simpson's Paradox" en datos.
- **Recordatorios:** Prepara tus dudas para la última sesión del sprint."""
    },
    "Sprint4_Webinar14_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Aplicamos todo lo aprendido: Funnels + Segmentación + Comparación.
- Interpretamos resultados para dar recomendaciones de negocio.

**Reflexión:**
- ¿Qué recomendación darías al Product Manager basada en tu análisis de hoy?
- ¿Cómo comunicas un resultado "negativo" (algo que no funcionó) de forma constructiva?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 5 - Introducción a Python y Pandas.
- **Participación:** ¡Felicidades por terminar el módulo de SQL!
- **Recordatorios:** Instala Anaconda/Python según la guía de setup."""
    },
    "Sprint5_Webinar15_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Iniciamos nuestro viaje en Python y Pandas.
- Cargamos nuestro primer DataFrame y exploramos sus dimensiones.

**Reflexión:**
- ¿Qué diferencia sientes entre manipular datos en SQL vs Python?
- ¿Por qué Pandas es tan popular para Data Analytics?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 5 - Práctica de manipulación básica de DataFrames.
- **Participación:** Ejecuta tus primeros comandos en un notebook local.
- **Recordatorios:** Familiarízate con la interfaz de Jupyter."""
    },
    "Sprint5_Webinar16_Práctico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Practicamos selección, filtrado y creación de columnas en Pandas.
- Resolvimos ejercicios básicos de exploración de datos.

**Reflexión:**
- ¿Qué comando te pareció más útil hoy (.loc, .iloc, filtrado condicional)?
- ¿Cómo te ayuda Jupyter a documentar tu proceso de análisis?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 5 - Caso de Licores: Limpieza y análisis real.
- **Participación:** Completa los ejercicios "TODO" que quedaron pendientes.
- **Recordatorios:** Revisa la documentación de Pandas si te atascas."""
    },
    "Sprint5_Webinar17_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Abordamos el caso de Licores Latinoamericanos.
- Planteamos la estrategia de limpieza y análisis exploratorio (EDA).

**Reflexión:**
- ¿Qué anomalía destacarías de este dataset a primera vista?
- ¿Por qué es importante revisar los tipos de datos (dtypes) al cargar un archivo?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 5 - Práctica avanzada: Limpieza y Outliers.
- **Participación:** Piensa en cómo manejarías los valores nulos en este caso.
- **Recordatorios:** Descarga el dataset actualizado si hubo cambios."""
    },
    "Sprint5_Webinar18_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Realizamos limpieza avanzada: outliers, strings y nulos.
- Dejamos el dataset listo para responder preguntas de negocio complejas.

**Reflexión:**
- ¿Qué criterio usamos para decidir qué hacer con los outliers?
- ¿Qué aprendiste hoy sobre la manipulación de textos (strings) en Pandas?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 7 - Estadística descriptiva y Git.
- **Participación:** Termina de limpiar el dataset y guárdalo como CSV.
- **Recordatorios:** Revisa el concepto de IQR (Rango Intercuartil)."""
    },
    "Sprint7_Webinar19_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Introdujimos conceptos estadísticos básicos para DA.
- Hablamos de la importancia del control de versiones (Git/GitHub).

**Reflexión:**
- ¿Por qué un analista debe saber usar Git y no solo guardar archivos "v1_final_final"?
- ¿Qué nos dice la distribución de una variable sobre el negocio?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 7 - Práctica de Git y Análisis Estadístico.
- **Participación:** Crea tu cuenta de GitHub si no la tienes.
- **Recordatorios:** Configura tu usuario y email en Git localmente."""
    },
    "Sprint7_Webinar20_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Practicamos el flujo básico de Git: init, add, commit, push.
- Analizamos distribuciones de datos usando Python.

**Reflexión:**
- ¿Qué ventaja tiene convertir tu trabajo en un proyecto usando funciones y Git en lugar de código suelto?
- ¿Qué te reveló el histograma sobre tus datos hoy?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 7 - Segmentación y Outliers profundos.
- **Participación:** Sube tu primer repositorio de práctica a GitHub.
- **Recordatorios:** No temas a la terminal; es tu amiga."""
    },
    "Sprint7_Webinar21_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Profundizamos en la detección de anomalías y segmentación.
- Vimos cómo usar reglas estadísticas para flaggear transacciones sospechosas.

**Reflexión:**
- ¿Es lo mismo un outlier que un error de datos? ¿Por qué?
- ¿Cómo aporta valor al negocio segmentar a los clientes?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 7 - Proyecto final del sprint: Clínica Agendada.
- **Participación:** Revisa los conceptos de media, mediana y desviación estándar.
- **Recordatorios:** Prepara tu entorno para el proyecto integrado."""
    },
    "Sprint7_Webinar22_Practico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Trabajamos en el proyecto "Clínica Agendada" de principio a fin.
- Generamos datos, limpiamos y detectamos segmentos.

**Reflexión:**
- ¿Qué fue lo más retador de integrar todas las habilidades (Python + Stats + Git)?
- ¿Cómo explicarías tus hallazgos a un director médico no técnico?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Sprint 8 - Correlaciones y Relaciones entre variables.
- **Participación:** Completa el README de tu repositorio en GitHub.
- **Recordatorios:** Entrega el link de tu repo en la plataforma."""
    },
    "Sprint8_Webinar23_Teorico.ipynb": {
        "cierre": """## Cierre
**Kahoot de repaso (5 min)**
- Exploramos correlaciones lineales y relaciones entre variables.
- Usamos Scatterplots para validar hipótesis visualmente.

**Reflexión:**
- ¿Por qué "Correlación no implica Causalidad" es la regla de oro?
- ¿Qué gráficos te ayudaron más a entender el comportamiento de los datos hoy?

**Q&A y próximos pasos.**""",
        "pasos": """## Siguientes Pasos
- **Próxima sesión:** Continuación del análisis exploratorio avanzado.
- **Participación:** Busca ejemplos de "correlaciones espurias" en internet.
- **Recordatorios:** Sigue practicando con datasets nuevos."""
    }
}

DEFAULT_CIERRE = """## Cierre
**Kahoot de repaso (5 min)**
- Validar aprendizajes clave de la sesión.
- Q&A y próximos pasos.

**Reflexión:**
- ¿Qué fue lo más importante que aprendiste hoy?
- ¿Cómo aplicarías esto en un proyecto real?
"""

DEFAULT_PASOS = """## Siguientes Pasos
- **Próxima sesión:** Revisar calendario del curso.
- **Participación:** Asistir a Co-Learning y Sprint Focus, y usar los canales de Discord.
- **Recordatorios:** La grabación y recursos se comparten al finalizar; agenda un 1:1 si necesitas apoyo."""

DIRECTORY = r"c:\Users\jeanp\Downloads\Proyectos\tpdata_python\DA"

def update_notebooks():
    for filename, content in CONTENT_MAP.items():
        filepath = os.path.join(DIRECTORY, filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found)")
            continue
            
        print(f"Processing {filename}...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                nb = json.load(f)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        cierre_md = content.get("cierre", DEFAULT_CIERRE)
        pasos_md = content.get("pasos", DEFAULT_PASOS)
        
        # Helper to create a markdown cell
        def create_md_cell(source_text):
            return {
                "cell_type": "markdown",
                "metadata": {},
                "source": [line + "\n" for line in source_text.split("\n")]
            }

        new_cells = nb.get("cells", [])
        
        # Remove existing Cierre/Pasos if they are placeholders or we want to overwrite
        # Strategy: Filter out cells that explicitly start with "## Cierre" or "## Siguientes Pasos"
        # to avoid duplication, then append the new ones.
        
        filtered_cells = []
        for cell in new_cells:
            if cell.get("cell_type") == "markdown":
                src = "".join(cell.get("source", "")).strip()
                if src.startswith("## Cierre") or src.startswith("# Cierre"):
                    continue
                if src.startswith("## Siguientes Pasos") or src.startswith("# Siguientes Pasos"):
                    continue
            filtered_cells.append(cell)
            
        # Append new cells
        filtered_cells.append(create_md_cell(cierre_md))
        filtered_cells.append(create_md_cell(pasos_md))
        
        nb["cells"] = filtered_cells
        
        # Save
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False) # indent=1 to match common ipynb format
            print(f"Updated {filename}")
        except Exception as e:
            print(f"Error writing {filename}: {e}")

if __name__ == "__main__":
    update_notebooks()
