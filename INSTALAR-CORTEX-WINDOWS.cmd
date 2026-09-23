@echo off
setlocal
chcp 65001 >nul
title Cortex 2.0 - Yure Digital
cd /d "%~dp0"
echo Cortex 2.0 - Instalacao e atualizacao
echo Propriedade da Yure Digital. Compartilhamento sem autorizacao proibido.
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
set "CORTEX_RESULT=%ERRORLEVEL%"
if not "%CORTEX_RESULT%"=="0" (
  echo.
  echo A instalacao nao foi concluida. Leia a orientacao acima.
) else (
  echo.
  echo Pronto. Abra uma nova sessao do Claude Code e digite /prev seguido do caso.
)
echo.
pause
exit /b %CORTEX_RESULT%
