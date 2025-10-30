#  Dashboard Interactivo de Hidrocarburos - Guatemala

Dashboard interactivo para análisis de datos de importación y consumo de hidrocarburos en Guatemala, con modelos predictivos integrados.

**Laboratorio 11 - Data Science**  
Universidad del Valle de Guatemala

---

##  Contenido del Proyecto

```
hydrocarbon_dashboard/
├── app.py                          # Aplicación principal de Streamlit
├── config.py                       # Configuración y paleta de colores
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── data/                           # Carpeta con datasets
│   ├── Estadisticas_historicas_comercializacion.xlsx
│   └── IMPORTACION-HIDROCARBUROS-VOLUMEN-2025-05.xlsx
└── utils/                          # Módulos auxiliares
    ├── __init__.py
    ├── data_loader.py              # Carga y preprocesamiento de datos
    ├── predictive_models.py        # Modelos de predicción
    └── visualization_utils.py      # Funciones de visualización
```

---

##  Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar o Descargar el Proyecto

```bash

git clone https://github.com/DiegoLinares11/Lab11-Visualizacion-dinamica 


```

### Paso 2: Crear Entorno Virtual (Recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Nota:** Si tienes problemas con alguna librería específica, instálalas una por una:

```bash
pip install streamlit pandas numpy plotly scikit-learn statsmodels matplotlib seaborn openpyxl scipy
```

---

## ▶ Cómo Ejecutar el Dashboard

### Ejecución Local

1. Asegúrate de estar en la carpeta del proyecto:
   ```bash
   cd lab11
   ```

2. Ejecuta el dashboard:
   ```bash
   streamlit run app.py
   ```

3. El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

4. Si no se abre automáticamente, copia y pega la URL que aparece en la terminal

### Comandos Adicionales

```bash
# Ejecutar en un puerto específico
streamlit run app.py --server.port 8502

# Ejecutar con recarga automática
streamlit run app.py --server.runOnSave true

# Ver ayuda de Streamlit
streamlit --help
```

---

##  Características del Dashboard

### 1. **Exploración de Datos** 
- **Series Temporales Interactivas**: Visualiza importación y consumo por producto
- **Análisis Agregado**: Tendencias anuales y patrones mensuales
- **Análisis Detallado**: Estadísticas descriptivas y correlaciones
- **Distribuciones**: Histogramas y box plots

### 2. **Modelos Predictivos** 
- **Linear Regression**: Modelo de regresión lineal
- **Random Forest**: Modelo de ensamble con árboles de decisión
- **SARIMA**: Modelo estadístico para series de tiempo con estacionalidad
- Visualización de predicciones vs valores reales
- Análisis de ajuste del modelo

### 3. **Comparación de Modelos** 
- Tabla comparativa de métricas (MAE, MSE, R²)
- Visualización gráfica de comparaciones
- Identificación del mejor modelo por métrica
- Comparación visual de predicciones

### Visualizaciones Incluidas (8+)
1.  Series temporales por producto
2.  Comparación importación vs consumo
3.  Volumen anual (barras agrupadas)
4.  Patrones mensuales promedio
5.  Matriz de correlación (heatmap)
6.  Distribuciones (histograma + boxplot)
7.  Predicciones vs valores reales
8.  Scatter plot real vs predicho
9.  Comparación de métricas de modelos

### Características de Interactividad
-  **Gráficos Enlazados**: Cambios en una visualización afectan otras
-  **Filtros Dinámicos**: Selección de productos, tipos de datos y modelos
-  **Zoom y Pan**: Todas las gráficas permiten zoom y navegación
-  **Exportación**: Descarga gráficos como PNG
-  **Tooltips**: Información detallada al pasar el cursor

---

##  Paleta de Colores

### Justificación
La paleta fue seleccionada siguiendo principios de diseño corporativo:

