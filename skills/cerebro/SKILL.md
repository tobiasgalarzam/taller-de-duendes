---
name: cerebro
description: Lee y escribe notas en el segundo cerebro de Tobias (bóveda de Obsidian). Usar cuando pida guardar, anotar, recordar o documentar algo "en el cerebro" / "en Obsidian" / "en mis notas", cuando pregunte qué tiene anotado sobre un tema, o cuando necesites contexto de sus materias de la facultad o de sus proyectos.
---

# Segundo cerebro (Obsidian)

Bóveda: `C:\Users\Tobias\source\taller-de-duendes\cerebro`
Tablero: `Inicio.md` (índice de todo; actualizarlo al crear una materia o proyecto nuevo).

## Carpetas

- `00-Inbox/` — destino por defecto de notas nuevas si no está claro dónde van.
- `10-Proyectos/<Proyecto>/<Proyecto>.md` — una carpeta por proyecto con su nota principal; notas extra del proyecto van en la misma carpeta.
  - Ámbito por tag: `profesional` (GeoAlarm, CarefulTeam), `personal` (ej. juegos de Roblox) o `facultad` (Optimización multinivel).
- `20-Areas/Facultad/` — `Facultad.md` (índice) y una carpeta por carrera:
  - `Sistemas/Ingeniería en Sistemas.md` + `Sistemas/Materias/<Materia>.md` (UTN, plan 2023).
  - `Nuclear/Ingeniería Nuclear.md` (arranca 2027; materias en `Nuclear/Materias/` cuando empiece).
- `20-Areas/Profesional/Perfil profesional.md` — CV, portafolio, certificados, stack y experiencia (enlaza a `source\serio`).
- `10-Proyectos/Búsqueda laboral/` — búsqueda de trabajo: la nota principal `Búsqueda laboral.md` y las notas de puestos que guarde la skill `chamba` (enlazarlas desde la nota principal).
- `20-Areas/Personal/` — responsabilidades personales que no son proyectos.
- `30-Recursos/` — conceptos y referencias sueltas (ej. "GRASP", "Autovalores").
- `40-Archivo/` — inactivo (materias aprobadas, proyectos terminados).
- `Plantillas/` — `Materia.md`, `Proyecto.md`, `Apunte.md`, `Nota.md`.

## Dónde está el material original

Los archivos NO se copian a la bóveda; las notas los enlazan.

- Facultad: `C:\Users\Tobias\source\utn\` (`sistemas\<materia>\`, `nuclear\`).
- Proyectos: `C:\Users\Tobias\source\proyectos\`. Prácticas chicas de C#: `C:\Users\Tobias\source\repos\`.
- Profesional (CV, portafolio, certificados): `C:\Users\Tobias\source\serio\`.
- Cada nota de materia/proyecto tiene `carpeta:` en el frontmatter con la ruta original.
- `C:\Users\Tobias\source\taller-de-duendes` NO entra en el cerebro hasta que Tobias lo pida.

## Buscar

Antes de crear una nota, buscar si ya existe algo del tema (grep por palabras clave en la bóveda) y, si existe, ampliar esa nota en vez de duplicar. Para un tema de una materia, mirar también la nota de la materia y su carpeta de material.

## Escribir una nota

- Nombre de archivo: título legible, ej. `Junctions en Windows.md`. Los nombres de nota deben ser únicos en toda la bóveda (los `[[enlaces]]` van por nombre).
- Frontmatter mínimo:
  ```
  ---
  tags: [tema1, tema2]
  fecha: AAAA-MM-DD
  fuente: <proyecto, URL o "conversación con Claude">
  ---
  ```
- Materias y proyectos: usar la plantilla correspondiente (`Plantillas/Materia.md`, `Plantillas/Proyecto.md`) reemplazando `{{title}}` y `{{date:...}}` a mano.
- Apunte de un tema de una materia: plantilla `Apunte.md`, con `materia: <nombre>` y enlace `[[<Materia>]]`; agregar el enlace al apunte en la sección "Mis apuntes" de la materia.
- Novedades de un proyecto (decisión, avance): agregar una línea en "Bitácora" o "Decisiones y aprendizajes" de su nota principal.
- Enlaces a archivos fuera de la bóveda: `[texto](file:///C:/Users/Tobias/...)` con espacios como `%20`.
- Una idea por nota. Enlazar notas relacionadas con `[[Nombre de nota]]`.
- Escribir en español, corto y directo.
- Al terminar, decir la ruta de la nota creada o editada.

## No hacer

- No tocar `.obsidian/` (configuración de la app).
- No borrar notas; si algo ya no sirve, moverlo a `40-Archivo/`.
- No copiar PDFs ni código a la bóveda; enlazarlos.
