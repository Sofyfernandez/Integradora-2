# Descripción: Punto de entrada principal del sistema Protectores del Código
# Proceso:
#   1. Importa la clase Menu del módulo menu
#   2. Crea una instancia de Menu
#   3. Inicia la ejecución del programa
# Entrada: No requiere 
# Salida: No retorna valores, ejecuta el programa principal

from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