- **Azul (#1f77b4)**: Confianza y profesionalismo (importación)
- **Naranja (#ff7f0e)**: Energía y acción (consumo)
- **Verde (#2ca02c)**: Crecimiento y éxito (predicciones)
- **Rojo (#d62728)**: Alertas y valores críticos
- **Grises neutros**: Facilitan lectura y reducen fatiga visual

 Cumple con estándares WCAG 2.1 de accesibilidad  
 Adecuada para daltonismo (deuteranopía y protanopía)

---

##  Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
# Verifica que todas las dependencias estén instaladas
pip install -r requirements.txt

# O instala el paquete faltante específicamente
pip install <nombre_del_paquete>
```

### Error: "No module named 'config'"
```bash
# Asegúrate de estar en la carpeta correcta
python -c "import sys; print(sys.path)"
```

### Error al cargar datos Excel
```bash
# Instala openpyxl si no está instalado
pip install openpyxl

# Verifica que los archivos .xlsx estén en la carpeta data/
ls data/
```

### El dashboard no se abre automáticamente
- Copia manualmente la URL de la terminal (usualmente `http://localhost:8501`)
- Verifica que no haya otro proceso usando el puerto 8501

### Warnings de statsmodels
- Son normales y no afectan la funcionalidad
- Se pueden ignorar o silenciar con `warnings.filterwarnings('ignore')`

---

##  Dependencias del Proyecto

| Librería | Versión | Propósito |
|----------|---------|-----------|
| streamlit | 1.31.0 | Framework del dashboard |
| pandas | 2.1.4 | Manipulación de datos |
| numpy | 1.26.3 | Operaciones numéricas |
| plotly | 5.18.0 | Visualizaciones interactivas |
| scikit-learn | 1.4.0 | Modelos de ML |
| statsmodels | 0.14.1 | Modelo SARIMA |
| matplotlib | 3.8.2 | Visualizaciones estáticas |
| seaborn | 0.13.1 | Visualizaciones estadísticas |
| openpyxl | 3.1.2 | Lectura de archivos Excel |
| scipy | 1.11.4 | Cálculos científicos |

---

##  Modelos Implementados

### 1. Linear Regression
- **Tipo**: Modelo de regresión lineal simple
- **Características**: Usa 12 períodos anteriores (lookback=12)
- **Ventajas**: Simple, rápido, interpretable
- **Métricas**: MAE, MSE, R²

### 2. Random Forest
- **Tipo**: Modelo de ensamble con árboles de decisión
- **Parámetros**: 100 árboles, max_depth=10
- **Ventajas**: Captura relaciones no lineales, robusto
- **Métricas**: MAE, MSE, R²

### 3. SARIMA
- **Tipo**: Modelo estadístico para series temporales
- **Orden**: (1, 1, 1) con estacionalidad (1, 1, 1, 12)
- **Ventajas**: Diseñado específicamente para series de tiempo
- **Métricas**: MAE, MSE, R²

### Interpretación de Métricas
- **MAE** (Mean Absolute Error): Error absoluto medio, menor es mejor
- **MSE** (Mean Squared Error): Error cuadrático medio, menor es mejor
- **R²** (Coefficient of Determination): Proporción de varianza explicada (0-1), mayor es mejor
- **RMSE** (Root Mean Squared Error): Raíz del MSE, en las mismas unidades que los datos

---

##  Despliegue en la Nube (Opcional)

### Streamlit Cloud

1. Crea una cuenta en [streamlit.io/cloud](https://streamlit.io/cloud)
2. Conecta tu repositorio de GitHub
3. Selecciona la rama y el archivo `app.py`
4. Despliega

### Requisitos para despliegue
- Repositorio público en GitHub
- Archivo `requirements.txt` en la raíz
- Datos en carpeta accesible o usar secrets de Streamlit


---

##  Soporte

Si encuentras problemas o tienes preguntas:

1. Revisa la sección de Solución de Problemas
2. Verifica que todas las dependencias estén instaladas
3. Consulta la documentación oficial de [Streamlit](https://docs.streamlit.io/)


---

**¡Disfruta explorando los datos de hidrocarburos de Guatemala!**
