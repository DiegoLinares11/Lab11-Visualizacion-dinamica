"""
Configuración del Dashboard de Hidrocarburos
Paleta de colores y configuración general
"""

# PALETA DE COLORES - Tema Profesional de Energía
# Paleta basada en tonos azules (confianza, profesionalismo) y naranjas (energía, acción)
# con grises neutros para facilitar lectura

COLORS = {
    # Colores principales
    'primary': '#1f77b4',      # Azul principal - Importación
    'secondary': '#ff7f0e',    # Naranja - Consumo
    'accent': '#2ca02c',       # Verde - Predicciones positivas
    'warning': '#d62728',      # Rojo - Alertas/Errores
    
    # Colores para productos específicos
    'gasolina_regular': '#4a90e2',     # Azul medio
    'gasolina_superior': '#7b68ee',    # Azul-violeta
    'diesel': '#ff8c42',               # Naranja
    
    # Colores para visualizaciones
    'chart_colors': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
    
    # Fondos y textos
    'background': '#f8f9fa',
    'text': '#2c3e50',
    'text_light': '#7f8c8d',
    
    # Grises
    'gray_light': '#ecf0f1',
    'gray_medium': '#bdc3c7',
    'gray_dark': '#34495e',
}

# CONFIGURACIÓN DE MODELOS
MODEL_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
    'sarima_order': (1, 1, 1),
    'sarima_seasonal_order': (1, 1, 1, 12),
}

# COLUMNAS DE INTERÉS
PRODUCTOS = ['Gasolina regular', 'Gasolina superior', 'Diesel alto azufre']

# CONFIGURACIÓN DEL DASHBOARD
DASHBOARD_CONFIG = {
    'page_title': 'Dashboard de Hidrocarburos Guatemala',
    'page_icon': '⛽',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}

# TEXTOS Y DESCRIPCIONES
TEXTS = {
    'main_title': ' Dashboard Interactivo - Análisis de Hidrocarburos en Guatemala',
    'subtitle': 'Exploración de datos de importación y consumo con modelos predictivos',
    'about': '''
    Este dashboard permite explorar los datos históricos de importación y consumo 
    de hidrocarburos en Guatemala, así como comparar el desempeño de diferentes 
    modelos predictivos para la toma de decisiones informadas.
    ''',
    'data_source': 'Fuente: Estadísticas Históricas de Comercialización - Guatemala',
}

# JUSTIFICACIÓN DE LA PALETA DE COLORES
COLOR_JUSTIFICATION = """
**Justificación de la Paleta de Colores:**

La paleta seleccionada sigue principios de diseño para dashboards corporativos:

1. **Azul (#1f77b4)**: Color principal que transmite confianza, profesionalismo y estabilidad.
   Ideal para datos de importación y análisis serio.

2. **Naranja (#ff7f0e)**: Color complementario que aporta energía y calidez, perfecto para
   representar consumo y acción.

3. **Verde (#2ca02c)**: Para indicadores positivos y predicciones favorables, asociado con
   crecimiento y éxito.

4. **Rojo (#d62728)**: Reservado para alertas, errores o valores críticos que requieren atención.

5. **Grises neutros**: Facilitan la lectura y reducen la fatiga visual, permitiendo que los
   datos sean el foco principal.

Esta paleta cumple con estándares de accesibilidad WCAG 2.1 para contraste y es adecuada
para personas con daltonismo (especialmente deuteranopía y protanopía).
"""
