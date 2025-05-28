import os
import pandas as pd

# Descripción: Verifica si un archivo Excel existe y tiene la estructura correcta
# Entrada: (str) file_path - Ruta al archivo Excel que se quiere validar
# Proceso: Verifica que el archivo exista y contenga todas las columnas requeridas
# Salida: (bool) True si el archivo es válido, False si hay error
def validate_excel_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        return False
    
    try:
        df = pd.read_excel(file_path)
        required_columns = [
            'ID_Universo', 
            'Año_Corrupcion', 
            'Codigo_Error',
            'Descripcion_Error',
            'Nivel_Afectacion',
            'Estado_Actual',
            'Dimension'
        ]
        
        for col in required_columns:
            if col not in df.columns:
                print(f"Error: Columna requerida '{col}' no encontrada en el archivo.")
                return False
                
        return True
    except Exception as e:
        print(f"Error al leer el archivo Excel: {str(e)}")
        return False

# Descripción: Valida si una entrada puede convertirse a un año válido
# Entrada: (str) year - Cadena de texto que representa el año
# Proceso: Intenta convertir la cadena a un número entero
# Salida: (tuple) (bool, int) - Par ordenado con éxito de validación y el año convertido
def validate_year(year):
    try:
        year_int = int(year)
        return True, year_int
    except ValueError:
        print("Error: El año debe ser un número entero válido.")
        return False, 0

# Descripción: Determina el estado del multiverso según un puntaje
# Entrada: (float) score - Puntaje de estabilidad del multiverso
# Proceso: Evalúa el puntaje en diferentes rangos para determinar el estado
# Salida: (str) Mensaje que describe el estado actual del multiverso
def validate_stability_score(score):
    if score >= 80:
        return "El Multiverso está a salvo"
    elif 50 <= score < 80:
        return "Riesgo moderado, seguir corrigiendo"
    else:
        return "Caos inminente, intervención urgente"