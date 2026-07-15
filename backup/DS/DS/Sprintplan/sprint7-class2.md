---
inclusion: manual
---

# Sprint 7 – Notebook 2: Programación Orientada a Objetos (OOP)

## Archivo (to be created)
`DS/Sprint 7/DS_Sprint7_class2.ipynb`

## Sprint
**SPRINT 7 – Herramientas de Desarrollo de Software**

## Tema
Programación Orientada a Objetos (POO / OOP)

## Objetivos de Aprendizaje
- Comprender qué es la **Programación Orientada a Objetos** y por qué es útil en DS
- Definir **clases**, crear **instancias** y usar **atributos y métodos**
- Aplicar el **constructor `__init__`** y métodos mágicos (`__repr__`, `__str__`)
- Diferenciar **atributos de instancia vs atributos de clase**
- Comprender los 4 principios de OOP: **Encapsulación, Abstracción, Herencia, Polimorfismo**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Clases, objetos e instancias | 20 mins |
| 3 | Constructor __init__ y atributos | 20 mins |
| 4 | Métodos, métodos de clase y estáticos | 20 mins |
| 5 | Herencia y principios OOP | 20 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo organizar código complejo para que sea reutilizable y mantenible?
2. **Clases y objetos** – "casi todo en Python es un objeto"; analogía: clase = plano de construcción, instancia = casa construida; `class`, `pass`
3. **Constructor y atributos** – `__init__`, `self`, atributos de instancia vs clase; `__repr__` para representación legible
4. **Métodos** – métodos de instancia, `@classmethod`, `@staticmethod`; cuándo usar cada uno; `cls`
5. **Herencia** – `super()`, sobreescritura de métodos; ejemplo con jerarquía de modelos DS
6. **Principios OOP** – Encapsulación (`@property`, getters/setters), Abstracción, Herencia, Polimorfismo; ejemplos en pandas/sklearn
7. **Estructura de proyectos** – cookiecutter, módulos e imports relativos; `__name__ == "__main__"`
8. **Actividad práctica – Breakout Rooms** – students build a simple `DataPipeline` class; spinner to pick presenter
9. **Tips y buenas prácticas** – single responsibility, meaningful names, docstrings, `assert` for testing
10. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
Pure Python + `pandas` (as OOP example)

## Notas de Estilo
- "Blueprint vs house" analogy for class vs instance
- Show how pandas DataFrame is itself a class — students already use OOP without knowing it
- Breakout Room: build a `DataPipeline` class that wraps load/clean/describe steps

---
