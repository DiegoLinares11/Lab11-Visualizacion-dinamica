@echo off
REM Script de instalación para Windows

echo ========================================
echo Dashboard de Hidrocarburos - Guatemala
echo Instalacion Automatica
echo ========================================
echo.

REM Verificar Python
echo 1. Verificando instalacion de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado. Por favor instalalo primero.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [OK] Python encontrado: %PYTHON_VERSION%
echo.

REM Crear entorno virtual
echo 2. Creando entorno virtual...
if exist venv (
    echo [AVISO] El entorno virtual ya existe.
    set /p response="Deseas recrearlo? (s/n): "
    if /i "%response%"=="s" (
        rmdir /s /q venv
        python -m venv venv
        echo [OK] Entorno virtual recreado
    ) else (
        echo [SKIP] Usando entorno virtual existente
    )
) else (
    python -m venv venv
    echo [OK] Entorno virtual creado
)
echo.

REM Activar entorno virtual
echo 3. Activando entorno virtual...
call venv\Scripts\activate.bat
echo [OK] Entorno virtual activado
echo.

REM Actualizar pip
echo 4. Actualizando pip...
python -m pip install --upgrade pip >nul 2>&1
echo [OK] pip actualizado
echo.

REM Instalar dependencias
echo 5. Instalando dependencias...
echo    Esto puede tomar varios minutos...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Hubo un error instalando las dependencias
    echo    Intenta instalarlas manualmente con: pip install -r requirements.txt
    pause
    exit /b 1
)

echo [OK] Todas las dependencias instaladas correctamente
echo.

REM Verificar archivos de datos
echo 6. Verificando archivos de datos...
if exist data\Estadisticas_historicas_comercializacion.xlsx (
    echo [OK] Archivo de estadisticas encontrado
) else (
    echo [AVISO] Archivo de estadisticas no encontrado en data\
    echo    Asegurate de copiar los archivos .xlsx a la carpeta data\
)
echo.

REM Completado
echo ========================================
echo [OK] Instalacion completada
echo ========================================
echo.
echo Para ejecutar el dashboard:
echo   1. Activa el entorno virtual: venv\Scripts\activate
echo   2. Ejecuta: streamlit run app.py
echo.
echo Disfruta explorando los datos!
echo.
pause
