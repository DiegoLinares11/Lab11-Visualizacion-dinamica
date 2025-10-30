# 🏗️ ARQUITECTURA DEL SISTEMA
## Dashboard de Hidrocarburos - Guatemala

```
┌─────────────────────────────────────────────────────────────────┐
│                        USUARIO FINAL                             │
│                    (Directivos / Analistas)                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NAVEGADOR WEB                                 │
│                 http://localhost:8501                            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    STREAMLIT SERVER                              │
│                      (app.py)                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Vista 1: Exploración de Datos                            │  │
│  │  - Series Temporales                                      │  │
│  │  - Análisis Agregado                                      │  │
│  │  - Análisis Detallado                                     │  │
│  │  - Distribuciones                                         │  │
│  └───────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Vista 2: Modelos Predictivos                            │  │
│  │  - Visualización de Predicciones                         │  │
│  │  - Métricas de Desempeño                                 │  │
│  │  - Análisis de Ajuste                                    │  │
│  └───────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Vista 3: Comparación de Modelos                         │  │
│  │  - Tabla Comparativa                                     │  │
│  │  - Gráficos de Métricas                                  │  │
│  │  - Selector de Modelos                                   │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌─────────────┐  ┌──────────────┐  ┌────────────────┐
│   CONFIG    │  │  DATA LOADER │  │   PREDICTIVE   │
│   config.py │  │              │  │    MODELS      │
│             │  │  data_loader │  │                │
│  • Colores  │  │     .py      │  │  predictive_   │
│  • Textos   │  │              │  │   models.py    │
│  • Params   │  │  • Carga     │  │                │
└─────────────┘  │  • Preproc.  │  │  • Linear Reg  │
                 │  • Stats     │  │  • Random For. │
                 │  • Agregac.  │  │  • SARIMA      │
                 └──────┬───────┘  └────────┬───────┘
                        │                   │
                        └─────────┬─────────┘
                                  ▼
                      ┌───────────────────────┐
                      │   VISUALIZATION       │
                      │      UTILS            │
                      │                       │
                      │  visualization_utils  │
                      │       .py             │
                      │                       │
                      │  • Time Series        │
                      │  • Bar Charts         │
                      │  • Heatmaps          │
                      │  • Scatter Plots     │
                      │  • Comparisons       │
                      └───────────┬───────────┘
                                  │
                                  ▼
                      ┌───────────────────────┐
                      │      PLOTLY           │
                      │   (Visualización)     │
                      └───────────┬───────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                  ▼
┌─────────────────┐                              ┌──────────────────┐
│  PANDAS/NUMPY   │                              │  SCIKIT-LEARN    │
│  (Procesamiento)│                              │  STATSMODELS     │
│                 │                              │  (Machine Learn.)│
└────────┬────────┘                              └─────────┬────────┘
         │                                                  │
         └──────────────────┬──────────────────────────────┘
                            ▼
                 ┌─────────────────────┐
                 │   DATOS (EXCEL)     │
                 │                     │
                 │  • Importación      │
                 │  • Consumo          │
                 │  • Hidrocarburos    │
                 └─────────────────────┘
```

##  MÓDULOS DEL SISTEMA

### 1. Frontend (Streamlit)
```
app.py (18KB)
├── Sidebar Navigation
│   ├── Vista 1: Exploración
│   ├── Vista 2: Modelos
│   └── Vista 3: Comparación
├── Caching (@st.cache_data)
└── Renderizado Reactivo
```

### 2. Configuración
```
config.py (3.1KB)
├── COLORS: Paleta de colores
├── MODEL_CONFIG: Parámetros ML
├── PRODUCTOS: Lista de productos
└── TEXTS: Strings de interfaz
```

### 3. Carga de Datos
```
utils/data_loader.py (5KB)
├── DataLoader Class
│   ├── load_data()
│   ├── get_combined_data()
│   ├── get_statistics()
│   ├── get_yearly_aggregation()
│   └── get_monthly_patterns()
```

