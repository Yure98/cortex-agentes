# Cortex — Instalador (Windows / PowerShell)
# Uso: clone o repo e rode  ->  powershell -ExecutionPolicy Bypass -File install.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$claude = Join-Path $HOME ".claude"
$skillsDst = Join-Path $claude "skills"
$cmdsDst = Join-Path $claude "commands"

Write-Host ""
Write-Host "==================================================" -ForegroundColor Green
Write-Host "  CORTEX - Agentes de IA para Advocacia" -ForegroundColor Green
Write-Host "  Instalando no Claude Code..." -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""

New-Item -ItemType Directory -Force -Path $skillsDst | Out-Null
New-Item -ItemType Directory -Force -Path $cmdsDst | Out-Null

# Skills
Get-ChildItem -Path (Join-Path $root "skills") -Directory | ForEach-Object {
  $dst = Join-Path $skillsDst $_.Name
  if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
  Copy-Item -Recurse -Force $_.FullName $dst
  Write-Host "  [skill]   $($_.Name)" -ForegroundColor Cyan
}

# Comandos
Get-ChildItem -Path (Join-Path $root "commands") -Filter *.md | ForEach-Object {
  Copy-Item -Force $_.FullName (Join-Path $cmdsDst $_.Name)
  Write-Host "  [comando] /$($_.BaseName)" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Instalacao concluida!" -ForegroundColor Green
Write-Host "Reinicie o Claude Code e teste:  /cnis  /peticionar  /decisor  /recurso" -ForegroundColor Yellow
Write-Host ""
