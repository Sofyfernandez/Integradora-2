import pandas as pd
from util import validate_excel_file, validate_stability_score

# Descripción: Clase que maneja el análisis de datos del multiverso
# Atributos:
#   - excel_path: Ruta al archivo Excel con los datos
#   - df: DataFrame de pandas con los datos cargados
#   - year_reference: Año de referencia para análisis temporal
class Multiverse:
    def __init__(self, excel_path):
        self.excel_path = excel_path
        self.df = None
        self.year_reference = None

    # Descripción: Carga los datos del archivo Excel a memoria
    # Entrada: No requiere parámetros, usa el excel_path del constructor
    # Proceso: Lee el archivo Excel y valida su estructura
    # Salida: (bool) True si la carga fue exitosa, False si hubo error
    def load_data(self) -> bool:

        if not validate_excel_file(self.excel_path):
            return False
            
        try:
            self.df = pd.read_excel(self.excel_path)
            print(f"Datos cargados exitosamente. Total de registros: {len(self.df)}")
            return True
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")
            return False

    # Descripción: Analiza eventos según un año de referencia
    # Entrada: (int) year - Año para comparar los eventos
    # Proceso: Cuenta eventos anteriores, posteriores y exactos al año dado
    # Salida: (dict) Diccionario con conteo de eventos por categoría temporal
    def filter_by_year(self, year: int) -> dict:

        self.year_reference = year
        previous = len(self.df[self.df['Año_Corrupcion'] < year])
        next_events = len(self.df[self.df['Año_Corrupcion'] > year])
        exact = len(self.df[self.df['Año_Corrupcion'] == year])
        
        return {
            'previous': previous,
            'next': next_events,
            'exact': exact
        }

    # Descripción: Clasifica eventos según su relación temporal con el año de referencia
    # Entrada: No requiere parámetros, usa year_reference almacenado
    # Proceso: Asigna estados (Histórico/Futuro/Imposible) según el año
    # Salida: (bool) True si la clasificación fue exitosa, False si falta el año de referencia
    def classify_events(self) -> bool:

        if self.year_reference is None:
            print("Error: Primero debe ejecutar el filtrado por año")
            return False
            
        if not isinstance(self.year_reference, int):
            print("Error: El año de referencia debe ser un número entero")
            return False
            
        def assign_state(year):
            if year < self.year_reference:
                return "Registro Histórico"
            elif year > self.year_reference:
                return "Va a Suceder"
            return "Imposible"
            
        self.df['Estado_Evento'] = self.df['Año_Corrupcion'].apply(assign_state)
        return True

    # Descripción: Identifica el código de error más frecuente
    # Entrada: No requiere parámetros, usa datos cargados
    # Proceso: Cuenta frecuencia de cada código de error
    # Salida: (str) Código de error que aparece más veces
    def most_common_error(self) -> str:

        return self.df['Codigo_Error'].mode().iloc[0]

    # Descripción: Analiza niveles de afectación de los universos
    # Entrada: No requiere parámetros, usa datos cargados
    # Proceso: Categoriza universos según su nivel de afectación
    # Salida: (dict) Conteo de universos por categoría de afectación
    def analyze_affectation(self) -> dict:

        # Categorías de afectación:
        # Bajo impacto: 1-30
        # Afectación moderada: 31-70
        # Alta corrupción: 71-100
        low = len(self.df[self.df['Nivel_Afectacion'].between(1, 30)])
        moderate = len(self.df[self.df['Nivel_Afectacion'].between(31, 70)])
        high = len(self.df[self.df['Nivel_Afectacion'].between(71, 100)])
        
        return {
            'low_impact': low,
            'moderate_impact': moderate,
            'high_impact': high
        }

    # Descripción: Encuentra la dimensión con más anomalías
    # Entrada: No requiere parámetros, usa datos cargados
    # Proceso: Cuenta anomalías por dimensión
    # Salida: (str) Nombre de la dimensión con más anomalías
    def highest_risk_dimension(self) -> str:

        return self.df['Dimension'].value_counts().index[0]

    # Descripción: Calcula el índice de estabilidad del multiverso
    # Entrada: No requiere parámetros, usa datos cargados
    # Proceso: Suma puntos según el estado de cada universo
    # Salida: (tuple) (puntaje total, mensaje de estado)
    def calculate_stability(self) -> tuple[float, str]:

        # Sistema de puntos:
        # Estable: +3 puntos
        # Inestable: +1 punto
        # Colapsado: -2 puntos
        points = {
            'Estable': 3,
            'Inestable': 1,
            'Colapsado': -2
        }
        
        total_score = sum(self.df['Estado_Actual'].map(points))
        message = validate_stability_score(total_score)
        return total_score, message

    # Descripción: Exporta los datos procesados a un nuevo archivo Excel
    # Entrada: No requiere parámetros, usa datos procesados
    # Proceso: Guarda todos los datos incluyendo el Estado_Evento en Excel
    # Salida: (bool) True si la exportación fue exitosa, False si hubo error
    def export_data(self) -> bool:
        if 'Estado_Evento' not in self.df.columns:
            print("Error: Primero debe ejecutar la clasificación de eventos")
            return False
            
        try:
            self.df.to_excel('realidades_restauradas.xlsx', index=False)
            print("Datos exportados exitosamente a 'realidades_restauradas.xlsx'")
            return True
        except Exception as e:
            print(f"Error al exportar datos: {str(e)}")
            return False