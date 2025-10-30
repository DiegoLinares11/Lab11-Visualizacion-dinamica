"""
Módulo con modelos predictivos para series de tiempo
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
warnings.filterwarnings('ignore')

class PredictiveModels:
    """Clase para entrenar y evaluar modelos predictivos"""
    
    def __init__(self, test_size=0.2):
        self.test_size = test_size
        self.models = {}
        self.predictions = {}
        self.metrics = {}
        self.scaler = MinMaxScaler()
        
    def prepare_data(self, serie, lookback=12):
        """
        Prepara los datos para modelos de ML
        
        Args:
            serie: Serie temporal
            lookback: Número de períodos anteriores a usar como features
        """
        serie = serie.dropna()
        
        # Crear features (valores pasados)
        X, y = [], []
        for i in range(lookback, len(serie)):
            X.append(serie.iloc[i-lookback:i].values)
            y.append(serie.iloc[i])
        
        X = np.array(X)
        y = np.array(y)
        
        # Split train/test
        split_idx = int(len(X) * (1 - self.test_size))
        X_train, X_test = X[:split_idx], X[split_idx:]
        y_train, y_test = y[:split_idx], y[split_idx:]
        
        return X_train, X_test, y_train, y_test, serie.index[lookback:]
    
    def train_linear_regression(self, serie, lookback=12):
        """Entrena modelo de Regresión Lineal"""
        X_train, X_test, y_train, y_test, dates = self.prepare_data(serie, lookback)
        
        # Entrenar modelo
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Predicciones
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        # Métricas
        metrics = {
            'train': {
                'mse': mean_squared_error(y_train, y_pred_train),
                'mae': mean_absolute_error(y_train, y_pred_train),
                'r2': r2_score(y_train, y_pred_train)
            },
            'test': {
                'mse': mean_squared_error(y_test, y_pred_test),
                'mae': mean_absolute_error(y_test, y_pred_test),
                'r2': r2_score(y_test, y_pred_test)
            }
        }
        
        return {
            'model': model,
            'predictions': {
                'train': y_pred_train,
                'test': y_pred_test,
                'y_train': y_train,
                'y_test': y_test,
                'dates': dates
            },
            'metrics': metrics
        }
    
    def train_random_forest(self, serie, lookback=12):
        """Entrena modelo de Random Forest"""
        X_train, X_test, y_train, y_test, dates = self.prepare_data(serie, lookback)
        
        # Entrenar modelo
        model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
        model.fit(X_train, y_train)
        
        # Predicciones
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        # Métricas
        metrics = {
            'train': {
                'mse': mean_squared_error(y_train, y_pred_train),
                'mae': mean_absolute_error(y_train, y_pred_train),
                'r2': r2_score(y_train, y_pred_train)
            },
            'test': {
                'mse': mean_squared_error(y_test, y_pred_test),
                'mae': mean_absolute_error(y_test, y_pred_test),
                'r2': r2_score(y_test, y_pred_test)
            }
        }
        
        return {
            'model': model,
            'predictions': {
                'train': y_pred_train,
                'test': y_pred_test,
                'y_train': y_train,
                'y_test': y_test,
                'dates': dates
            },
            'metrics': metrics
        }
    
    def train_sarima(self, serie):
        """Entrena modelo SARIMA"""
        serie = serie.dropna()
        
        # Normalizar serie
        serie_norm = self.scaler.fit_transform(serie.values.reshape(-1, 1)).flatten() * 10
        serie_norm = pd.Series(serie_norm, index=serie.index)
        
        # Split train/test
        split_idx = int(len(serie_norm) * (1 - self.test_size))
        train = serie_norm.iloc[:split_idx]
        test = serie_norm.iloc[split_idx:]
        
        try:
            # Entrenar modelo SARIMA
            model = SARIMAX(
                train,
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12),
                enforce_stationarity=False,
                enforce_invertibility=False
            )
            fitted_model = model.fit(disp=False, maxiter=200)
            
            # Predicciones
            y_pred_train = fitted_model.fittedvalues
            y_pred_test = fitted_model.forecast(steps=len(test))
            
            # Desnormalizar
            y_pred_train_original = self.scaler.inverse_transform(
                (y_pred_train / 10).values.reshape(-1, 1)
            ).flatten()
            y_pred_test_original = self.scaler.inverse_transform(
                (y_pred_test.values / 10).reshape(-1, 1)
            ).flatten()
            
            train_original = serie.iloc[:split_idx].values
            test_original = serie.iloc[split_idx:].values
            
            # Métricas
            metrics = {
                'train': {
                    'mse': mean_squared_error(train_original, y_pred_train_original),
                    'mae': mean_absolute_error(train_original, y_pred_train_original),
                    'r2': r2_score(train_original, y_pred_train_original)
                },
                'test': {
                    'mse': mean_squared_error(test_original, y_pred_test_original),
                    'mae': mean_absolute_error(test_original, y_pred_test_original),
                    'r2': r2_score(test_original, y_pred_test_original)
                }
            }
            
            return {
                'model': fitted_model,
                'predictions': {
                    'train': y_pred_train_original,
                    'test': y_pred_test_original,
                    'y_train': train_original,
                    'y_test': test_original,
                    'dates': serie.index
                },
                'metrics': metrics
            }
        
        except Exception as e:
            print(f"Error en SARIMA: {e}")
            return None
    
    def compare_models(self, serie, nombre_serie):
        """
        Compara los tres modelos en una serie
        
        Returns:
            DataFrame con métricas comparativas
        """
        print(f"Entrenando modelos para: {nombre_serie}")
        
        # Entrenar modelos
        lr_result = self.train_linear_regression(serie)
        rf_result = self.train_random_forest(serie)
        sarima_result = self.train_sarima(serie)
        
        # Guardar resultados
        self.models[nombre_serie] = {
            'Linear Regression': lr_result,
            'Random Forest': rf_result,
            'SARIMA': sarima_result
        }
        
        # Crear tabla comparativa
        comparacion = []
        
        for model_name, result in self.models[nombre_serie].items():
            if result is not None:
                comparacion.append({
                    'Modelo': model_name,
                    'MAE (Train)': result['metrics']['train']['mae'],
                    'MSE (Train)': result['metrics']['train']['mse'],
                    'R² (Train)': result['metrics']['train']['r2'],
                    'MAE (Test)': result['metrics']['test']['mae'],
                    'MSE (Test)': result['metrics']['test']['mse'],
                    'R² (Test)': result['metrics']['test']['r2']
                })
        
        df_comparacion = pd.DataFrame(comparacion)
        
        return df_comparacion
    
    def get_predictions(self, serie_nombre, modelo_nombre):
        """Obtiene las predicciones de un modelo específico"""
        if serie_nombre in self.models and modelo_nombre in self.models[serie_nombre]:
            return self.models[serie_nombre][modelo_nombre]['predictions']
        return None
