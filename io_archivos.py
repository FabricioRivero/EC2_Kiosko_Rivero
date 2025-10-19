import csv

def cargar_datos(ruta_archivo):
    inventario = []
    try:
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila['cantidad'] = int(fila['cantidad'])
                fila['precio'] = float(fila['precio'])
                inventario.append(fila)
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo de datos.")
    return inventario

def guardar_datos(ruta_archivo, inventario):
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['codigo', 'nombre', 'categoria', 'cantidad', 'precio']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for producto in inventario:
            escritor.writerow(producto)
