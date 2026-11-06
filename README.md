# Taller de duendes

Mi mesa de trabajo para construir **agentes y skills para [Claude Code](https://docs.claude.com/en/docs/claude-code)**. Uso todo esto en el día a día para investigar, estudiar y organizar mi búsqueda laboral, y todo queda conectado a un segundo cerebro en Obsidian.

No es "pedirle código a la IA y pegarlo". Cada agente tiene un rol acotado, herramientas limitadas, reglas explícitas y un formato de salida que puedo revisar.

## Qué hay adentro

| Pieza | Tipo | Qué hace |
|---|---|---|
| [`sherlock`](agents/sherlock.md) | Subagente | Investiga un tema en la web (y con un navegador si la página lo necesita), contrasta las fuentes y guarda una nota con citas en el cerebro, con su PDF al lado. |
| [`profesor`](agents/profesor.md) | Subagente | Arma una clase o guía de estudio partiendo de mis apuntes y la completa con la web. |
| [`analisis-cv`](skills/analisis-cv/SKILL.md) | Skill | Compara mi CV con lo que piden las empresas (delega el relevamiento a Sherlock) y propone cambios. Solo edita una copia del CV, y solo con mi aprobación. |
| [`chamba`](skills/chamba/SKILL.md) | Skill | Busca puestos, calcula la compatibilidad con mi perfil y lleva el registro de postulaciones y de mi evolución. |
| [`cerebro`](skills/cerebro/SKILL.md) | Skill | Lee y escribe notas en la bóveda de Obsidian siguiendo su estructura (método PARA). |
| [`enlazar.ps1`](scripts/enlazar.ps1) | Script | Publica las skills y los agentes en `~/.claude` con *junctions*, así cualquier proyecto los usa y los cambios se ven al instante. |
| [`md-a-pdf.py`](agents/sherlock/md-a-pdf.py) · [`docx-a-texto.py`](skills/analisis-cv/scripts/docx-a-texto.py) | Scripts Python | Convierten las notas a PDF y extraen el texto de un `.docx`. |

## Cómo se conectan

```
Yo ──► Claude Code ──► skill (analisis-cv / chamba / cerebro)
                         │
                         ├─► subagente sherlock ──► web + navegador ──► nota con fuentes + PDF
                         │                                                  │
                         └─► subagente profesor ──► mis apuntes + web ──────┤
                                                                            ▼
                                                              cerebro/ (Obsidian)
```

## Reglas de diseño

Las reglas están escritas en cada skill y agente, no quedan en mi cabeza:

- **No inventar.** Todo dato sobre mí tiene que salir de un archivo. Si falta algo, el agente pregunta antes de escribir.
- **Fuentes verificables.** Sherlock solo cita páginas que abrió y leyó. Un extracto de búsqueda no cuenta como fuente, y si dos fuentes se contradicen lo muestra.
- **Privacidad.** Los datos personales nunca van en búsquedas web ni en pedidos a otros agentes. Para eso se arma un perfil anónimo.
- **Permisos mínimos.** Cada subagente declara solo las herramientas que necesita. El navegador se usa solo para leer: nada de logins, formularios ni CAPTCHAs.
- **Cuarentena.** Todo lo que se baja de internet va a [`descargas/`](descargas/README.md) y se lee entero, scripts incluidos, antes de habilitarlo.
- **Descripciones como contrato.** El `description` de cada skill dice *cuándo* activarla, y también qué **no** hace, para que no se pisen entre sí (por ejemplo, `chamba` busca puestos y `analisis-cv` pule el CV).

## Ejemplo de salida

[`ejemplos/`](ejemplos/) tiene una investigación real de Sherlock: *Demanda laboral de vibe coders y agentic engineers*, con 16 fuentes.

## Usarlo

Requisitos: Windows, Claude Code y Python 3. Obsidian es opcional, para ver el cerebro.

```powershell
git clone https://github.com/tobiasgalarzam/taller-de-duendes
cd taller-de-duendes
powershell -ExecutionPolicy Bypass -File scripts/enlazar.ps1
```

Las rutas dentro de las skills apuntan a mis carpetas (`C:\Users\Tobias\...`): hay que adaptarlas a las tuyas.

## Qué no está publicado

- El contenido del cerebro (notas de la facultad, proyectos y búsqueda laboral): es personal. Solo se publican la estructura y las [plantillas](cerebro/Plantillas/).
- Skills de terceros que uso, como [Impeccable](https://github.com/pbakaus/impeccable): se instalan desde su propio repo.
