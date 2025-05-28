import os
from time import sleep
from util import validate_year
from multiverso import Multiverse

# Descripción: Clase que maneja la interfaz de usuario en consola
# Atributos:
#   - multiverse: Instancia de la clase Multiverso para análisis de datos
class Menu:
    def __init__(self):
        self.multiverse = Multiverse('anomalias_multiverso_test.xlsx')
        
    # Descripción: Limpia la pantalla de la consola
    # Entrada: No requiere parámetros
    # Proceso: Ejecuta el comando de limpieza según el sistema operativo
    # Salida: No retorna valor, efecto visual en consola
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # Descripción: Muestra el encabezado decorativo del programa
    # Entrada: No requiere parámetros
    # Proceso: Imprime título y versión con formato decorativo
    # Salida: No retorna valor, imprime en consola
    def show_header(self):
        print("\n" + "="*50)
        print("🌌 SISTEMA PROTECTORES DEL CÓDIGO 🌌".center(50))
        print("Análisis del Multiverso v1.0".center(50))
        print("="*50 + "\n")
        
    # Descripción: Muestra las opciones disponibles del menú
    # Entrada: No requiere parámetros
    # Proceso: Imprime lista numerada de opciones
    # Salida: No retorna valor, imprime en consola
    def show_menu(self):
        print("\nOPCIONES DISPONIBLES:")
        print("1. Cargar datos del multiverso")
        print("2. Filtrar eventos por año")
        print("3. Clasificar eventos temporalmente")
        print("4. Ver código de error más común")
        print("5. Analizar niveles de afectación")
        print("6. Identificar dimensión de mayor riesgo")
        print("7. Calcular estabilidad del multiverso")
        print("8. Exportar datos procesados")
        print("9. Salir")
        
    # Descripción: Pausa la ejecución hasta que el usuario presione Enter
    # Entrada: No requiere parámetros
    # Proceso: Espera input del usuario
    # Salida: No retorna valor, pausa la ejecución
    def wait_enter(self):
        input("\nPresione Enter para continuar...")
        
    # Descripción: Ejecuta el bucle principal del programa
    # Entrada: No requiere parámetros
    # Proceso: 
    #   1. Muestra menú y opciones
    #   2. Procesa selección del usuario
    #   3. Ejecuta la funcionalidad correspondiente
    #   4. Repite hasta que usuario seleccione salir
    # Salida: No retorna valor, controla flujo del programa
    def run(self):
        while True:
            self.clear_screen()
            self.show_header()
            self.show_menu()
            
            option = input("\nSeleccione una opción (1-9): ")
            
            self.clear_screen()
            self.show_header()
            
            if option == "1":
                if self.multiverse.load_data():
                    print("\n✅ Datos cargados exitosamente!")
                else:
                    print("\n❌ Error al cargar los datos.")
                    
            elif option == "2":
                if self.multiverse.df is None:
                    print("\n❌ Error: Primero debe cargar los datos (opción 1)")
                else:
                    year = input("\nIngrese el año de referencia: ")
                    valid, year_int = validate_year(year)
                    if valid:
                        results = self.multiverse.filter_by_year(year_int)
                        print(f"\nResultados del filtrado para el año {year_int}:")
                        print(f"- Eventos anteriores: {results['previous']}")
                        print(f"- Eventos posteriores: {results['next']}")
                        print(f"- Eventos del año exacto: {results['exact']}")
                        
            elif option == "3":
                if self.multiverse.year_reference is None:
                    print("\n❌ Error: Primero debe filtrar por año (opción 2)")
                else:
                    if self.multiverse.classify_events():
                        print("\n✅ Eventos clasificados exitosamente!")
                        
            elif option == "4":
                if self.multiverse.df is None:
                    print("\n❌ Error: Primero debe cargar los datos (opción 1)")
                else:
                    code = self.multiverse.most_common_error()
                    print(f"\nEl código de error más común es: {code}")
                    
            elif option == "5":
                if self.multiverse.df is None:
                    print("\n❌ Error: Primero debe cargar los datos (opción 1)")
                else:
                    results = self.multiverse.analyze_affectation()
                    print("\nAnálisis de niveles de afectación:")
                    print(f"- Bajo impacto (1-30): {results['low_impact']}")
                    print(f"- Afectación moderada (31-70): {results['moderate_impact']}")
                    print(f"- Alta corrupción (71-100): {results['high_impact']}")
                    
            elif option == "6":
                if self.multiverse.df is None:
                    print("\n❌ Error: Primero debe cargar los datos (opción 1)")
                else:
                    dimension = self.multiverse.highest_risk_dimension()
                    print(f"\nLa dimensión con mayor riesgo es: {dimension}")
                    
            elif option == "7":
                if self.multiverse.df is None:
                    print("\n❌ Error: Primero debe cargar los datos (opción 1)")
                else:
                    score, message = self.multiverse.calculate_stability()
                    print(f"\nPuntaje de estabilidad: {score}")
                    print(f"Estado del multiverso: {message}")
                    
            elif option == "8":
                if self.multiverse.df is None:
                    print("\n❌ Error: Primero debe cargar los datos (opción 1)")
                else:
                    if self.multiverse.export_data():
                        print("\n✅ Datos exportados exitosamente!")
                        
            elif option == "9":
                print("\n¡Gracias por usar el Sistema Protectores del Código!")
                print("Cerrando programa", end="")
                for _ in range(3):
                    sleep(0.5)
                    print(".", end="", flush=True)
                print()
                break
                
            else:
                print("\n❌ Opción inválida. Por favor, seleccione una opción válida (1-9)")
                
            self.wait_enter()
