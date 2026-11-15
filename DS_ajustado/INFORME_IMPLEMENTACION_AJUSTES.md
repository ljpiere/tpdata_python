# Informe de implementación — DS ajustado

Fecha: 2026-08-19

## Alcance completado

- 39 notebooks de tutor y 39 notebooks de estudiante copiados y reestructurados.
- Contenido temático original conservado; la nueva capa pedagógica sigue la estructura vigente de `DA`.
- Hallazgo crítico de Funciones corregido: `calcular_promedio` se define y prueba antes de usarse.
- Hallazgo crítico de Pandas corregido: el ejemplo de Excel se genera en memoria y ya no depende de `data.xlsx`.
- Ejemplo de API actualizado para leer `OPENAI_API_KEY` del entorno, con alternativa local documentada.
- Uso obsoleto de `labels=` en `boxplot` actualizado a `tick_labels=` y ejemplos de Seaborn ajustados para evitar el warning de `palette` sin `hue`.
- Outputs de error, warnings auditados y rutas privadas eliminados de tutores; estudiantes completamente limpios.
- Dependencias de curso separadas de las dependencias internas de Jupyter e imports faltantes declarados.
- Índice y manifiesto regenerados desde los archivos finales.

## Verificación incluida

- Validez JSON y `nbformat` 4.5.
- ID válido y único en cada celda.
- Correspondencia uno a uno entre tutor y estudiante.
- Apertura, prerrequisitos, entregable, criterios, cierre y ayuda presentes en cada notebook.
- Cero outputs, errores o contadores en las versiones estudiante.
- Ausencia de `data.xlsx`, credenciales de ejemplo inseguras y API obsoleta `labels=`.

## Verificación operativa recomendada antes de publicación

La auditoría original fue estática y la generación también evita ejecutar operaciones externas. Antes de impartir cada sesión se debe instalar `requirements-jupyter.txt` y ejecutar el notebook tutor con **Restart Kernel and Run All** en el entorno docente. Los notebooks con red, APIs, NLTK o TensorFlow incluyen controles/contingencias en su estructura, pero la disponibilidad externa debe comprobarse el día de clase.
