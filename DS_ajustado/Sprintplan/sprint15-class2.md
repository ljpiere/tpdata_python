---
inclusion: manual
---

# Sprint 15 – Notebook 2: Gradient Descent Avanzado y Optimización

## Archivo
`DS/Sprint 15/DS_Sprint15_class2_Gradient_Descent_Avanzado_Learning_Rate_Momentum_y_Adam.ipynb`

## Sprint
**SPRINT 15 – Métodos Numéricos**

## Tema
Gradient Descent Avanzado: Learning Rate, Momentum y Adam

## Estado
🔲 **POR CREAR**

## Fuentes
- `complements/ML/Gradient_descent.ipynb`
- `complements/TripleTen/Webinars/DS/S12/Webinar DS 12.2 - Gradient Descent y optimización.md`

## Objetivos de Aprendizaje
- Comprender el efecto del **learning rate** en la convergencia
- Aplicar **momentum** y **Adam** como optimizadores avanzados
- Diferenciar entre **SGD, mini-batch y batch** gradient descent
- Entender por qué el **feature scaling** es crucial para GD
- Visualizar la convergencia con diferentes configuraciones

## Agenda (2 horas)
| Tema | Duración |
|---|---|
Introducción + Pregunta guía | 10 min |
Learning rate: demasiado grande vs pequeño | 20 min |
SGD vs Mini-batch vs Batch | 20 min |
Momentum y Adam | 25 min |
Feature scaling para convergencia | 15 min |
Breakout Rooms | 15 min |
Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo hacer que un modelo aprenda más rápido sin perder precisión?
2. **Learning rate** – Muy grande = diverge, muy pequeño = lento; learning rate scheduling
3. **SGD vs Batch** – Trade-off velocidad vs estabilidad; mini-batch como compromiso
4. **Momentum y Adam** – Intuición física (bola rodando); Adam combina momentum + adaptive LR
5. **Feature scaling** – Sin escalar: GD zigzaguea; con escalar: converge directo
6. **Breakout** – Implementar GD con diferentes LR y optimizadores, comparar convergencia

## Librerías Clave
`pandas`, `numpy`, `matplotlib`, `sklearn`
