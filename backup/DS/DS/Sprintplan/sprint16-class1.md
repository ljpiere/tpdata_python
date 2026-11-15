---
inclusion: manual
---

# Sprint 16 – Notebook 1: Análisis por Series de Tiempo

## Archivo (to be created)
`DS/Sprint 16/DS_Sprint16_class1.ipynb`

## Sprint
**SPRINT 16 – Series Temporales**

## Tema
Análisis por Series de Tiempo – Descomposición de Señal

## Objetivos de Aprendizaje
- Comprender la estructura de una **serie de tiempo**: tendencia, estacionalidad, residuos
- Aplicar la **descomposición de señal** para separar componentes
- Detectar **estacionariedad** con el test de Augmented Dickey-Fuller
- Calcular e interpretar la **autocorrelación** (ACF y PACF)
- Construir predicciones básicas con **promedios móviles** y **naive forecasting**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Estructura de una serie de tiempo | 20 mins |
| 3 | Descomposición de señal | 20 mins |
| 4 | Estacionariedad y test ADF | 20 mins |
| 5 | ACF, PACF y autocorrelación | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 20 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo predecir el futuro usando patrones del pasado?
2. **Estructura de una serie de tiempo** – índice temporal, frecuencia, formato de fechas; `pd.to_datetime()`, `resample()`; visualización básica
3. **Componentes** – tendencia (trend), estacionalidad (seasonality), residuos (noise); `seasonal_decompose()`; visualización de componentes
4. **Promedios móviles** – `rolling().mean()`; ventana de suavizado; naive forecasting (última observación, media estacional)
5. **Estacionariedad** – qué es y por qué importa para ARIMA; Augmented Dickey-Fuller test (`adfuller()`); diferenciación para hacer estacionaria
6. **ACF y PACF** – qué miden; `plot_acf()`, `plot_pacf()`; cómo usarlos para elegir parámetros ARIMA
7. **Actividad práctica – Breakout Rooms** – students decompose and analyze the AirPassengers dataset; spinner to pick presenter
8. **Tips y buenas prácticas** – always visualize first, check stationarity before modeling, use AIC for model selection
9. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `statsmodels` (seasonal_decompose, adfuller, plot_acf, plot_pacf)

## Notas de Estilo
- AirPassengers dataset as the main example (classic, clear seasonality, well-known)
- Connects to Sprint 5 (statistics) and Sprint 11 (model evaluation)
- Visual decomposition plot is the "aha moment" of this session

---
