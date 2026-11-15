---
inclusion: manual
---

# Sprint 16 – Notebook 2: Modelos ARIMA y Predicción

## Archivo
`DS/Sprint 16/DS_Sprint16_class2_Modelos_ARIMA_SARIMA_y_Prediccion_Temporal.ipynb`

## Sprint
**SPRINT 16 – Series Temporales**

## Tema
Modelos ARIMA, SARIMA y Predicción Temporal

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/TripleTen/Webinars/DS/S13/Webinar DS 13.2 - Algunas métricas y métodos básicos para medir y hacer predicción con series de tiempo.md`

## Objetivos de Aprendizaje
- Comprender la estructura del modelo **ARIMA** (p, d, q)
- Usar **auto_arima** para selección automática de parámetros
- Aplicar **SARIMA** para series con estacionalidad
- Evaluar predicciones con **RMSE, MAE y MAPE**
- Realizar **split temporal** correcto (no aleatorio)

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
ARIMA: estructura y parámetros | 25 min |
auto_arima y selección de modelo | 20 min |
SARIMA para series estacionales | 15 min |
Evaluación y split temporal | 15 min |
Breakout Rooms | 20 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo elegir el modelo correcto para predecir una serie de tiempo?
2. **ARIMA** – AR (autoregressive), I (differencing), MA (moving average); ACF/PACF guían p,q
3. **auto_arima** – pmdarima; búsqueda automática; AIC como criterio
4. **SARIMA** – Extensión estacional (P,D,Q,m); SARIMAX
5. **Evaluación** – Split temporal (NUNCA aleatorio); RMSE, MAE, MAPE
6. **Breakout** – Fit ARIMA a AirPassengers y evaluar predicción

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `sklearn`
