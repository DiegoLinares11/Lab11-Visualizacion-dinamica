"""
Dashboard Interactivo de Hidrocarburos - Guatemala
Laboratorio 11 - Data Science
"""
import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Añadir path de utilidades
sys.path.append(str(Path(__file__).parent))

from config import DASHBOARD_CONFIG, TEXTS, COLORS, COLOR_JUSTIFICATION
from utils.data_loader import DataLoader
from utils.predictive_models import PredictiveModels
from utils.visualization_utils import *

# Configuración de página
st.set_page_config(**DASHBOARD_CONFIG)

# CSS personalizado
st.markdown(f"""
    <style>
    .main {{
        background-color: {COLORS['background']};
    }}
    .stMetric {{
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    h1, h2, h3 {{
        color: {COLORS['text']};
    }}
    .info-box {{
        background-color: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid {COLORS['primary']};
        margin: 20px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# Cache de datos
@st.cache_data
def load_all_data():
    """Carga todos los datos necesarios"""
    loader = DataLoader()
    df_imp, df_cons = loader.load_data()
    return loader, df_imp, df_cons

@st.cache_data
def train_all_models(df_imp, df_cons):
    """Entrena todos los modelos para todas las series"""
    model_trainer = PredictiveModels(test_size=0.2)
    
    productos = ['Gasolina regular', 'Gasolina superior', 'Diesel alto azufre']
    tipos = ['Importación', 'Consumo']
    
    resultados = {}
    
    for tipo in tipos:
        df = df_imp if tipo == 'Importación' else df_cons
        for producto in productos:
            serie_nombre = f'{tipo} {producto}'
            with st.spinner(f'Entrenando modelos para {serie_nombre}...'):
                df_metrics = model_trainer.compare_models(df[producto], serie_nombre)
                resultados[serie_nombre] = {
                    'metrics': df_metrics,
                    'trainer': model_trainer
                }
    
    return resultados

# Header principal
st.markdown(f"# {TEXTS['main_title']}")
st.markdown(f"### {TEXTS['subtitle']}")

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/1f77b4/ffffff?text=Hidrocarburos+GT", 
             use_container_width=True)
    
    st.markdown("##  Configuración")
    
    # Selección de vista
    vista = st.radio(
        "Selecciona la vista:",
        [" Exploración de Datos", " Modelos Predictivos", " Comparación de Modelos"]
    )
    
    st.markdown("---")
    
    # Información
    with st.expander(" Acerca del Dashboard"):
        st.markdown(TEXTS['about'])
        st.caption(TEXTS['data_source'])
    
    with st.expander(" Paleta de Colores"):
        st.markdown(COLOR_JUSTIFICATION)

# Cargar datos
loader, df_imp, df_cons = load_all_data()

# ============================================================================
# VISTA 1: EXPLORACIÓN DE DATOS
# ============================================================================
if vista == " Exploración de Datos":
    st.markdown("##  Exploración Interactiva de Datos")
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs([
        " Series Temporales", 
        " Análisis Agregado",
        " Análisis Detallado",
        " Distribuciones"
    ])
    
    # TAB 1: Series Temporales
    with tab1:
        st.markdown("### Series Temporales por Producto")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tipo_dato = st.selectbox(
                "Tipo de dato:",
                ["Importación", "Consumo", "Comparación"]
            )
        
        with col2:
            producto_sel = st.selectbox(
                "Producto:",
                ["Gasolina regular", "Gasolina superior", "Diesel alto azufre"]
            )
        
        # Gráfico según selección
        if tipo_dato == "Comparación":
            st.plotly_chart(
                create_comparison_plot(df_imp, df_cons, producto_sel),
                use_container_width=True
            )
        else:
            df_selected = df_imp if tipo_dato == "Importación" else df_cons
            fig = create_time_series_plot(
                df_selected, 
                [producto_sel], 
                f'{tipo_dato} de {producto_sel}'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Gráfico enlazado: Todos los productos
        st.markdown("####  Vista Enlazada: Todos los Productos")
        df_display = df_imp if tipo_dato != "Consumo" else df_cons
        fig_all = create_time_series_plot(
            df_display,
            df_display.columns.tolist(),
            f'{tipo_dato} - Todos los Productos',
            tipo=tipo_dato.lower()
        )
        st.plotly_chart(fig_all, use_container_width=True)
    
    # TAB 2: Análisis Agregado
    with tab2:
        st.markdown("### Análisis de Tendencias Anuales y Mensuales")
        
        tipo_agregado = st.radio(
            "Tipo de agregación:",
            ["Anual", "Mensual (Patrones)"],
            horizontal=True
        )
        
        col1, col2 = st.columns(2)
        
        if tipo_agregado == "Anual":
            yearly_data = loader.get_yearly_aggregation()
            
            with col1:
                st.markdown("#### Importación Anual")
                fig_imp = create_yearly_bar_chart(yearly_data['importacion'], 'importacion')
                st.plotly_chart(fig_imp, use_container_width=True)
            
            with col2:
                st.markdown("#### Consumo Anual")
                fig_cons = create_yearly_bar_chart(yearly_data['consumo'], 'consumo')
                st.plotly_chart(fig_cons, use_container_width=True)
        
        else:  # Mensual
            monthly_data = loader.get_monthly_patterns()
            
            with col1:
                st.markdown("#### Patrón Mensual - Importación")
                fig_imp = create_monthly_pattern(monthly_data['importacion'], 'importacion')
                st.plotly_chart(fig_imp, use_container_width=True)
            
            with col2:
                st.markdown("#### Patrón Mensual - Consumo")
                fig_cons = create_monthly_pattern(monthly_data['consumo'], 'consumo')
                st.plotly_chart(fig_cons, use_container_width=True)
    
    # TAB 3: Análisis Detallado
    with tab3:
        st.markdown("### Análisis Estadístico Detallado")
        
        tipo_detalle = st.selectbox(
            "Selecciona el tipo de dato:",
            ["Importación", "Consumo"],
            key="detalle"
        )
        
        df_detalle = df_imp if tipo_detalle == "Importación" else df_cons
        
        # Estadísticas descriptivas
        st.markdown("####  Estadísticas Descriptivas")
        st.dataframe(df_detalle.describe().T, use_container_width=True)
        
        # Matriz de correlación
        st.markdown("####  Matriz de Correlación")
        fig_corr = create_correlation_heatmap(df_detalle)
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Información del rango de datos
        date_info = loader.get_date_range()
        info = date_info['importacion'] if tipo_detalle == "Importación" else date_info['consumo']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Fecha Inicio", info['inicio'].strftime('%Y-%m'))
        with col2:
            st.metric("Fecha Fin", info['fin'].strftime('%Y-%m'))
        with col3:
            st.metric("Total Registros", info['registros'])
    
    # TAB 4: Distribuciones
    with tab4:
        st.markdown("### Análisis de Distribuciones")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tipo_dist = st.selectbox(
                "Tipo de dato:",
                ["Importación", "Consumo"],
                key="dist"
            )
        
        with col2:
            producto_dist = st.selectbox(
                "Producto:",
                ["Gasolina regular", "Gasolina superior", "Diesel alto azufre"],
                key="prod_dist"
            )
        
        df_dist = df_imp if tipo_dist == "Importación" else df_cons
        
        fig_dist = create_distribution_plot(df_dist, producto_dist)
        st.plotly_chart(fig_dist, use_container_width=True)
        
        # Estadísticas adicionales
        st.markdown("####  Estadísticas del Producto")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Media", f"{df_dist[producto_dist].mean():,.0f}")
        with col2:
            st.metric("Mediana", f"{df_dist[producto_dist].median():,.0f}")
        with col3:
            st.metric("Desv. Estándar", f"{df_dist[producto_dist].std():,.0f}")
        with col4:
            st.metric("Coef. Variación", f"{(df_dist[producto_dist].std()/df_dist[producto_dist].mean()*100):.1f}%")

# ============================================================================
# VISTA 2: MODELOS PREDICTIVOS
# ============================================================================
elif vista == " Modelos Predictivos":
    st.markdown("##  Modelos Predictivos")
    
    st.info("""
     Esta sección permite explorar tres modelos predictivos diferentes:
    - **Linear Regression**: Modelo de regresión lineal simple
    - **Random Forest**: Modelo de ensamble basado en árboles de decisión
    - **SARIMA**: Modelo estadístico para series de tiempo con estacionalidad
    """)
    
    # Selección de serie y modelo
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tipo_pred = st.selectbox("Tipo:", ["Importación", "Consumo"])
    
    with col2:
        producto_pred = st.selectbox(
            "Producto:",
            ["Gasolina regular", "Gasolina superior", "Diesel alto azufre"],
            key="prod_pred"
        )
    
    with col3:
        modelo_pred = st.selectbox(
            "Modelo:",
            ["Linear Regression", "Random Forest", "SARIMA"]
        )
    
    serie_nombre = f'{tipo_pred} {producto_pred}'
    
    # Entrenar modelos (con cache)
    with st.spinner(' Entrenando modelos...'):
        resultados = train_all_models(df_imp, df_cons)
    
    # Obtener resultados
    if serie_nombre in resultados:
        trainer = resultados[serie_nombre]['trainer']
        df_metrics = resultados[serie_nombre]['metrics']
        
        # Obtener predicciones
        predictions = trainer.get_predictions(serie_nombre, modelo_pred)
        
        # Mostrar métricas
        st.markdown(f"###  Métricas del Modelo: {modelo_pred}")
        
        modelo_metrics = df_metrics[df_metrics['Modelo'] == modelo_pred].iloc[0]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("MAE (Test)", f"{modelo_metrics['MAE (Test)']:,.2f}")
        with col2:
            st.metric("MSE (Test)", f"{modelo_metrics['MSE (Test)']:,.2f}")
        with col3:
            st.metric("R² (Test)", f"{modelo_metrics['R² (Test)']:.3f}")
        with col4:
            # Calcular RMSE
            rmse = np.sqrt(modelo_metrics['MSE (Test)'])
            st.metric("RMSE (Test)", f"{rmse:,.2f}")
        
        # Gráfico de predicciones
        st.markdown("### Predicciones vs Valores Reales")
        fig_pred = create_prediction_plot(predictions, serie_nombre, modelo_pred)
        if fig_pred:
            st.plotly_chart(fig_pred, use_container_width=True)
        
        # Gráfico enlazado: Scatter Real vs Predicho
        st.markdown("### Análisis de Ajuste del Modelo")
        col1, col2 = st.columns(2)
        
        with col1:
            fig_scatter = create_scatter_actual_vs_predicted(predictions, modelo_pred)
            if fig_scatter:
                st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            # Tabla de métricas
            st.markdown("#### Métricas Detalladas")
            metrics_display = pd.DataFrame({
                'Métrica': ['MAE', 'MSE', 'R²', 'RMSE'],
                'Train': [
                    modelo_metrics['MAE (Train)'],
                    modelo_metrics['MSE (Train)'],
                    modelo_metrics['R² (Train)'],
                    np.sqrt(modelo_metrics['MSE (Train)'])
                ],
                'Test': [
                    modelo_metrics['MAE (Test)'],
                    modelo_metrics['MSE (Test)'],
                    modelo_metrics['R² (Test)'],
                    np.sqrt(modelo_metrics['MSE (Test)'])
                ]
            })
            st.dataframe(metrics_display, use_container_width=True, hide_index=True)
            
            st.markdown("""
            **Interpretación:**
            - **MAE**: Error absoluto medio
            - **MSE**: Error cuadrático medio
            - **R²**: Coeficiente de determinación (0-1, mayor es mejor)
            - **RMSE**: Raíz del error cuadrático medio
            """)

# ============================================================================
# VISTA 3: COMPARACIÓN DE MODELOS
# ============================================================================
else:  # Comparación de Modelos
    st.markdown("##  Comparación de Modelos")
    
    st.info("""
    🔍 Esta sección permite comparar el desempeño de los tres modelos predictivos
    para diferentes productos y tipos de datos.
    """)
    
    # Selección de serie
    col1, col2 = st.columns(2)
    
    with col1:
        tipo_comp = st.selectbox("Tipo:", ["Importación", "Consumo"], key="tipo_comp")
    
    with col2:
        producto_comp = st.selectbox(
            "Producto:",
            ["Gasolina regular", "Gasolina superior", "Diesel alto azufre"],
            key="prod_comp"
        )
    
    serie_comp = f'{tipo_comp} {producto_comp}'
    
    # Entrenar modelos
    with st.spinner(' Entrenando y comparando modelos...'):
        resultados = train_all_models(df_imp, df_cons)
    
    if serie_comp in resultados:
        df_metrics = resultados[serie_comp]['metrics']
        trainer = resultados[serie_comp]['trainer']
        
        # Tabla comparativa
        st.markdown("###  Tabla Comparativa de Modelos")
        
        # Selector de modelos a comparar
        modelos_disponibles = df_metrics['Modelo'].tolist()
        modelos_seleccionados = st.multiselect(
            "Selecciona los modelos a comparar:",
            modelos_disponibles,
            default=modelos_disponibles
        )
        
        if modelos_seleccionados:
            df_metrics_filtered = df_metrics[df_metrics['Modelo'].isin(modelos_seleccionados)]
            
            # Mostrar tabla
            st.dataframe(
                df_metrics_filtered.style.highlight_min(
                    subset=['MAE (Test)', 'MSE (Test)'],
                    color='lightgreen'
                ).highlight_max(
                    subset=['R² (Test)'],
                    color='lightgreen'
                ),
                use_container_width=True,
                hide_index=True
            )
            
            # Gráfico comparativo
            st.markdown("###  Visualización Comparativa")
            fig_comp = create_metrics_comparison_plot(df_metrics_filtered)
            st.plotly_chart(fig_comp, use_container_width=True)
            
            # Análisis de mejores modelos
            st.markdown("###  Análisis de Rendimiento")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                mejor_mae = df_metrics_filtered.loc[df_metrics_filtered['MAE (Test)'].idxmin()]
                st.success(f"""
                **Mejor MAE**  
                {mejor_mae['Modelo']}  
                MAE: {mejor_mae['MAE (Test)']:.2f}
                """)
            
            with col2:
                mejor_mse = df_metrics_filtered.loc[df_metrics_filtered['MSE (Test)'].idxmin()]
                st.success(f"""
                **Mejor MSE**  
                {mejor_mse['Modelo']}  
                MSE: {mejor_mse['MSE (Test)']:.2f}
                """)
            
            with col3:
                mejor_r2 = df_metrics_filtered.loc[df_metrics_filtered['R² (Test)'].idxmax()]
                st.success(f"""
                **Mejor R²**  
                {mejor_r2['Modelo']}  
                R²: {mejor_r2['R² (Test)']:.3f}
                """)
            
            # Comparación visual de predicciones
            st.markdown("###  Comparación Visual de Predicciones")
            
            modelo_viz = st.selectbox(
                "Selecciona modelo para visualizar:",
                modelos_seleccionados
            )
            
            predictions_viz = trainer.get_predictions(serie_comp, modelo_viz)
            if predictions_viz:
                fig_viz = create_prediction_plot(predictions_viz, serie_comp, modelo_viz)
                st.plotly_chart(fig_viz, use_container_width=True)
        
        else:
            st.warning(" Selecciona al menos un modelo para comparar")

# Footer
st.markdown("---")
st.caption("""
 **Laboratorio 11 - Data Science**  
Universidad del Valle de Guatemala  
Dashboard desarrollado con Streamlit y Plotly
""")
