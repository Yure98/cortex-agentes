# Cortex 2.0 — Yure Digital. Instala e atualiza sem exigir administrador.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$installer = Join-Path $root "scripts/install.py"
$pythonCommand = $null
$pythonArguments = @()
foreach ($candidate in @("py", "python", "python3")) {
    if (Get-Command $candidate -ErrorAction SilentlyContinue) {
        $prefix = @()
        if ($candidate -eq "py") { $prefix = @("-3") }
        & $candidate @prefix -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" 2>$null
        if ($LASTEXITCODE -eq 0) {
            $pythonCommand = $candidate
            $pythonArguments = $prefix
            break
        }
    }
}
if (-not $pythonCommand) {
    Write-Host "Python 3.10 ou superior nao foi encontrado." -ForegroundColor Yellow
    Write-Host "1. Instale Python em https://www.python.org/downloads/windows/ e marque Add python.exe to PATH."
    Write-Host "2. Feche esta janela e abra INSTALAR-CORTEX-WINDOWS.cmd novamente."
    Write-Host "Nenhuma skill foi substituida."
    exit 1
}
& $pythonCommand @pythonArguments $installer @args
exit $LASTEXITCODE
