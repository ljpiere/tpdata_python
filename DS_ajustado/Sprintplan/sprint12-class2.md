---
inclusion: manual
---

# Sprint 12 – Notebook 2: Modularización de un Proyecto de DS

## Archivo
`DS/Sprint 12/DS_Sprint12_class2_Modularizacion_y_Estructura_Profesional_de_Proyectos.ipynb`

## Sprint
**SPRINT 12 – ML en Negocios**

## Tema
Modularización y Estructura Profesional de Proyectos

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/TripleTen/Webinars/DS/S8/Webinar DS 8.2 - Modularización de un proyecto.md`
- `complements/TripleTen/Webinars/DS/S8_DS_W2_project/`

## Objetivos de Aprendizaje
- Organizar un proyecto de DS con **estructura profesional** de carpetas
- Separar código en **módulos reutilizables** (preprocessing, models, execution)
- Crear archivos de **configuración y parámetros** centralizados
- Usar **joblib** para guardar y cargar modelos entrenados
- Aplicar el flujo **input → preprocessing → model → output** en producción

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
Estructura de carpetas profesional | 20 min |
Modularización: separar responsabilidades | 25 min |
Configuración y parámetros | 15 min |
Guardar y cargar modelos (joblib) | 15 min |
Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo pasar de un notebook exploratorio a un proyecto de producción?
2. **Estructura** – input/, intermediate/, models/, output/, preprocessing/, pipeline/
3. **Módulos** – Cada .py tiene una responsabilidad; imports entre módulos
4. **Parámetros** – params.py centralizado; no hardcodear valores
5. **Persistencia** – joblib.dump/load; versionado de modelos
6. **Ejecución** – Script principal que orquesta todo el flujo

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `sklearn`
