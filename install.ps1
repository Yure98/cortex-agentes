# Cortex — Windows/PowerShell. Mesma transação usada no Mac/Linux.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$installer = Join-Path $root "scripts/install.py"
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $installer @args
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python $installer @args
} else {
    throw "Instale Python 3.10 ou superior e habilite o comando Python no terminal."
}
exit $LASTEXITCODE
