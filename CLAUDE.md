# Taller de duendes

Mesa de trabajo para fabricar skills, agentes y el segundo cerebro (Obsidian).
Todo lo que se construye acá tiene que poder usarse desde cualquier otro proyecto de Claude Code.

## Estructura

- `skills/<nombre>/SKILL.md` — skills propias. Cada skill es una carpeta.
- `agents/<nombre>.md` — subagentes propios.
- `descargas/` — cuarentena: skills/agentes bajados de internet. Se revisan antes de moverlos a `skills/` o `agents/`.
- `cerebro/` — bóveda de Obsidian (segundo cerebro).
- `scripts/enlazar.ps1` — publica skills y agentes en `~/.claude` para que todas las sesiones los vean.

## Reglas

- Después de crear, renombrar o borrar una skill o agente, correr:
  `powershell -ExecutionPolicy Bypass -File scripts/enlazar.ps1`
  El script crea enlaces (junctions) en `~/.claude/skills` y `~/.claude/agents`; las ediciones se ven al instante en otros proyectos sin volver a correrlo.
- Nunca editar directamente `~/.claude/skills/synced` (lo maneja la app).
- Nada de `descargas/` se enlaza globalmente hasta revisarlo: leer todo el contenido (scripts incluidos) y moverlo a `skills/` o `agents/`.
- Nombres de skills y agentes en kebab-case, sin tildes ni espacios.
- El frontmatter `description` de cada skill/agente dice **cuándo** usarla; es lo que Claude lee para decidir si la activa.
