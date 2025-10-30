@echo off
REM Script para ejecutar el Dashboard en Windows

echo Iniciando Dashboard de Hidrocarburos...
echo.

REM Verificar entorno virtual
if not exist venv (
    echo [ERROR] Entorno virtual no encontrado
    echo    Ejecuta primero: setup.bat
    pause
    exit /b 1
)

REM Activar entorno virtual
call venv\Scripts\activate.bat
echo [OK] Entorno virtual activado
echo.

REM Verificar streamlit
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Streamlit no esta instalado
    echo    Ejecuta: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Ejecutar dashboard
echo Abriendo dashboard en el navegador...
echo.
streamlit run app.py
