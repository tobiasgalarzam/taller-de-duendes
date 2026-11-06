# Publica las skills y agentes del taller en ~/.claude para que cualquier sesión de Claude Code los use.
# Usa junctions (no requieren admin). Las ediciones en el taller se ven al instante.

$ErrorActionPreference = 'Stop'
$taller = Split-Path -Parent $PSScriptRoot
$claude = Join-Path $HOME '.claude'
$skillsGlobal = Join-Path $claude 'skills'
$agentsGlobal = Join-Path $claude 'agents'

New-Item -ItemType Directory -Force $skillsGlobal | Out-Null

function Es-Enlace($ruta) {
    $item = Get-Item -LiteralPath $ruta -Force -ErrorAction SilentlyContinue
    return $item -and ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)
}

# Skills: un enlace por carpeta, porque ~/.claude/skills también tiene cosas de la app (synced, .trash)
$skillsTaller = Join-Path $taller 'skills'
$nombres = @()
foreach ($skill in Get-ChildItem -Directory $skillsTaller) {
    if (-not (Test-Path (Join-Path $skill.FullName 'SKILL.md'))) { continue }
    $nombres += $skill.Name
    $destino = Join-Path $skillsGlobal $skill.Name
    if (Es-Enlace $destino) { continue }
    if (Test-Path $destino) { Write-Warning "Ya existe $destino y no es un enlace; lo salteo."; continue }
    New-Item -ItemType Junction -Path $destino -Target $skill.FullName | Out-Null
    Write-Host "skill enlazada: $($skill.Name)"
}

# Limpiar enlaces de skills que ya no existen en el taller
foreach ($item in Get-ChildItem -Force $skillsGlobal) {
    if ((Es-Enlace $item.FullName) -and ($item.Target -like "$skillsTaller*") -and ($nombres -notcontains $item.Name)) {
        [IO.Directory]::Delete($item.FullName)   # borra solo el enlace, no el destino
        Write-Host "enlace quitado: $($item.Name)"
    }
}

# Agentes: la carpeta entera es un enlace
$agentsTaller = Join-Path $taller 'agents'
if (-not (Test-Path $agentsGlobal)) {
    New-Item -ItemType Junction -Path $agentsGlobal -Target $agentsTaller | Out-Null
    Write-Host "agentes enlazados: $agentsGlobal -> $agentsTaller"
} elseif (-not (Es-Enlace $agentsGlobal)) {
    Write-Warning "$agentsGlobal ya existe como carpeta normal. Mové su contenido a $agentsTaller, borrala y volvé a correr el script."
}

Write-Host "Listo."
