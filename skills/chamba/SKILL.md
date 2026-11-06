---
name: chamba
description: Búsqueda de puestos de trabajo para Tobias. Usar cuando pida /chamba, buscar trabajo, pasantías o puestos que encajen (LinkedIn, Computrabajo, Bumeran, ZonaJobs, Indeed, Get on Board), con o sin criterios (remoto, part time, rubro, tecnologías, tipo de empresa, salario, contrato...); ver o actualizar su lista de puestos con % de compatibilidad; anotar postulaciones; guardar qué tipo de trabajo busca; o medir su evolución ("Chamba, ¿cómo vengo?", "¿cuánto crecí?", "¿mejoré?"). No pule el CV ni analiza el mercado: eso lo hace la skill analisis-cv.
---

# Chamba: búsqueda de puestos

Buscás puestos que encajen con Tobias y con lo que él quiere, calculás la compatibilidad, le mostrás los resultados en el chat y los guardás en el cerebro. Hablale en español rioplatense, simple y directo.

## Rutas

- **Perfil (fuente de verdad):** `C:\Users\Tobias\source\serio\` (CV original, CV modificable si existe, portafolio, certificados y `Datos confirmados.md`).
- Cerebro: `C:\Users\Tobias\source\taller-de-duendes\cerebro\10-Proyectos\Búsqueda laboral\`
  - `Búsqueda laboral.md`: nota principal (Puestos, Postulaciones, Bitácora).
  - `Puestos encontrados.md`: la lista acumulada de puestos.
  - `Qué busco.md`: criterios guardados (se crea cuando Tobias pide guardarlos).
  - `Evolución profesional.md`: checkpoints de cómo viene (sección 6).
- Texto de un docx: `python "C:/Users/Tobias/source/taller-de-duendes/skills/chamba/scripts/docx-a-texto.py" "<ruta.docx>"`

## Perfil de Tobias

- Antes de puntuar, leé **todo** `serio/`. Lo que sabés de Tobias sale solo de ahí: no supongas tecnologías, años ni idiomas.
- Si un aviso pide algo que no figura, va en "Le falta" como "confirmar X" y se lo preguntás al final. Si Tobias lo confirma, anotalo en `serio\Datos confirmados.md` con la fecha (lo comparte con la skill `analisis-cv`).
- **Perfil anónimo** para Sherlock: título y nivel, ciudad, stack principal y proyectos en una línea. Sin nombre, mail, teléfono ni links personales. Los datos personales nunca van en búsquedas web.

## 1. Criterios de búsqueda

Tobias puede decir qué tipo de trabajo busca, en el pedido (ej. `/chamba remoto, part time, backend .NET, nada de consultoras`) o en el chat. Sacá los criterios de ahí:

| Criterio | Ejemplos |
|---|---|
| Rol, rubro y tecnologías | backend .NET, Android, full stack JS · incluir Kotlin · evitar PHP |
| Seniority | pasantía, trainee, junior |
| Modalidad y lugar | remoto, híbrido, presencial · Córdoba, Argentina, exterior |
| Jornada y horario | part time, full time, compatible con el cursado, solo mañana |
| Tipo de contratación | relación de dependencia, pasantía, freelance, contrato temporal |
| Salario | mínimo $X (solo si el aviso lo dice) |
| Tipo de empresa | startup, empresa de producto, consultora, software factory · tamaño · industria (fintech, salud, agro) |
| Idioma del trabajo | español, inglés |
| Otros | capacitación, mentoría, beneficios · empresas a excluir |
| Búsqueda | cantidad de avisos (por defecto 10), antigüedad máxima (por defecto 30 días) |

- **Excluyente o preferido:** "sí o sí", "solo", "nada de" → **excluyente** (si el aviso no lo cumple, no entra; si el aviso no lo dice, entra con "sin dato"). "Mejor", "prefiero", "si se puede" → **preferido** (no filtra, suma en la columna "Criterios"). Si no está claro, es preferido.
- **Sin criterios:** usá los de `Qué busco.md`. Si no existe, usá el perfil del CV con "Córdoba o remoto desde Argentina", y al final ofrecele guardar criterios.
- **Guardar:** si Tobias dice "guardá esto como lo que busco" (o acepta tu oferta), escribí `Qué busco.md` (formato abajo) y agregá `- [[Qué busco]]: criterios de búsqueda` en la sección "Puestos" de `Búsqueda laboral.md`. Los criterios de un pedido puntual se suman a los guardados solo para esa búsqueda; si se contradicen, gana el del pedido.
- Antes de buscar, repetí los criterios en una línea ("Busco: 10 avisos, backend .NET junior, remoto (excluyente), part time (preferido)") y seguí. Preguntá solo si falta el rol y no hay criterios guardados.

```markdown
---
tags: [busqueda-laboral, criterios]
fecha: AAAA-MM-DD
fuente: skill chamba
---
# Qué busco

