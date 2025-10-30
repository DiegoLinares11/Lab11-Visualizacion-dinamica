#!/bin/bash
# Script para ejecutar el Dashboard

echo "🚀 Iniciando Dashboard de Hidrocarburos..."
echo ""

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Entorno virtual activado"
else
    echo "⚠️  Entorno virtual no encontrado"
    echo "   Ejecuta primero: ./setup.sh"
    exit 1
fi

# Verificar si streamlit está instalado
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit no está instalado"
    echo "   Ejecuta: pip install -r requirements.txt"
    exit 1
fi

# Ejecutar dashboard
echo "📊 Abriendo dashboard en el navegador..."
echo ""
streamlit run app.py
