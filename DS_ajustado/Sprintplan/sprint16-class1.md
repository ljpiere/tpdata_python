---
inclusion: manual
---

# Sprint 16 – Notebook 1: Series de Tiempo – Descomposición

## Archivo
`DS/Sprint 16/DS_Sprint16_class1_Analisis_por_Series_de_Tiempo_Descomposicion_de_Señal.ipynb`

## Sprint
**SPRINT 16 – Series Temporales**

## Tema
Análisis por Series de Tiempo: Descomposición de Señal

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/TripleTen/Webinars/DS/S13/Webinar DS 13.1 - Time Series Analysis - Descomposición de señal.md`
- `complements/TripleTen/Webinars/DS/S13/DS_W13_1_Time_Series_Analysis.py`
- `complements/TripleTen/Webinars/DS/S13/ACF vs PACF.md`

## Objetivos de Aprendizaje
- Comprender la estructura de una **serie de tiempo**: tendencia, estacionalidad, residuos
- Aplicar **descomposición de señal** (aditiva y multiplicativa)
- Detectar **estacionariedad** con el test Augmented Dickey-Fuller
- Calcular e interpretar **ACF y PACF** para selección de modelos
- Aplicar **promedios móviles** y naive forecasting como baselines

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
Estructura de una serie de tiempo | 20 min |
Descomposición de señal | 20 min |
Estacionariedad y test ADF | 20 min |
ACF y PACF | 15 min |
Breakout Rooms | 20 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo predecir el futuro usando patrones del pasado?
2. **Estructura** – Índice temporal, frecuencia, pd.to_datetime, resample
3. **Descomposición** – seasonal_decompose(); tendencia, estacionalidad, residuos
4. **Estacionariedad** – Qué es, por qué importa; ADF test; diferenciación
5. **ACF/PACF** – Qué miden; plot_acf/pacf; guían elección de p,q para ARIMA
6. **Breakout** – Descomponer y analizar AirPassengers dataset

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `sklearn`
