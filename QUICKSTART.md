# 🚀 Inicio Rápido - Dashboard de Hidrocarburos

## Instalación Express (3 comandos)

### Linux / macOS
```bash
./setup.sh
source venv/bin/activate
./run.sh
```

### Windows
```cmd
.\setup.bat
venv\Scripts\activate
.\run.bat
```

## ¿Qué hace cada comando?

1. **setup.sh/bat**: Instala todas las dependencias automáticamente
2. **source venv/bin/activate**: Activa el entorno virtual
3. **run.sh/bat**: Ejecuta el dashboard

## ¿No funcionan los scripts?

### Instalación Manual

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar dashboard
streamlit run app.py
```

## Verificar Instalación

```bash
# Verificar que streamlit está instalado
streamlit --version

# Debería mostrar: Streamlit, version 1.31.0
```

## Acceder al Dashboard

Una vez ejecutado, el dashboard estará disponible en:
- URL Local: http://localhost:8501
- URL Red: http://TU_IP:8501

El navegador se abrirá automáticamente.

## Problemas Comunes

### "ModuleNotFoundError: No module named 'streamlit'"
**Solución**: 
```bash
pip install -r requirements.txt
```

### "python: command not found"
**Solución**: Instala Python 3.8+ desde https://python.org

### "Permission denied" en Linux/Mac
**Solución**: 
```bash
chmod +x setup.sh run.sh
```

### El puerto 8501 está ocupado
**Solución**: 
```bash
streamlit run app.py --server.port 8502
```

## Estructura del Proyecto

```
hydrocarbon_dashboard/
├── app.py              ← ARCHIVO PRINCIPAL
├── config.py           ← Configuración
├── requirements.txt    ← Dependencias
├── data/              ← Datos (xlsx)
└── utils/             ← Módulos auxiliares
```

## Siguiente Paso

Lee el **README.md** completo para detalles de uso, características y documentación técnica.

---

