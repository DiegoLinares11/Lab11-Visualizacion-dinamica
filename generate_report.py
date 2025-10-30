"""
Script para generar el reporte PDF del proyecto
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime

def create_report():
    """Crea el reporte PDF del proyecto"""
    
    # Crear documento
    doc = SimpleDocTemplate(
        "Reporte_Dashboard_Hidrocarburos.pdf",
        pagesize=letter,
        topMargin=1*inch,
        bottomMargin=1*inch,
        leftMargin=1*inch,
        rightMargin=1*inch
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilo personalizado para el título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        textColor=colors.HexColor('#1f77b4'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    # Estilo para subtítulos
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1f77b4'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    # Estilo para subtítulos nivel 2
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=10,
        spaceBefore=10
    )
    
    # Estilo para texto normal
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )
    
    # Lista de estilos
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=6
    )
    
    # Contenido del documento
    story = []
    
    # ===== PORTADA =====
    story.append(Spacer(1, 1*inch))
    
    story.append(Paragraph("DASHBOARD INTERACTIVO DE HIDROCARBUROS", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Análisis de Importación y Consumo en Guatemala", styles['Heading2']))
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph("Laboratorio 11 - Visualización Interactiva", styles['Heading2']))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("CC3066 - Data Science", styles['Normal']))
    story.append(Paragraph("Universidad del Valle de Guatemala", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph(f"Fecha: 30 De Octubre de 2025", styles['Normal']))
    story.append(Spacer(1, 1*inch))
    
    # Autores
    story.append(Paragraph("<b>Autores:</b>", styles['Normal']))
    story.append(Paragraph("Diego Linares - #221256", styles['Normal']))
    story.append(Paragraph("José Prince - #22087", styles['Normal']))
    
    story.append(PageBreak())
    
    # ===== ÍNDICE =====
    story.append(Paragraph("TABLA DE CONTENIDO", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc_data = [
        ["1.", "Resumen Ejecutivo", "3"],
        ["2.", "Selección de Paleta de Colores", "3"],
        ["3.", "Planificación del Proyecto", "4"],
        ["4.", "Diseño del Dashboard", "5"],
        ["5.", "Selección de Herramienta", "6"],
        ["6.", "Arquitectura del Sistema", "7"],
        ["7.", "Modelos Predictivos", "8"],
        ["8.", "Visualizaciones Implementadas", "9"],
        ["9.", "Características de Interactividad", "10"],
        ["10.", "Instrucciones de Uso", "11"]
    ]
    
    toc_table = Table(toc_data, colWidths=[0.5*inch, 4.5*inch, 0.5*inch])
    toc_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(toc_table)
    
    story.append(PageBreak())
    
    # ===== 1. RESUMEN EJECUTIVO =====
    story.append(Paragraph("1. RESUMEN EJECUTIVO", heading_style))
    
    story.append(Paragraph(
        "Este proyecto presenta un dashboard interactivo desarrollado con <b>Streamlit</b> para el "
        "análisis exploratorio y predictivo de datos de importación y consumo de hidrocarburos en Guatemala. "
        "El sistema integra visualizaciones dinámicas enlazadas con tres modelos predictivos (Linear Regression, "
        "Random Forest y SARIMA) para facilitar la toma de decisiones basadas en datos.",
        normal_style
    ))
    
    story.append(Paragraph(
        "El dashboard cumple con todos los requisitos establecidos en el laboratorio, incluyendo más de 8 "
        "visualizaciones interactivas, gráficos enlazados, comparación de modelos predictivos, y una interfaz "
        "intuitiva diseñada bajo principios de HCI y UX.",
        normal_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    # ===== 2. PALETA DE COLORES =====
    story.append(Paragraph("2. SELECCIÓN DE PALETA DE COLORES", heading_style))
    
    story.append(Paragraph("2.1 Paleta Seleccionada", heading2_style))
    
    colors_data = [
        ["Color", "Código Hex", "Uso"],
        ["Azul Principal", "#1f77b4", "Importación, gráficos principales"],
        ["Naranja", "#ff7f0e", "Consumo, acciones"],
        ["Verde", "#2ca02c", "Predicciones positivas, éxito"],
        ["Rojo", "#d62728", "Alertas, errores, valores críticos"],
        ["Azul Medio", "#4a90e2", "Gasolina Regular"],
        ["Azul-Violeta", "#7b68ee", "Gasolina Superior"],
        ["Naranja Cálido", "#ff8c42", "Diesel"],
    ]
    
    colors_table = Table(colors_data, colWidths=[1.5*inch, 1.5*inch, 2.5*inch])
    colors_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    story.append(colors_table)
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("2.2 Justificación", heading2_style))
    
    story.append(Paragraph(
        "La paleta fue seleccionada siguiendo principios de diseño para dashboards corporativos:",
        normal_style
    ))
    
    justification_points = [
        "<b>Azul (#1f77b4)</b>: Color principal que transmite confianza, profesionalismo y estabilidad. "
        "Ideal para datos de importación y análisis serio.",
        
        "<b>Naranja (#ff7f0e)</b>: Color complementario que aporta energía y calidez, perfecto para "
        "representar consumo y acción.",
        
        "<b>Verde (#2ca02c)</b>: Para indicadores positivos y predicciones favorables, asociado con "
        "crecimiento y éxito.",
        
        "<b>Rojo (#d62728)</b>: Reservado para alertas, errores o valores críticos que requieren atención.",
        
        "<b>Grises neutros</b>: Facilitan la lectura y reducen la fatiga visual, permitiendo que los "
        "datos sean el foco principal."
    ]
    
    for point in justification_points:
        story.append(Paragraph(f"• {point}", bullet_style))
    
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph(
        " <b>Esta paleta cumple con:</b>",
        normal_style
    ))
    story.append(Paragraph("• Estándares de accesibilidad WCAG 2.1 para contraste", bullet_style))
    story.append(Paragraph("• Compatibilidad con daltonismo (deuteranopía y protanopía)", bullet_style))
    story.append(Paragraph("• Principios de UX para reducir fatiga visual", bullet_style))
    
    story.append(PageBreak())
    
    # ===== 3. PLANIFICACIÓN =====
    story.append(Paragraph("3. PLANIFICACIÓN DEL PROYECTO", heading_style))
    
    story.append(Paragraph("3.1 Distribución de Tareas", heading2_style))
    
    tasks_data = [
        ["Tarea", "Responsable", "Tiempo"],
        ["Diseño de arquitectura", "Equipo", "2 horas"],
        ["Módulo de carga de datos", "Diego Linares", "3 horas"],
        ["Módulo de modelos predictivos", "José Prince", "4 horas"],
        ["Módulo de visualizaciones", "Diego Linares", "3 horas"],
        ["Dashboard principal (Streamlit)", "José Prince", "5 horas"],
        ["Integración y pruebas", "Equipo", "3 horas"],
        ["Documentación y reporte", "Equipo", "2 horas"],
    ]
    
    tasks_table = Table(tasks_data, colWidths=[3*inch, 1.5*inch, 1*inch])
    tasks_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    story.append(tasks_table)
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.2 Metodología", heading2_style))
    story.append(Paragraph(
        "Se siguió una metodología ágil iterativa con los siguientes sprints:",
        normal_style
    ))
    
    sprints = [
        "<b>Sprint 1</b>: Análisis de requisitos y diseño de arquitectura",
        "<b>Sprint 2</b>: Desarrollo de módulos base (carga de datos, modelos)",
        "<b>Sprint 3</b>: Desarrollo del dashboard y visualizaciones",
        "<b>Sprint 4</b>: Integración, pruebas y refinamiento de UX",
        "<b>Sprint 5</b>: Documentación y preparación de entrega"
    ]
    
    for sprint in sprints:
        story.append(Paragraph(f"• {sprint}", bullet_style))
    
    story.append(PageBreak())
    
    # ===== 4. DISEÑO DEL DASHBOARD =====
    story.append(Paragraph("4. DISEÑO DEL DASHBOARD", heading_style))
    
    story.append(Paragraph("4.1 Bosquejo de Diseño", heading2_style))
    story.append(Paragraph(
        "El dashboard fue diseñado con una estructura de tres vistas principales:",
        normal_style
    ))
    
    design_points = [
        "<b>Vista 1 - Exploración de Datos</b>: Permite al usuario explorar las series temporales, "
        "agregaciones anuales/mensuales, estadísticas descriptivas y distribuciones.",
        
        "<b>Vista 2 - Modelos Predictivos</b>: Muestra las predicciones de los tres modelos con "
        "métricas de desempeño y gráficos de ajuste.",
        
        "<b>Vista 3 - Comparación de Modelos</b>: Tabla y gráficos comparativos del desempeño de "
        "los modelos para facilitar la selección del mejor."
    ]
    
    for point in design_points:
        story.append(Paragraph(f"• {point}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("4.2 Estructura de Navegación", heading2_style))
    story.append(Paragraph(
        "La navegación se implementó mediante un sidebar con radio buttons para cambiar entre vistas. "
        "Dentro de cada vista, se utilizan tabs y selectboxes para facilitar la exploración sin "
        "saturar la interfaz.",
        normal_style
    ))
    
    story.append(Paragraph("4.3 Principios de Diseño Aplicados", heading2_style))
    
    design_principles = [
        "<b>Jerarquía Visual</b>: Tamaños de fuente y colores diferenciados para guiar al usuario",
        "<b>Espaciado Generoso</b>: Uso de espacios en blanco para mejorar legibilidad",
        "<b>Consistencia</b>: Colores y estilos consistentes en todo el dashboard",
        "<b>Feedback Inmediato</b>: Indicadores de carga y tooltips informativos",
        "<b>Minimizar Carga Cognitiva</b>: No más de 3-4 controles visibles simultáneamente"
    ]
    
    for principle in design_principles:
        story.append(Paragraph(f"• {principle}", bullet_style))
    
    story.append(PageBreak())
    
    # ===== 5. SELECCIÓN DE HERRAMIENTA =====
    story.append(Paragraph("5. SELECCIÓN DE HERRAMIENTA", heading_style))
    
    story.append(Paragraph("5.1 Herramienta Seleccionada: Streamlit", heading2_style))
    story.append(Paragraph(
        "Se seleccionó <b>Streamlit</b> como framework principal para el desarrollo del dashboard "
        "por las siguientes razones:",
        normal_style
    ))
    
    streamlit_reasons = [
        "<b>Facilidad de Uso</b>: Sintaxis simple en Python puro, sin necesidad de HTML/CSS/JavaScript",
        "<b>Desarrollo Rápido</b>: Permite crear prototipos funcionales en horas",
        "<b>Integración con Plotly</b>: Soporte nativo para gráficos interactivos",
        "<b>Despliegue Gratuito</b>: Streamlit Cloud permite publicar gratuitamente",
        "<b>Comunidad Activa</b>: Amplia documentación y ejemplos disponibles",
        "<b>Compatibilidad</b>: Funciona con todas las librerías de Python (pandas, scikit-learn, etc.)"
    ]
    
    for reason in streamlit_reasons:
        story.append(Paragraph(f"• {reason}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("5.2 Librerías Complementarias", heading2_style))
    
    libs_data = [
        ["Librería", "Versión", "Propósito"],
        ["streamlit", "1.31.0", "Framework del dashboard"],
        ["plotly", "5.18.0", "Visualizaciones interactivas"],
        ["pandas", "2.1.4", "Manipulación de datos"],
        ["scikit-learn", "1.4.0", "Modelos de ML"],
        ["statsmodels", "0.14.1", "Modelo SARIMA"],
        ["numpy", "1.26.3", "Operaciones numéricas"],
    ]
    
    libs_table = Table(libs_data, colWidths=[1.5*inch, 1*inch, 3*inch])
    libs_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    story.append(libs_table)
    
    story.append(PageBreak())
    
    # ===== 6. ARQUITECTURA =====
    story.append(Paragraph("6. ARQUITECTURA DEL SISTEMA", heading_style))
    
    story.append(Paragraph("6.1 Estructura Modular", heading2_style))
    story.append(Paragraph(
        "El proyecto sigue una arquitectura modular para facilitar mantenimiento y escalabilidad:",
        normal_style
    ))
    
    modules = [
        "<b>config.py</b>: Configuración central (colores, parámetros, textos)",
        "<b>utils/data_loader.py</b>: Carga y preprocesamiento de datos",
        "<b>utils/predictive_models.py</b>: Entrenamiento y evaluación de modelos",
        "<b>utils/visualization_utils.py</b>: Funciones para crear gráficos con Plotly",
        "<b>app.py</b>: Aplicación principal de Streamlit"
    ]
    
    for module in modules:
        story.append(Paragraph(f"• {module}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("6.2 Flujo de Datos", heading2_style))
    story.append(Paragraph(
        "1. <b>Carga de Datos</b>: DataLoader lee archivos Excel y preprocesa<br/>"
        "2. <b>Procesamiento</b>: Se calculan agregaciones y estadísticas<br/>"
        "3. <b>Modelado</b>: PredictiveModels entrena y evalúa modelos<br/>"
        "4. <b>Visualización</b>: Funciones crean gráficos interactivos<br/>"
        "5. <b>Presentación</b>: Streamlit renderiza en el navegador",
        normal_style
    ))
    
    story.append(Paragraph("6.3 Optimizaciones Implementadas", heading2_style))
    
    optimizations = [
        "<b>Caching</b>: @st.cache_data para evitar recarga de datos en cada interacción",
        "<b>Carga Lazy</b>: Los modelos se entrenan solo cuando el usuario los requiere",
        "<b>Normalización</b>: Datos normalizados para mejorar desempeño de modelos",
        "<b>Vectorización</b>: Uso de operaciones vectorizadas de NumPy/Pandas"
    ]
    
    for opt in optimizations:
        story.append(Paragraph(f"• {opt}", bullet_style))
    
    story.append(PageBreak())
    
    # ===== 7. MODELOS PREDICTIVOS =====
    story.append(Paragraph("7. MODELOS PREDICTIVOS IMPLEMENTADOS", heading_style))
    
    story.append(Paragraph("7.1 Linear Regression", heading2_style))
    story.append(Paragraph(
        "<b>Descripción</b>: Modelo de regresión lineal simple que utiliza 12 períodos anteriores "
        "como características (lookback=12).",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Ventajas</b>: Simple, rápido, fácil de interpretar, bajo riesgo de overfitting.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Limitaciones</b>: Asume relaciones lineales, no captura patrones complejos.",
        normal_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("7.2 Random Forest", heading2_style))
    story.append(Paragraph(
        "<b>Descripción</b>: Modelo de ensamble basado en árboles de decisión con 100 árboles "
        "y profundidad máxima de 10.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Ventajas</b>: Captura relaciones no lineales, robusto a outliers, reduce varianza.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Limitaciones</b>: Más lento que regresión lineal, menos interpretable.",
        normal_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("7.3 SARIMA (Seasonal ARIMA)", heading2_style))
    story.append(Paragraph(
        "<b>Descripción</b>: Modelo estadístico especializado para series temporales con "
        "estacionalidad. Orden (1,1,1) y estacionalidad (1,1,1,12).",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Ventajas</b>: Diseñado específicamente para series de tiempo, captura estacionalidad.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Limitaciones</b>: Computacionalmente costoso, requiere datos estacionarios.",
        normal_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("7.4 Métricas de Evaluación", heading2_style))
    
    metrics_desc = [
        "<b>MAE (Mean Absolute Error)</b>: Promedio de errores absolutos. Fácil de interpretar.",
        "<b>MSE (Mean Squared Error)</b>: Promedio de errores al cuadrado. Penaliza más errores grandes.",
        "<b>R² (Coefficient of Determination)</b>: Proporción de varianza explicada (0-1).",
        "<b>RMSE (Root Mean Squared Error)</b>: Raíz del MSE, en unidades originales."
    ]
    
    for metric in metrics_desc:
        story.append(Paragraph(f"• {metric}", bullet_style))
    
    story.append(PageBreak())
    
    # ===== 8. VISUALIZACIONES =====
    story.append(Paragraph("8. VISUALIZACIONES IMPLEMENTADAS", heading_style))
    
    story.append(Paragraph(
        "El dashboard incluye más de 8 visualizaciones interactivas:",
        normal_style
    ))
    
    visualizations = [
        ["#", "Visualización", "Descripción", "Interactividad"],
        ["1", "Series Temporales", "Evolución de importación/consumo", "Zoom, pan, hover"],
        ["2", "Comparación Import/Cons", "Gráfico de área superpuesto", "Filtros enlazados"],
        ["3", "Volumen Anual", "Barras agrupadas por año", "Hover tooltips"],
        ["4", "Patrones Mensuales", "Líneas de promedios mensuales", "Zoom, pan"],
        ["5", "Matriz Correlación", "Heatmap de correlaciones", "Hover valores"],
        ["6", "Distribuciones", "Histograma + boxplot", "Selector productos"],
        ["7", "Predicciones", "Real vs predicho", "Selector modelos"],
        ["8", "Scatter Real/Pred", "Análisis de ajuste", "Hover, zoom"],
        ["9", "Métricas Comparativas", "Barras de métricas", "Selector modelos"],
        ["10", "Estadísticas Tabla", "DataFrame interactivo", "Sort, filtros"],
    ]
    
    viz_table = Table(visualizations, colWidths=[0.4*inch, 1.3*inch, 2*inch, 1.8*inch])
    viz_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    story.append(viz_table)
    
    story.append(PageBreak())
    
    # ===== 9. INTERACTIVIDAD =====
    story.append(Paragraph("9. CARACTERÍSTICAS DE INTERACTIVIDAD", heading_style))
    
    story.append(Paragraph("9.1 Gráficos Enlazados", heading2_style))
    story.append(Paragraph(
        "El dashboard implementa múltiples niveles de enlace entre visualizaciones:",
        normal_style
    ))
    
    linked = [
        "<b>Enlace 1</b>: Al seleccionar un producto en series temporales, el gráfico de todos "
        "los productos se actualiza para destacar el seleccionado.",
        
        "<b>Enlace 2</b>: Al cambiar el tipo de dato (Importación/Consumo), todas las "
        "visualizaciones de la sección se actualizan automáticamente.",
        
        "<b>Enlace 3</b>: En comparación de modelos, la selección de modelos afecta tanto la tabla "
        "como los gráficos de métricas y predicciones."
    ]
    
    for link in linked:
        story.append(Paragraph(f"• {link}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("9.2 Niveles de Detalle", heading2_style))
    story.append(Paragraph(
        "Los usuarios pueden aumentar o disminuir el nivel de detalle mediante:",
        normal_style
    ))
    
    detail_levels = [
        "Selección de productos específicos vs todos los productos",
        "Vista agregada anual vs vista mensual detallada",
        "Estadísticas resumidas vs distribuciones completas",
        "Métricas agregadas vs predicciones punto por punto"
    ]
    
    for level in detail_levels:
        story.append(Paragraph(f"• {level}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("9.3 Controles de Usuario", heading2_style))
    
    controls = [
        "<b>Selectbox</b>: Selección única de opciones (productos, modelos)",
        "<b>Multiselect</b>: Selección múltiple para comparaciones",
        "<b>Radio Buttons</b>: Cambio entre vistas principales",
        "<b>Tabs</b>: Organización de contenido relacionado",
        "<b>Expanders</b>: Información adicional colapsable",
        "<b>Tooltips</b>: Ayuda contextual en gráficos"
    ]
    
    for control in controls:
        story.append(Paragraph(f"• {control}", bullet_style))
    
    story.append(PageBreak())
    
    # ===== 10. INSTRUCCIONES =====
    story.append(Paragraph("10. INSTRUCCIONES DE USO", heading_style))
    
    story.append(Paragraph("10.1 Instalación", heading2_style))
    
    story.append(Paragraph("<b>Opción 1: Script Automático</b>", normal_style))
    story.append(Paragraph("Linux/Mac:", bullet_style))
    story.append(Paragraph("<font face='Courier'>./setup.sh</font>", bullet_style))
    story.append(Paragraph("Windows:", bullet_style))
    story.append(Paragraph("<font face='Courier'>setup.bat</font>", bullet_style))
    
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>Opción 2: Manual</b>", normal_style))
    manual_steps = [
        "1. Crear entorno virtual: <font face='Courier'>python -m venv venv</font>",
        "2. Activar: <font face='Courier'>source venv/bin/activate</font> (Linux/Mac) "
        "o <font face='Courier'>venv\\Scripts\\activate</font> (Windows)",
        "3. Instalar dependencias: <font face='Courier'>pip install -r requirements.txt</font>"
    ]
    
    for step in manual_steps:
        story.append(Paragraph(step, bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("10.2 Ejecución", heading2_style))
    story.append(Paragraph(
        "Ejecutar desde la carpeta del proyecto:",
        normal_style
    ))
    story.append(Paragraph("<font face='Courier'>streamlit run app.py</font>", bullet_style))
    story.append(Paragraph(
        "El dashboard se abrirá automáticamente en el navegador en http://localhost:8501",
        normal_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("10.3 Navegación", heading2_style))
    
    navigation = [
        "Usar el <b>sidebar</b> izquierdo para cambiar entre vistas",
        "Usar <b>selectboxes</b> para elegir productos y modelos",
        "Usar <b>tabs</b> para explorar diferentes análisis",
        "Hacer <b>hover</b> sobre gráficos para ver detalles",
        "Hacer <b>zoom</b> arrastrando sobre gráficos",
        "Hacer <b>doble clic</b> para resetear zoom"
    ]
    
    for nav in navigation:
        story.append(Paragraph(f"• {nav}", bullet_style))
    
    story.append(PageBreak())
    
    # ===== CONCLUSIONES =====
    story.append(Paragraph("CONCLUSIONES", heading_style))
    
    conclusions = [
        "Se desarrolló exitosamente un dashboard interactivo que cumple con todos los requisitos "
        "del laboratorio, incluyendo más de 8 visualizaciones, gráficos enlazados, y comparación "
        "de 3 modelos predictivos.",
        
        "La selección de Streamlit como framework permitió un desarrollo ágil y una interfaz "
        "intuitiva que facilita la exploración de datos sin necesidad de conocimientos técnicos "
        "avanzados por parte del usuario final.",
        
        "La paleta de colores seleccionada cumple con estándares de accesibilidad y mejora la "
        "legibilidad y usabilidad del dashboard, siguiendo principios de diseño corporativo.",
        
        "Los tres modelos predictivos implementados (Linear Regression, Random Forest, SARIMA) "
        "ofrecen diferentes enfoques para el análisis de series temporales, permitiendo comparar "
        "su desempeño y seleccionar el más adecuado según el caso de uso.",
        
        "La arquitectura modular del proyecto facilita el mantenimiento, pruebas y futuras "
        "extensiones del sistema."
    ]
    
    for i, conclusion in enumerate(conclusions, 1):
        story.append(Paragraph(f"{i}. {conclusion}", normal_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # ===== RECOMENDACIONES =====
    story.append(Paragraph("RECOMENDACIONES", heading_style))
    
    recommendations = [
        "Considerar el despliegue en Streamlit Cloud para acceso remoto sin instalación local.",
        
        "Implementar autenticación si el dashboard será usado en producción con datos sensibles.",
        
        "Añadir funcionalidad de exportación de gráficos y tablas para reportes ejecutivos.",
        
        "Incorporar más modelos de ML avanzados (LSTM, Prophet) para series con patrones complejos.",
        
        "Implementar sistema de alertas automáticas cuando se detecten anomalías en los datos."
    ]
    
    for i, rec in enumerate(recommendations, 1):
        story.append(Paragraph(f"{i}. {rec}", normal_style))
    
    story.append(Spacer(1, 0.5*inch))
    
    
    # Construir PDF
    doc.build(story)
    print(" Reporte PDF generado: Reporte_Dashboard_Hidrocarburos.pdf")

if __name__ == "__main__":
    create_report()
