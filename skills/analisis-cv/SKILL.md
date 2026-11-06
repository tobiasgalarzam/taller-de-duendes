---
name: analisis-cv
description: Análisis del CV y el portafolio de Tobias contra lo que piden las empresas. Usar cuando pida /analisis-cv o "analisisCV", quiera saber qué buscan las empresas para su perfil o para un rol o rubro, pida revisar, pulir o adaptar su CV o currículum (para un aviso, un puesto o un rubro), o pida sugerencias para su portafolio. No busca puestos: eso lo hace la skill chamba.
---

# Análisis del CV

Investigás qué piden las empresas, lo comparás con el CV y el portafolio de Tobias, le contás en el chat qué encontraste y le proponés mejoras. Hablale en español rioplatense, simple y directo.

## Rutas

- **Fuente de verdad:** `C:\Users\Tobias\source\serio\`
- **CV original** (nunca se modifica): `serio\Tobias_Galarza_Montoro_CV.docx` y `.pdf`
- **CV modificable** (el único que esta skill escribe): `serio\Tobias_Galarza_Montoro_CV_modificable.docx` y `.pdf`
- Portafolio: `serio\Portafolio_Tobias_Galarza.html` (solo se leen y se sugieren cambios; no se edita)
- Datos que Tobias confirmó en el chat: `serio\Datos confirmados.md` (lo comparte con la skill `chamba`)
- Texto de un docx: `python "C:/Users/Tobias/source/taller-de-duendes/skills/analisis-cv/scripts/docx-a-texto.py" "<ruta.docx>"`

Siempre hay dos CV: el original y el modificable. No se crean otras versiones.

## Regla de oro: no inventar

Todo dato sobre Tobias (estudios, fechas, tecnologías, experiencia, logros, idiomas, niveles, certificados) tiene que salir de un archivo de `serio/`. Antes de empezar, leé **todos** los archivos de `serio/`: los `.pdf` y `.jpg` con Read, los `.docx` con el script, y el `.html` y los `.md` con Read. Si hay archivos nuevos, leelos también.

- Si algo no figura, **preguntá**: "¿Esto lo tenés? (ej. inglés: ¿qué nivel?)". No lo agregues hasta que Tobias diga que sí.
- Cuando confirme un dato nuevo, anotalo en `serio\Datos confirmados.md` con la fecha (`- 2026-11-06: Usa Git y GitHub (repos de GeoAlarm y del proyecto DDS).`). Desde ahí cuenta como fuente.
- Se puede: reordenar, redactar mejor, elegir qué destacar, sacar lo que no suma para ese objetivo y usar las palabras del mercado cuando dicen lo mismo que el CV.
- No se puede: inventar métricas, años, niveles, roles ("lideré" si lo hizo solo), tecnologías, títulos o fechas, ni inflar un proyecto académico como trabajo pago.
- Datos personales (nombre, mail, teléfono, foto): quedan solo en los archivos del CV. **Nunca** van en búsquedas web ni en el pedido a Sherlock.

## Pasos

### 1. Objetivo

Sacá del pedido contra qué se compara: un rol o rubro ("junior .NET"), un aviso puntual (si pasa un link, leelo con WebFetch) o un enfoque ("primer trabajo", "pasantía"). Si vino con texto (ej. `/analisis-cv backend .NET en Córdoba`), ese es el objetivo. Si no dijo nada, usá el título del CV y preguntale si le sirve.

### 2. Qué buscan las empresas

- **Aviso puntual:** alcanza con leer el aviso. No hace falta Sherlock.
- **Rol o rubro:** delegá al agente **sherlock** (herramienta Agent, `subagent_type: "sherlock"`) con este pedido:

  ```
  Investigá qué piden hoy las empresas en <Argentina / Córdoba / remoto> para puestos de <rol> nivel <trainee/junior/pasantía>.
  Perfil (sin datos personales): <perfil anónimo>.
  Leé al menos 10 avisos reales y recientes (últimos 60 días) en LinkedIn (solo páginas públicas por búsqueda web; NO abras linkedin.com en el navegador ni inicies sesión), Computrabajo, Bumeran, ZonaJobs, Indeed, Get on Board, y sumá informes o encuestas del mercado si hay.
  Quiero: tecnologías y herramientas más pedidas (contá en cuántos avisos aparece cada una), seniority y años pedidos, nivel de inglés, habilidades blandas que repiten, qué esperan ver en el CV o el portafolio (GitHub, proyectos, deploy) y rangos salariales si hay datos públicos.
  Título de la nota: "Qué piden las empresas - <rol> (AAAA-MM-DD)".
  ```

  Sherlock guarda su nota (con PDF) en `cerebro/00-Inbox/` y te pasa la ruta: leela entera.

**Perfil anónimo:** armalo desde `serio/` con el título y el nivel, la ciudad, el stack principal y los proyectos en una línea. Sin nombre, mail, teléfono ni links personales.

### 3. Informe en el chat

Respondé en el mismo chat, en este orden y corto:

1. **Qué piden:** tabla `Requisito | En cuántos avisos | ¿Lo tenés?`. En "¿Lo tenés?" va sí, parcial o no, con el archivo de `serio/` de donde sale (ej. "sí: CV, Habilidades técnicas").
2. **Lo que ya tenés a favor:** 2 a 4 puntos.
3. **Lo que te falta:** las brechas ordenadas por cuántos avisos las piden, con una idea concreta para cerrar cada una (un curso, un proyecto chico, mostrar mejor algo que ya tenés).
4. **Preguntas:** lo que pide el mercado y no figura en `serio/` ("¿Usás Git? ¿Qué nivel de inglés tenés?").
5. **Cambios propuestos al CV:** tabla `Sección | Antes | Después | Por qué`.
6. **Sugerencias para el portafolio:** qué agregar, sacar o reordenar en `Portafolio_Tobias_Galarza.html` y por qué. Solo son sugerencias: el portafolio no se edita.

Cerrá preguntando qué cambios del CV aplica (todos, algunos o ninguno) y esperá la respuesta.

### 4. Guardar el CV modificable

Solo con el ok de Tobias, y solo los cambios que aprobó.

1. **Base:** si el modificable no existe, copiá el `.docx` original como `Tobias_Galarza_Montoro_CV_modificable.docx`. Si ya existe, los cambios van sobre el modificable. Si Tobias pide "empezar de cero", volvé a copiar el original encima del modificable.
2. **Editar:** cambiá solo el texto de `word/document.xml` (descomprimir, editar, volver a comprimir), así se mantienen el diseño, la columna azul y la foto. Usá la skill `anthropic-skills:docx`. El CV es una tabla de dos columnas: no rompas la estructura.
3. **PDF:** `"C:/Program Files/LibreOffice/program/soffice.exe" --headless --convert-to pdf --outdir "C:/Users/Tobias/source/serio" "C:/Users/Tobias/source/serio/Tobias_Galarza_Montoro_CV_modificable.docx"`
4. **Revisar el PDF con Read:** que entre en **una página**, que no se haya cortado texto y que no haya datos sin fuente. Si se pasa de una página, acortá la redacción (no los datos clave).
5. **Cerrar** con las rutas del docx y el pdf modificables y un resumen de qué cambió (3 a 6 líneas).

## No hacer

- No modificar el CV original ni el portafolio.
- No crear más versiones del CV que el modificable.
- No buscar puestos ni puntuar avisos: eso lo hace la skill `chamba`.