Criterios por defecto de la skill `chamba`. Ver [[Búsqueda laboral]].

## Excluyentes
- Modalidad: remoto o Córdoba

## Preferidos
- Jornada: part time

## Búsqueda
- Cantidad: 10 · Antigüedad máxima: 30 días
```

## 2. Buscar

1. Leé `Puestos encontrados.md` (si existe) y juntá las URLs que ya están, para no repetir.
2. Delegá al agente **sherlock** (herramienta Agent, `subagent_type: "sherlock"`). Completá lo que está entre `< >`:

   ```
   Buscá <N> avisos de trabajo ABIERTOS para: <rol/rubro y seniority>.
   Criterios excluyentes (si el aviso no los cumple, no lo cuentes; si no dice, contalo y marcá "sin dato"): <lista o "ninguno">.
   Criterios preferidos (no filtran; anotá si el aviso los cumple): <lista o "ninguno">.
   Perfil (sin datos personales): <perfil anónimo>.
   Portales: LinkedIn (solo avisos públicos que aparezcan en la búsqueda web, ej. linkedin.com/jobs/view/...; NO abras linkedin.com en el navegador integrado ni inicies sesión), Computrabajo, Bumeran, ZonaJobs, Indeed, Get on Board y sitios de empleo de empresas.
   Solo avisos de los últimos <días> días. Solo contá un aviso si abriste y leíste su página.
   No incluyas estas URLs (ya las tengo): <lista o "ninguna">.
   Para cada aviso, en una tabla de la nota: URL, puesto, empresa, tipo de empresa, ciudad, modalidad, jornada y horario, tipo de contratación, salario (si lo dice), fecha de publicación, seniority pedido, requisitos obligatorios (lista), deseables (lista), idioma pedido, y si cumple cada criterio (sí / no / sin dato).
   Título de la nota: "Búsqueda de puestos - <rol> (AAAA-MM-DD)".
   ```

3. Leé la nota de Sherlock entera (te pasa la ruta). Descartá los avisos que no cumplan un excluyente.
4. Calculá la compatibilidad (sección 3) y el puntaje de criterios de cada aviso.
5. Si Sherlock no está disponible, hacé la búsqueda vos con WebSearch y WebFetch siguiendo las mismas reglas.
6. Nunca te postules, no llenes formularios ni mandes mensajes: Tobias se postula solo.

## 3. Compatibilidad: rúbrica fija de 100 puntos (versión **v1**)

Mide cuánto encaja **Tobias con el aviso** y no cambia con los criterios, así los % se pueden comparar entre búsquedas. Lo que Tobias quiere va aparte, en la columna "Criterios".

Si alguna vez cambia esta rúbrica, subí la versión (v2, v3...) acá y anotá en una línea qué cambió. Cada búsqueda y cada checkpoint registra con qué versión se puntuó.

| Criterio | Puntos | Cómo se cuenta |
|---|---|---|
| Requisitos obligatorios | 50 | 50 × (cumplidos + 0,5 × parciales) / total |
| Deseables | 15 | 15 × (cumplidos + 0,5 × parciales) / total |
| Seniority | 15 | trainee/pasante/junior o sin experiencia exigida: 15 · hasta 1 año: 10 · 1–2 años o semi senior: 5 · 3+ años o senior: 0 |
| Ubicación y modalidad | 10 | remoto desde Argentina, o presencial/híbrido en Córdoba: 10 · presencial/híbrido en otra ciudad de Argentina: 3 · exige otro país o mudarse: 0 |
| Idioma | 10 | no pide otro idioma, o pide uno que `serio/` respalda: 10 · pide uno que `serio/` no menciona: 0 (y preguntale a Tobias) |

- **Cumplido:** está en `serio/` tal cual. **Parcial:** tiene algo cercano (ej. pide Java y tiene Kotlin; pide SQL Server y tiene PostgreSQL). **No:** no figura.
- Seniority, ubicación e idioma se cuentan solo en su fila, no en "obligatorios" (para no contarlos dos veces).
- Si el aviso se contradice (ej. la ficha resumida dice "2 años" y el texto acepta junior), usá el texto del aviso y anotá la contradicción en "Por qué".
- Si el aviso no lista deseables, esa fila da 15. Si un dato del aviso no se sabe, poné el máximo y marcá "sin dato" en la justificación.
- "Años de experiencia" se compara con la experiencia que figure en `serio/` (proyectos y pasantías cuentan como experiencia práctica, no como años de trabajo en desarrollo).
- Redondeá a múltiplos de 5. Lectura: **75+** encaja fuerte · **50–70** vale la pena · **<50** lejos.

**Criterios:** cumplidos / preferidos totales, más lo que no se sabe (ej. `2/3 · jornada sin dato`). Si la búsqueda no tuvo preferidos, poné `—`.

## 4. Lista de puestos (cerebro)

Archivo: `Puestos encontrados.md`. Si no existe, crealo así y agregá `- [[Puestos encontrados]]: lista acumulada con % de compatibilidad` en la sección "Puestos" de `Búsqueda laboral.md`:

```markdown
---
tags: [busqueda-laboral, puestos]
fecha: AAAA-MM-DD
fuente: skill chamba
---
# Puestos encontrados