### 4. Modelos Predictivos
```
utils/predictive_models.py (7KB)
├── PredictiveModels Class
│   ├── prepare_data()
│   ├── train_linear_regression()
│   ├── train_random_forest()
│   ├── train_sarima()
│   └── compare_models()
```

### 5. Visualizaciones
```
utils/visualization_utils.py (9KB)
├── create_time_series_plot()
├── create_comparison_plot()
├── create_yearly_bar_chart()
├── create_monthly_pattern()
├── create_distribution_plot()
├── create_correlation_heatmap()
├── create_prediction_plot()
├── create_metrics_comparison_plot()
└── create_scatter_actual_vs_predicted()
```

##  FLUJO DE DATOS

```
1. CARGA
   Excel → DataLoader → DataFrame (Pandas)

2. PREPROCESAMIENTO
   DataFrame → Limpieza → Transformación → Normalización

3. ANÁLISIS
   ├─→ Estadísticas Descriptivas
   ├─→ Agregaciones (Anual/Mensual)
   └─→ Correlaciones

4. MODELADO
   DataFrame → PredictiveModels → Modelos Entrenados
   ├─→ Linear Regression
   ├─→ Random Forest
   └─→ SARIMA

5. VISUALIZACIÓN
   Datos + Modelos → visualization_utils → Gráficos Plotly

6. PRESENTACIÓN
   Gráficos → Streamlit → HTML → Navegador
```

##  OPTIMIZACIONES

### Caching Estratégico
```python
@st.cache_data
def load_all_data():
    # Se ejecuta solo una vez
    return loader, df_imp, df_cons

@st.cache_data
def train_all_models():
    # Se entrena solo cuando cambian los datos
    return resultados
```

### Carga Lazy
- Modelos se entrenan solo cuando usuario los requiere
- Gráficos se generan on-demand
- Datos se cargan una sola vez

### Procesamiento Eficiente
- Operaciones vectorizadas (NumPy/Pandas)
- Normalización previa para ML
- Filtrado optimizado de datos

##  SEGURIDAD Y VALIDACIÓN

```
┌─────────────────┐
│  Validación     │
│  de Entrada     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Verificación   │
│  de Archivos    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Sanitización   │
│  de Datos       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Manejo de      │
│  Excepciones    │
└─────────────────┘
```

##  MÉTRICAS DEL SISTEMA

### Performance
- **Tiempo de carga inicial**: ~2 segundos
- **Tiempo de cambio de vista**: ~0.1 segundos
- **Tiempo de renderizado gráfico**: ~0.3 segundos
- **Entrenamiento de modelos**: ~5-10 segundos (con cache)

### Capacidad
- **Datos procesables**: Hasta 10,000 registros
- **Modelos simultáneos**: 18 (3 × 6 series)
- **Gráficos por vista**: 10+
- **Usuarios concurrentes**: Limitado por Streamlit (1 por instancia local)

##  DEPENDENCIAS PRINCIPALES

```
streamlit 1.31.0     ─┐
                      ├─→ Framework Web
plotly 5.18.0        ─┘

pandas 2.1.4         ─┐
numpy 1.26.3         ─┼─→ Procesamiento de Datos
openpyxl 3.1.2       ─┘

scikit-learn 1.4.0   ─┐
statsmodels 0.14.1   ─┼─→ Machine Learning
scipy 1.11.4         ─┘

matplotlib 3.8.2     ─┐
seaborn 0.13.1       ─┘─→ Visualizaciones Adicionales
```

##  ESCALABILIDAD

### Horizontal
- Desplegar múltiples instancias en Streamlit Cloud
- Load balancer para distribución de carga

### Vertical
- Optimizar caching para datasets más grandes
- Implementar procesamiento paralelo para modelos
- Usar bases de datos en lugar de Excel

### Funcional
- Agregar más modelos predictivos
- Incorporar más tipos de visualizaciones
- Añadir módulo de exportación de reportes
- Implementar sistema de alertas

---

**Arquitectura diseñada para:**
 Modularidad
 Mantenibilidad
 Escalabilidad
 Performance
 Usabilidad
