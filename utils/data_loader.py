"""
Módulo para carga y preprocesamiento de datos
"""
import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    """Clase para cargar y preprocesar los datos de hidrocarburos"""
    
    def __init__(self, data_path='data'):
        self.data_path = Path(data_path)
        self.df_importacion = None
        self.df_consumo = None
        
    def load_data(self):
        """Carga los datos de importación y consumo"""
        archivo = self.data_path / "Estadisticas_historicas_comercializacion.xlsx"
        
        # Cargar importación
        self.df_importacion = pd.read_excel(
            archivo, 
            sheet_name="IMPORTACION", 
            skiprows=6, 
            nrows=289
        )
        
        # Cargar consumo
        self.df_consumo = pd.read_excel(
            archivo, 
            sheet_name="CONSUMO", 
            skiprows=6, 
            nrows=301
        )
        
        # Preprocesar
        self._preprocess()
        
        return self.df_importacion, self.df_consumo
    
    def _preprocess(self):
        """Preprocesamiento de los dataframes"""
        # Seleccionar columnas de interés
        cols_interes = ['Fecha', 'Gasolina regular', 'Gasolina superior', 'Diesel alto azufre']
        
        self.df_importacion = self.df_importacion[cols_interes].copy()
        self.df_consumo = self.df_consumo[cols_interes].copy()
        
        # Convertir fecha a datetime
        self.df_importacion['Fecha'] = pd.to_datetime(self.df_importacion['Fecha'])
        self.df_consumo['Fecha'] = pd.to_datetime(self.df_consumo['Fecha'])
        
        # Establecer fecha como índice
        self.df_importacion.set_index('Fecha', inplace=True)
        self.df_consumo.set_index('Fecha', inplace=True)
        
        # Eliminar valores NaN
        self.df_importacion = self.df_importacion.dropna()
        self.df_consumo = self.df_consumo.dropna()
    
    def get_combined_data(self):
        """Combina los datos de importación y consumo con prefijos"""
        df_imp = self.df_importacion.copy()
        df_cons = self.df_consumo.copy()
        
        # Renombrar columnas con prefijos
        df_imp.columns = [f'Importación {col}' for col in df_imp.columns]
        df_cons.columns = [f'Consumo {col}' for col in df_cons.columns]
        
        # Combinar en el índice común
        df_combined = df_imp.join(df_cons, how='outer')
        
        return df_combined
    
    def get_statistics(self):
        """Retorna estadísticas descriptivas de los datos"""
        stats_imp = self.df_importacion.describe()
        stats_cons = self.df_consumo.describe()
        
        return {
            'importacion': stats_imp,
            'consumo': stats_cons
        }
    
    def get_date_range(self):
        """Retorna el rango de fechas disponible"""
        return {
            'importacion': {
                'inicio': self.df_importacion.index.min(),
                'fin': self.df_importacion.index.max(),
                'registros': len(self.df_importacion)
            },
            'consumo': {
                'inicio': self.df_consumo.index.min(),
                'fin': self.df_consumo.index.max(),
                'registros': len(self.df_consumo)
            }
        }
    
    def get_data_for_product(self, producto, tipo='ambos'):
        """
        Retorna datos para un producto específico
        
        Args:
            producto: Nombre del producto
            tipo: 'importacion', 'consumo', o 'ambos'
        """
        result = {}
        
        if tipo in ['importacion', 'ambos']:
            result['importacion'] = self.df_importacion[producto]
        
        if tipo in ['consumo', 'ambos']:
            result['consumo'] = self.df_consumo[producto]
        
        return result
    
    def get_yearly_aggregation(self):
        """Retorna agregación anual de los datos"""
        # Importación
        df_imp_yearly = self.df_importacion.copy()
        df_imp_yearly['Año'] = df_imp_yearly.index.year
        imp_yearly = df_imp_yearly.groupby('Año').sum()
        
        # Consumo
        df_cons_yearly = self.df_consumo.copy()
        df_cons_yearly['Año'] = df_cons_yearly.index.year
        cons_yearly = df_cons_yearly.groupby('Año').sum()
        
        return {
            'importacion': imp_yearly,
            'consumo': cons_yearly
        }
    
    def get_monthly_patterns(self):
        """Retorna patrones mensuales promedio"""
        # Importación
        df_imp_monthly = self.df_importacion.copy()
        df_imp_monthly['Mes'] = df_imp_monthly.index.month
        imp_monthly = df_imp_monthly.groupby('Mes').mean()
        
        # Consumo
        df_cons_monthly = self.df_consumo.copy()
        df_cons_monthly['Mes'] = df_cons_monthly.index.month
        cons_monthly = df_cons_monthly.groupby('Mes').mean()
        
        return {
            'importacion': imp_monthly,
            'consumo': cons_monthly
        }
