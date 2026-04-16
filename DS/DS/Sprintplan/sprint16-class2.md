---
inclusion: manual
---

# Sprint 16 – Notebook 2: Modelos de Inferencia por Dependencia Temporal

## Archivo (to be created)
`DS/Sprint 16/DS_Sprint16_class2.ipynb`

## Sprint
**SPRINT 16 – Series Temporales**

## Tema
Modelos de Inferencia por Dependencia Temporal (ARIMA y variantes)

## Objetivos de Aprendizaje
- Comprender la estructura del modelo **ARIMA** (p, d, q) y sus componentes
- Usar **auto_arima** para selección automática de parámetros
- Evaluar predicciones con **RMSE, MAE y MAPE**
- Aplicar **SARIMA** para series con estacionalidad
- Comparar modelos y seleccionar el mejor usando **AIC/BIC**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | ARIMA: estructura y parámetros | 25 mins |
| 3 | auto_arima y selección de modelo | 20 mins |
| 4 | SARIMA para series estacionales | 15 mins |
| 5 | Evaluación y comparación de modelos | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 20 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo elegir el modelo correcto para predecir una serie de tiempo?
2. **ARIMA** – AR (autoregressive), I (integrated/differencing), MA (moving average); parámetros p, d, q; cómo ACF/PACF guían la elección
3. **Implementación** – `statsmodels.tsa.arima.model.ARIMA`; `model.fit()`, `model.forecast()`; visualización de predicciones vs real
4. **auto_arima** – `pmdarima.auto_arima()`; búsqueda automática de parámetros; AIC como criterio de selección
5. **SARIMA** – extensión estacional (P, D, Q, m); cuándo usar SARIMA vs ARIMA; `SARIMAX`
6. **Métricas de evaluación** – RMSE, MAE, MAPE; `sklearn.metrics`; train/test split temporal (no random!)
7. **Comparación de modelos** – naive vs ARIMA vs SARIMA; AIC/BIC; residual analysis
8. **Actividad práctica – Breakout Rooms** – students fit and evaluate ARIMA on a provided time series; spinner to pick presenter
9. **Tips y buenas prácticas** – never use random split for time series, check residuals, report prediction intervals
10. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`statsmodels`, `pmdarima`, `pandas`, `numpy`, `matplotlib`, `sklearn`

## Notas de Estilo
- Connects directly to Sprint 16 class1 (decomposition and stationarity)
- Emphasize temporal train/test split — a common mistake
- AirPassengers dataset continues from class1

---
