---
inclusion: manual
---

# Sprint 4 – Notebook 5: Git Intermedio

## Archivo
`DS/Sprint 4/DS_Sprint4_class5_Git_Intermedio.ipynb`

## Sprint
**SPRINT 4 – Manipulación de Datos (Data Wrangling) Continuación**

## Webinar Fuente
`complements/TripleTen/Webinars/DA-DS/S4/Webinar 4.5 - Git Intermedio.md`

## Tema
Git Intermedio – Branching, Conflictos, Stash y Flujos de Trabajo

## Estado
✅ **CREADO**

## Tipo de Sesión
🟡 **Workshop práctico** – 6 hands-on exercises interspersed with theory

## Objetivos de Aprendizaje
- Dominar los **comandos Git intermedios**: `rebase`, `stash`, `cherry-pick`, `amend`
- Aplicar una **estrategia de branching** (GitFlow) para proyectos DS
- Resolver **conflictos de merge** de forma sistemática
- Configurar **aliases de Git** para productividad (incluyendo `git lg`)
- Gestionar **múltiples remotos** y colaborar con forks y pull requests

## Agenda (2 hours)
| Bloque | Actividad | Duración |
|---|---|---|
| 1 | Repaso + configuración y aliases | 15 min |
| 2 | Branching strategies: GitFlow | 20 min |
| 3 | Conflictos: merge vs rebase | 20 min |
| 4 | Stash y amend | 15 min |
| 5 | Forks y pull requests | 10 min |
| 6 | Ejercicios prácticos (6 ejercicios) | 35 min |
| 7 | Cierre y Kahoot | 5 min |

## Resumen de Secciones y Contenido (with exercises)
1. **Configuración y aliases** – `~/.gitconfig`; `git config --global user.name/email`; aliases: `git lg` (historial visual con ramas), `git co`, `git br`, `git st`, `git cm`
   - **Ejercicio 1**: configurar usuario, crear aliases, repo con 3 commits, usar `git lg`
2. **GitFlow** – diagrama main/develop/feature/release/hotfix; comandos `git flow init/feature/release/hotfix`
   - **Ejercicio 2**: simular desarrollo con GitFlow: feature análisis, feature visualización, release v1.0
3. **Conflictos** – cuándo ocurren; cómo se ven (`<<<<<<< HEAD`); merge vs rebase tabla; `--abort`
   - **Ejercicio 3**: crear conflicto, resolverlo; probar merge y rebase
4. **Stash y amend** – `git stash`, `stash list`, `stash pop`, `stash push -m`; `git commit --amend`
   - **Ejercicio 4**: stash WIP, cambiar rama, recuperar; amend para corregir mensaje
5. **Forks y PRs** – flujo: fork → clone → `remote add upstream` → rama → push → PR; mantener fork actualizado
   - **Ejercicio 5**: fork del repo del compañero, mejora, PR, review
6. **Ejercicio 6** – proyecto completo con GitFlow: 2 features, release v1.0, hotfix, `git lg` final

## Librerías Clave / Tools
`git`, `git-flow`, `github.com`

---
