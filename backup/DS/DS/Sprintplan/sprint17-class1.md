---
inclusion: manual
---

# Sprint 17 – Notebook 1: Aprendizaje Automático para Textos (NLP y LLM)

## Archivo (to be created)
`DS/Sprint 17/DS_Sprint17_class1.ipynb`

## Sprint
**SPRINT 17 – Aprendizaje Automático para Textos**

## Tema
Modelos de Lenguaje: NLP clásico e introducción a LLMs

## Tipo de Sesión
🔴 **Enfoque en proyecto** – combines theory with a project-oriented activity

## Objetivos de Aprendizaje
- Comprender el **pipeline de NLP**: tokenización, limpieza, vectorización, modelado
- Aplicar técnicas clásicas de NLP: **Bag of Words, TF-IDF**
- Entrenar un **clasificador de texto** (análisis de sentimientos, spam detection)
- Comprender intuitivamente qué son los **embeddings** y los **modelos de lenguaje**
- Tener una visión general de los **LLMs** (GPT, BERT) y cómo se usan en DS

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | Pipeline de NLP: preprocesamiento de texto | 20 mins |
| 3 | Vectorización: Bag of Words y TF-IDF | 20 mins |
| 4 | Clasificación de texto con sklearn | 20 mins |
| 5 | Embeddings y LLMs: intuición | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 20 mins |
| 7 | Tips y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo puede una máquina entender el lenguaje humano?
2. **Preprocesamiento de texto** – tokenización, lowercasing, stopwords, stemming/lemmatization; `nltk`, `re`; pipeline de limpieza
3. **Bag of Words** – representación como vector de frecuencias; `CountVectorizer`; limitaciones (no captura orden ni semántica)
4. **TF-IDF** – term frequency × inverse document frequency; `TfidfVectorizer`; por qué es mejor que BoW para clasificación
5. **Clasificación de texto** – `LogisticRegression` + TF-IDF pipeline; análisis de sentimientos (IMDB/Yelp reviews); `classification_report()`
6. **Embeddings** – word2vec intuición: "king - man + woman = queen"; representación densa vs sparse; `gensim` básico
7. **LLMs** – qué son BERT y GPT; transformers en una oración; cómo usar modelos pre-entrenados con `transformers` (HuggingFace); casos de uso en DS
8. **Actividad práctica – Breakout Rooms** – students build a text classifier for a provided dataset; spinner to pick presenter
9. **Tips y buenas prácticas** – clean text before vectorizing, use pre-trained embeddings when possible, LLMs for generation not classification
10. **Cierre y Kahoot**

## Imágenes Utilizadas
None documented yet

## Librerías Clave
`nltk`, `sklearn` (CountVectorizer, TfidfVectorizer, LogisticRegression), `re`, `pandas`, `gensim` (optional), `transformers` (optional demo)

## Notas de Estilo
- "King - man + woman = queen" analogy for embeddings is universally engaging
- Keep LLM section conceptual — focus on when to use them, not how to build them
- Connects to Sprint 18 (vision) — both use deep learning representations

---
