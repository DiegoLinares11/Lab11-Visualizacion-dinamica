"""
Utilidades para crear visualizaciones con Plotly
"""
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from config import COLORS

def create_time_series_plot(df, columns, title, tipo='importacion'):
    """Crea gráfico de serie temporal interactivo"""
    fig = go.Figure()
    
    colors_map = {
        'Gasolina regular': COLORS['gasolina_regular'],
        'Gasolina superior': COLORS['gasolina_superior'],
        'Diesel alto azufre': COLORS['diesel']
    }
    
    for col in columns:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df[col],
            name=col,
            mode='lines',
            line=dict(color=colors_map.get(col, COLORS['primary']), width=2),
            hovertemplate='<b>%{x|%Y-%m}</b><br>Valor: %{y:,.0f}<extra></extra>'
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Fecha',
        yaxis_title='Volumen (Barriles)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def create_comparison_plot(df_imp, df_cons, producto):
    """Crea gráfico comparativo de importación vs consumo"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_imp.index,
        y=df_imp[producto],
        name=f'Importación',
        mode='lines',
        line=dict(color=COLORS['primary'], width=2),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=df_cons.index,
        y=df_cons[producto],
        name=f'Consumo',
        mode='lines',
        line=dict(color=COLORS['secondary'], width=2),
        fill='tozeroy'
    ))
    
    fig.update_layout(
        title=f'Comparación: {producto}',
        xaxis_title='Fecha',
        yaxis_title='Volumen (Barriles)',
        hovermode='x unified',
        template='plotly_white',
        height=450,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_yearly_bar_chart(df_yearly, tipo='importacion'):
    """Crea gráfico de barras agrupadas por año"""
    fig = go.Figure()
    
    colors = [COLORS['gasolina_regular'], COLORS['gasolina_superior'], COLORS['diesel']]
    
    for i, col in enumerate(df_yearly.columns):
        fig.add_trace(go.Bar(
            x=df_yearly.index,
            y=df_yearly[col],
            name=col,
            marker_color=colors[i]
        ))
    
    fig.update_layout(
        title=f'Volumen Anual - {tipo.capitalize()}',
        xaxis_title='Año',
        yaxis_title='Volumen Total (Barriles)',
        barmode='group',
        template='plotly_white',
        height=450,
        hovermode='x unified'
    )
    
    return fig

def create_monthly_pattern(df_monthly, tipo='importacion'):
    """Crea gráfico de patrones mensuales"""
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
             'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    fig = go.Figure()
    
    colors = [COLORS['gasolina_regular'], COLORS['gasolina_superior'], COLORS['diesel']]
    
    for i, col in enumerate(df_monthly.columns):
        fig.add_trace(go.Scatter(
            x=meses,
            y=df_monthly[col].values,
            name=col,
            mode='lines+markers',
            line=dict(color=colors[i], width=3),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title=f'Patrón Mensual Promedio - {tipo.capitalize()}',
        xaxis_title='Mes',
        yaxis_title='Volumen Promedio (Barriles)',
        template='plotly_white',
        height=450,
        hovermode='x unified'
    )
    
    return fig

def create_distribution_plot(df, producto):
    """Crea gráfico de distribución (histograma + boxplot)"""
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Distribución', 'Box Plot'),
        column_widths=[0.7, 0.3]
    )
    
    # Histograma
    fig.add_trace(
        go.Histogram(
            x=df[producto],
            nbinsx=30,
            name='Distribución',
            marker_color=COLORS['primary'],
            showlegend=False
        ),
        row=1, col=1
    )
    
    # Boxplot
    fig.add_trace(
        go.Box(
            y=df[producto],
            name='',
            marker_color=COLORS['secondary'],
            showlegend=False
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        title=f'Análisis de Distribución - {producto}',
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    fig.update_xaxes(title_text="Volumen (Barriles)", row=1, col=1)
    fig.update_yaxes(title_text="Frecuencia", row=1, col=1)
    fig.update_yaxes(title_text="Volumen (Barriles)", row=1, col=2)
    
    return fig

def create_correlation_heatmap(df):
    """Crea mapa de calor de correlaciones"""
    corr_matrix = df.corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=corr_matrix.values,
        texttemplate='%{text:.2f}',
        textfont={"size": 12},
        colorbar=dict(title="Correlación")
    ))
    
    fig.update_layout(
        title='Matriz de Correlación',
        template='plotly_white',
        height=400,
        xaxis={'side': 'bottom'}
    )
    
    return fig

def create_prediction_plot(predictions, serie_nombre, modelo_nombre):
    """Crea gráfico de predicciones vs valores reales"""
    if predictions is None:
        return None
    
    dates = predictions['dates']
    split_idx = len(predictions['y_train'])
    
    fig = go.Figure()
    
    # Datos reales - Train
    fig.add_trace(go.Scatter(
        x=dates[:split_idx],
        y=predictions['y_train'],
        name='Real (Train)',
        mode='lines',
        line=dict(color=COLORS['text_light'], width=2)
    ))
    
    # Datos reales - Test
    fig.add_trace(go.Scatter(
        x=dates[split_idx:],
        y=predictions['y_test'],
        name='Real (Test)',
        mode='lines',
        line=dict(color=COLORS['text'], width=2)
    ))
    
    # Predicciones - Train
    fig.add_trace(go.Scatter(
        x=dates[:split_idx],
        y=predictions['train'],
        name='Predicción (Train)',
        mode='lines',
        line=dict(color=COLORS['primary'], width=2, dash='dash')
    ))
    
    # Predicciones - Test
    fig.add_trace(go.Scatter(
        x=dates[split_idx:],
        y=predictions['test'],
        name='Predicción (Test)',
        mode='lines',
        line=dict(color=COLORS['accent'], width=2)
    ))
    
    fig.update_layout(
        title=f'Predicciones: {modelo_nombre} - {serie_nombre}',
        xaxis_title='Fecha',
        yaxis_title='Volumen (Barriles)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_metrics_comparison_plot(df_metrics):
    """Crea gráfico comparativo de métricas de modelos"""
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=('MAE (Test)', 'MSE (Test)', 'R² (Test)'),
        specs=[[{'type': 'bar'}, {'type': 'bar'}, {'type': 'bar'}]]
    )
    
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent']]
    
    # MAE
    fig.add_trace(
        go.Bar(
            x=df_metrics['Modelo'],
            y=df_metrics['MAE (Test)'],
            marker_color=colors,
            showlegend=False,
            text=df_metrics['MAE (Test)'].round(2),
            textposition='auto'
        ),
        row=1, col=1
    )
    
    # MSE
    fig.add_trace(
        go.Bar(
            x=df_metrics['Modelo'],
            y=df_metrics['MSE (Test)'],
            marker_color=colors,
            showlegend=False,
            text=df_metrics['MSE (Test)'].round(2),
            textposition='auto'
        ),
        row=1, col=2
    )
    
    # R²
    fig.add_trace(
        go.Bar(
            x=df_metrics['Modelo'],
            y=df_metrics['R² (Test)'],
            marker_color=colors,
            showlegend=False,
            text=df_metrics['R² (Test)'].round(3),
            textposition='auto'
        ),
        row=1, col=3
    )
    
    fig.update_layout(
        title='Comparación de Métricas de Modelos',
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    fig.update_yaxes(title_text="Valor", row=1, col=1)
    fig.update_yaxes(title_text="Valor", row=1, col=2)
    fig.update_yaxes(title_text="Valor", row=1, col=3)
    
    return fig

def create_scatter_actual_vs_predicted(predictions, modelo_nombre):
    """Crea scatter plot de valores reales vs predichos"""
    if predictions is None:
        return None
    
    # Combinar train y test
    y_true = np.concatenate([predictions['y_train'], predictions['y_test']])
    y_pred = np.concatenate([predictions['train'], predictions['test']])
    
    # Crear línea perfecta
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    perfect_line = [min_val, max_val]
    
    fig = go.Figure()
    
    # Scatter
    fig.add_trace(go.Scatter(
        x=y_true,
        y=y_pred,
        mode='markers',
        name='Predicciones',
        marker=dict(
            color=COLORS['primary'],
            size=8,
            opacity=0.6,
            line=dict(color='white', width=1)
        ),
        hovertemplate='Real: %{x:.0f}<br>Predicho: %{y:.0f}<extra></extra>'
    ))
    
    # Línea perfecta
    fig.add_trace(go.Scatter(
        x=perfect_line,
        y=perfect_line,
        mode='lines',
        name='Predicción Perfecta',
        line=dict(color=COLORS['warning'], width=2, dash='dash')
    ))
    
    fig.update_layout(
        title=f'Real vs Predicho - {modelo_nombre}',
        xaxis_title='Valores Reales',
        yaxis_title='Valores Predichos',
        template='plotly_white',
        height=450,
        hovermode='closest'
    )
    
    return fig
