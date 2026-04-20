---
inclusion: manual
---

# Sprint 8 – Notebook 2: Web Scraping

## Archivo (to be created)
`DS/Sprint 8/DS_Sprint8_class2.ipynb`

## Sprint
**SPRINT 8 – Recopilación y Almacenamiento de Datos**

## Tema
Web Scraping

## Objetivos de Aprendizaje
- Comprender cómo funciona la **estructura HTML** y cómo los datos están embebidos en páginas web
- Usar **BeautifulSoup** para extraer datos de páginas HTML estáticas
- Usar **Requests** para hacer peticiones HTTP y obtener contenido web
- Manejar **paginación** y extraer datos de múltiples páginas
- Almacenar datos scrapeados en un **DataFrame de pandas**

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Introducción + Pregunta guía | 10 mins |
| 2 | HTML básico: estructura y etiquetas relevantes | 15 mins |
| 3 | Requests: obtener páginas web | 15 mins |
| 4 | BeautifulSoup: parsear y extraer datos | 30 mins |
| 5 | Paginación y scraping de múltiples páginas | 15 mins |
| 6 | Actividad práctica – Breakout Rooms | 15 mins |
| 7 | Tips, ética y buenas prácticas | 5 mins |
| 8 | Cierre y Kahoot | 5 mins |

## Resumen de Secciones y Contenido
1. **Pregunta Guía** – ¿Cómo obtener datos cuando no existe una API ni un CSV?
2. **HTML básico** – `<html>`, `<head>`, `<body>`, `<div>`, `<table>`, `<a>`, `<span>`; inspeccionar elementos en el navegador (DevTools)
3. **Requests** – `requests.get()`, status codes, `response.text`, headers; qué es HTTP
4. **BeautifulSoup** – `BeautifulSoup(html, 'html.parser')`, `.find()`, `.find_all()`, `.select()` (CSS selectors), `.get_text()`, `.get('href')`
5. **Extracción de tablas** – `pd.read_html()` como atajo; cuándo usar BeautifulSoup vs `read_html()`
6. **Paginación** – loop over pages; URL patterns; `time.sleep()` para ser respetuoso
7. **Almacenamiento** – guardar en DataFrame, exportar a CSV
8. **Actividad práctica – Breakout Rooms** – students scrape a simple static website; spinner to pick presenter
9. **Ética y buenas prácticas** – `robots.txt`, rate limiting, no scraping datos privados, términos de servicio
10. **Cierre y Kahoot**

## Requerimientos
- `requests`, `beautifulsoup4` installed
- Internet connection
- Target website for practice (use a stable, scraping-friendly site like `books.toscrape.com`)

## Librerías Clave
`requests`, `beautifulsoup4`, `pandas`, `time`

## Notas de Estilo
- Use `books.toscrape.com` as the practice site — designed for scraping practice
- DevTools demo: show students how to inspect elements before writing code
- Emphasize ethics: always check `robots.txt`

---