% original, con la rúbrica fija de la skill `chamba` (v1: obligatorios 50 · deseables 15 · seniority 15 · ubicación 10 · idioma 10). "Criterios" = preferidos que cumple el aviso. Ver [[Búsqueda laboral]].

## Puestos
| % | Criterios | Puesto | Empresa | Ubicación / modalidad | Publicado | Encontrado | Por qué | Le falta | Estado |
|---|---|---|---|---|---|---|---|---|---|

## Búsquedas
| Fecha | Qué se buscó (criterios) | Nuevos | Rúbrica | Nota |
|---|---|---|---|---|
```

- Fila: `| 70 | 2/3 | [Puesto](url) | Empresa | Córdoba · híbrido | 2026-11-02 | 2026-11-06 | Oblig. 3/4, desea. 1/2, junior, Córdoba, sin inglés | Docker; confirmar inglés | nuevo |`
- **Sin repetidos:** antes de agregar, compará la URL (sin `utm_*`, `ref` ni `trackingId`; conservá el parámetro que identifica el aviso, ej. `jk=` en Indeed) y también empresa + puesto + ciudad. Si es el mismo aviso en otro portal, no lo agregues: sumá " · [otro portal](url)" en la fila existente.
- Agregá las filas nuevas y dejá la tabla ordenada por % (de mayor a menor). No borres filas viejas.
- Estado: `nuevo` · `postulado` · `descartado` · `cerrado`. Cuando Tobias diga que se postuló, cambiá el estado y agregá una fila en "Postulaciones" de `Búsqueda laboral.md`.
- En "Búsquedas" agregá una fila con los criterios usados (excluyentes y preferidos), la versión de rúbrica y el enlace a la nota de Sherlock (`[[Búsqueda de puestos - ...]]`).
- "Por qué" y "Le falta": cortos (máx. ~15 palabras cada uno). Sin `|` dentro de las celdas.
- El % de esta tabla es el **original** (con el perfil del día en que se encontró). No lo sobrescribas nunca: los recálculos van en `Evolución profesional.md`.

## 5. Qué le mostrás a Tobias

- Los criterios usados, en una línea.
- Tabla corta ordenada por %: puesto con link, empresa, modalidad, %, criterios y lo que le falta.
- Cuántos avisos se descartaron por criterios excluyentes y qué portales no se pudieron leer.
- Lo que tenés que preguntarle (datos que no figuran en `serio/`).
- Ruta de la lista: `cerebro/10-Proyectos/Búsqueda laboral/Puestos encontrados.md`.
- Si hay brechas que se repiten, sugerí la skill `analisis-cv` para trabajar el CV.

## 6. Evolución profesional ("Chamba, ¿cómo vengo?")

Comparar promedios entre búsquedas distintas engaña porque cada una trae avisos distintos. Por eso se mide de dos formas fijas:

- **Re-puntuar avisos viejos:** los mismos avisos, con el perfil de hoy. Muestra cuánto creció Tobias contra un mercado fijo.
- **Búsqueda de control:** una búsqueda con criterios fijos que se repite cada ~3 meses. Muestra cómo encaja con el mercado actual.

### Pasos

1. Leé todo `serio/` (incluido `Datos confirmados.md`) y anotá qué hay nuevo desde el checkpoint anterior: archivos nuevos, certificados, datos confirmados con fecha posterior y cambios en el CV modificable.
2. **Re-puntuá** todos los avisos de `Puestos encontrados.md`, en cualquier estado. Sacá sus requisitos, deseables, seniority, modalidad e idioma de la nota de Sherlock enlazada en "Búsquedas" y aplicá la rúbrica actual contra el perfil de hoy. Si un aviso no tiene sus requisitos guardados, salteálo y avisalo.
3. **Búsqueda de control:** mirá la sección "Búsqueda de control" de la nota.
   - Si no está definida, proponele una a Tobias (ej. "desarrollador junior/trainee, Córdoba o remoto desde Argentina, 10 avisos") y guardala cuando diga que sí.
   - Si pasaron ~3 meses o más desde la última corrida (o nunca se corrió), ofrecele correrla. Se corre como la sección 2 con **exactamente** esos criterios. Los avisos nuevos se suman a `Puestos encontrados.md` como siempre.
4. **Brechas:** contá en cuántos avisos aparece cada brecha de "Le falta", tanto del re-puntaje de hoy como de la búsqueda de control. Unificá nombres equivalentes ("inglés" e "inglés intermedio" → "Inglés"). "Confirmar X" cuenta como brecha de X. No cuentes lo que no depende de Tobias (ciudad del aviso, seniority pedido).
5. **Brechas cerradas:** las que estaban en el checkpoint anterior y ya no están. Para cada una, decí qué la cerró y en qué archivo de `serio/` está (ej. "Docker: certificado nuevo `serio/...pdf`"). Si no hay checkpoint anterior, poné "primer checkpoint".
6. **Prioridades:** 2 o 3 cosas para aprender o mostrar, elegidas por las brechas más repetidas y que se puedan cerrar con algo concreto (un curso, un proyecto, confirmar un dato que quizás ya tiene).
7. Agregá el checkpoint en la nota (el más nuevo arriba) y respondé con un resumen corto: promedio antes → ahora, brechas que más se repiten y prioridades.

**Versión de rúbrica:** cada checkpoint dice con qué versión se puntuó. No compares promedios entre checkpoints de versiones distintas. Si la versión cambió, escribí "cambio de rúbrica (v1 → v2), arranca serie nueva" y compará solo desde ahí. En la tabla antes → ahora, si el % original es de otra versión, poné "—" en "Original".

### Nota `Evolución profesional.md`

Si no existe, creala así y enlazala: `- [[Evolución profesional]]: checkpoints de cómo vengo` en la sección "Puestos" de `Búsqueda laboral.md`, y la misma línea en la sección "Búsqueda de trabajo" de `cerebro/20-Areas/Profesional/Perfil profesional.md`.

```markdown
---
tags: [busqueda-laboral, evolucion]
fecha: AAAA-MM-DD
fuente: skill chamba
---
# Evolución profesional

