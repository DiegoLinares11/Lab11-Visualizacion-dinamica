#!/bin/bash
# Script de instalación automática para el Dashboard de Hidrocarburos

echo "========================================"
echo "Dashboard de Hidrocarburos - Guatemala"
echo "Instalación Automática"
echo "========================================"
echo ""

# Verificar Python
echo "1️⃣ Verificando instalación de Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor instálalo primero."
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ Python encontrado: $PYTHON_VERSION"
echo ""

# Crear entorno virtual
echo "2️⃣ Creando entorno virtual..."
if [ -d "venv" ]; then
    echo "⚠️  El entorno virtual ya existe. ¿Deseas recrearlo? (s/n)"
    read -r response
    if [[ "$response" =~ ^[Ss]$ ]]; then
        rm -rf venv
        python3 -m venv venv
        echo "✅ Entorno virtual recreado"
    else
        echo "⏭️  Usando entorno virtual existente"
    fi
else
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
fi
echo ""

# Activar entorno virtual
echo "3️⃣ Activando entorno virtual..."
source venv/bin/activate
echo "✅ Entorno virtual activado"
echo ""

# Actualizar pip
echo "4️⃣ Actualizando pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip actualizado"
echo ""

# Instalar dependencias
echo "5️⃣ Instalando dependencias..."
echo "   Esto puede tomar varios minutos..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Todas las dependencias instaladas correctamente"
else
    echo "❌ Hubo un error instalando las dependencias"
    echo "   Intenta instalarlas manualmente con: pip install -r requirements.txt"
    exit 1
fi
echo ""

# Verificar archivos de datos
echo "6️⃣ Verificando archivos de datos..."
if [ -f "data/Estadisticas_historicas_comercializacion.xlsx" ]; then
    echo "✅ Archivo de estadísticas encontrado"
else
    echo "⚠️  Archivo de estadísticas no encontrado en data/"
    echo "   Asegúrate de copiar los archivos .xlsx a la carpeta data/"
fi
echo ""

# Completado
echo "========================================"
echo "✅ Instalación completada"
echo "========================================"
echo ""
echo "Para ejecutar el dashboard:"
echo "  1. Activa el entorno virtual: source venv/bin/activate"
echo "  2. Ejecuta: streamlit run app.py"
echo ""
echo "¡Disfruta explorando los datos! 📊"
