#  ÍNDICE DE ARCHIVOS DEL PROYECTO
## Dashboard Interactivo de Hidrocarburos - Guatemala

---


##  CONTENIDO DEL PROYECTO

###  APLICACIÓN (Archivos Python)

#### 1. **app.py**   PRINCIPAL
   - Aplicación principal del dashboard
   - Interfaz de usuario con Streamlit
   - 3 vistas principales
   - Manejo de interactividad
   
#### 2. **config.py** 
   - Configuración central
   - Paleta de colores justificada
   - Parámetros de modelos
   - Textos de interfaz

#### 3. **generate_report.py** 
   - Script para generar el PDF del reporte
   - Usado para crear la documentación

###  MÓDULOS AUXILIARES (utils/)

#### 4. **utils/data_loader.py** 
   - Clase DataLoader
   - Carga de archivos Excel
   - Preprocesamiento de datos
   - Agregaciones y estadísticas

#### 5. **utils/predictive_models.py** 
   - Clase PredictiveModels
   - 3 modelos implementados:
     * Linear Regression
     * Random Forest
     * SARIMA
   - Métricas de evaluación

#### 6. **utils/visualization_utils.py** 
   - 10+ funciones de visualización
   - Gráficos con Plotly
   - Personalización de estilos

#### 7. **utils/__init__.py**
   - Archivo de inicialización del paquete

###  DOCUMENTACIÓN

#### 8. **README.md** 
   - Documentación completa del proyecto
   - Instrucciones de instalación
   - Características del dashboard
   - Solución de problemas
   - Guía de uso

#### 9. **QUICKSTART.md** 
   - Guía de inicio rápido
   - 3 comandos para ejecutar
   - Solución de problemas comunes

#### 10. **RESUMEN_EJECUTIVO.md**
   - Resumen ejecutivo del proyecto
   - Requisitos cumplidos
   - Características destacadas
   - Evaluación y criterios

#### 11. **ARQUITECTURA.md** 
   - Diagrama de arquitectura
   - Flujo de datos
   - Módulos del sistema
   - Optimizaciones

#### 12. **Reporte_Dashboard_Hidrocarburos.pdf** 
   - Reporte académico completo
   - Decisiones de diseño
   - Justificación de paleta de colores
   - Planificación y tareas
   - Bosquejo de diseño

###  INSTALACIÓN Y EJECUCIÓN

#### 13. **requirements.txt** (165 bytes)
   - Dependencias del proyecto
   - Versiones específicas
   - Para: `pip install -r requirements.txt`

#### 14. **setup.sh** (2.4 KB) - Linux/macOS
   - Script de instalación automática
   - Crea entorno virtual
   - Instala dependencias
   - Ejecutar: `./setup.sh`

#### 15. **setup.bat** (2.3 KB) - Windows
   - Script de instalación para Windows
   - Misma funcionalidad que setup.sh
   - Ejecutar: `setup.bat`

#### 16. **run.sh** (649 bytes) - Linux/macOS
   - Script para ejecutar el dashboard
   - Activa entorno y corre app
   - Ejecutar: `./run.sh`

#### 17. **run.bat** (666 bytes) - Windows
   - Script para ejecutar en Windows
   - Misma funcionalidad que run.sh
   - Ejecutar: `run.bat`

###  DATOS

#### 18. **data/Estadisticas_historicas_comercializacion.xlsx** (341 KB)
   - Datos principales del proyecto
   - Hojas: IMPORTACION, CONSUMO
   - Período: 2000-2024
   - 300+ registros mensuales

#### 19. **data/IMPORTACION-HIDROCARBUROS-VOLUMEN-2025-05.xlsx** (46 KB)
   - Datos adicionales de importación
   - Año 2025
   - Datos de Mayo

###  CONFIGURACIÓN

#### 20. **.gitignore** 
   - Archivos a ignorar en Git
   - Python, IDEs, OS
   - Entorno virtual

---



##  INICIO RÁPIDO EN 3 PASOS


### Paso 1: Instalar
```bash
# Linux/Mac
./setup.sh

# Windows
setup.bat
```

### Paso 2: Ejecutar
```bash
# Linux/Mac
./run.sh

# Windows
run.bat
```

**¡Listo! Abre http://localhost:8501 en tu navegador **

---

##  ESTADÍSTICAS DEL PROYECTO


### Visualizaciones
- **Total de visualizaciones**: 10
- **Tipos de gráficos**: 8 diferentes
- **Gráficos enlazados**: 3+

### Modelos
- **Modelos implementados**: 3
- **Series analizadas**: 6
- **Modelos entrenados total**: 18
- **Métricas calculadas**: 3 (MAE, MSE, R²)

### Documentación
- **Archivos de documentación**: 5

---

##  EVALUACIÓN - CHECKLIST

### Diseño y UX (30 puntos)
-  Paleta de colores seleccionada y justificada
-  Aplicación intuitiva y fácil de usar
-  Diseño profesional para directivos
-  Principios de HCI y UX aplicados

### Funcionalidad (50 puntos)
-  Exploración de datos con gráficos adecuados
-  3 modelos predictivos/clasificación
-  Gráficos enlazados funcionando
-  Niveles de detalle ajustables
-  Comparación de modelos con selección
-  Mínimo 8 visualizaciones (10 implementadas)

### Calidad Técnica (20 puntos)
-  Aplicación funciona sin errores
-  Código bien organizado
-  Interactividad completa
-  Documentación exhaustiva

---

##  SOPORTE

### Archivos de Ayuda
- **README.md**: Documentación completa
- **QUICKSTART.md**: Inicio rápido
- **RESUMEN_EJECUTIVO.md**: Overview general

### Sección de Problemas
Ver "Solución de Problemas" en **README.md**

---



##  ESTRUCTURA COMPLETA

```
hydrocarbon_dashboard/
├── 
│   ├── app.py                          
│   ├── config.py                       
│   └── generate_report.py              
│
├── 
│   └── utils/
│       ├── __init__.py
│       ├── data_loader.py
│       ├── predictive_models.py
│       └── visualization_utils.py
│
├── 
│   ├── README.md                       
│   ├── QUICKSTART.md                   
│   ├── RESUMEN_EJECUTIVO.md           
│   ├── ARQUITECTURA.md                
│   ├── Reporte_Dashboard_Hidrocarburos.pdf  
│   └── INDEX.md                       
│
├── 
│   ├── requirements.txt
│   ├── setup.sh                       (Linux/Mac)
│   ├── setup.bat                      (Windows)
│   ├── run.sh                         (Linux/Mac)
│   └── run.bat                        (Windows)
│
├── 
│   └── data/
│       ├── Estadisticas_historicas_comercializacion.xlsx
│       └── IMPORTACION-HIDROCARBUROS-VOLUMEN-2025-05.xlsx
│
└──  CONFIGURACIÓN
    └── .gitignore
```

---

##  CARACTERÍSTICAS DESTACADAS

###  Interfaz
- Diseño profesional y limpio
- Paleta de colores accesible
- Navegación intuitiva
- Responsive

###  Visualizaciones
- 10 tipos diferentes
- Todas interactivas
- Gráficos enlazados
- Exportables

###  Modelos
- 3 modelos diferentes
- Métricas completas
- Comparación visual
- Predicciones precisas

###  Código
- Modular y organizado
- Bien documentado
- Optimizado con caching
- Fácil de mantener

---