Cómo vengo contra el mercado. Se mide re-puntuando los mismos avisos con el perfil actual y repitiendo una búsqueda de control. Ver [[Búsqueda laboral]] · [[Puestos encontrados]] · [[Perfil profesional]].

## Búsqueda de control
- Rol: <...>
- Criterios: <excluyentes y preferidos>
- Cantidad: <N> avisos · Portales: los de la skill `chamba`
- Repetir cada: ~3 meses
- Definida: AAAA-MM-DD · Última corrida: AAAA-MM-DD (o "nunca")

## Checkpoints

### AAAA-MM-DD · rúbrica v1
- **Perfil:** <qué hay nuevo en `serio/` desde el anterior, o "primer checkpoint">
- **Re-puntuados:** <N> avisos · promedio original <X>% → ahora <Y>% (checkpoint anterior: <Z>%)
- **Búsqueda de control:** <N> avisos, promedio <W>% · o "no se corrió"

| Aviso | Original | Ahora | Qué cambió |
|---|---|---|---|
| [Puesto - Empresa](url) | 60 | 70 | confirmó inglés |

**Brechas más repetidas**
| Brecha | Avisos |
|---|---|
| Inglés | 3 |

**Brechas cerradas:** <brecha: qué hizo + archivo de `serio/`> · o "ninguna" / "primer checkpoint"

**Prioridades**
1. <...>
2. <...>
```
