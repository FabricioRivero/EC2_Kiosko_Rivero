from inventario import Inventario 
from reportes import Reportes
from io_archivos import IOArchivos  

def menu_principal():
    while  True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Inventario")
        print("2. Reportes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "4":
            print("Guardando datos y saliendo...    ")
            guardar_datos()
            break
        else:
            print("Opcion en desarrollo...")
            
if __name__ == "__main__":
    cargar_datos()
    menu_principal()
    
