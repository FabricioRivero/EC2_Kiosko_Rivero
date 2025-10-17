# inventario.py
from io_archivos import guardar_datos
from busquedas_ordenamientos import busqueda_lineal, ordenamiento_burbuja

# Lista de productos en memoria
productos = []

# Alta de producto
def alta_producto():
    print("\n--- Alta de producto ---")
    codigo = input("Ingrese el código del producto: ")
    
    # Verificar si el código ya existe
    if busqueda_lineal(productos, codigo):
        print("¡Error! El producto ya existe.")
        return
    
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        stock_minimo = int(input("Ingrese el stock mínimo: "))
    except ValueError:
        print("Error: Valores inválidos. Deben ser números.")
        return
    
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo
    }
    
    productos.append(producto)
    print(f"Producto {nombre} agregado correctamente.")
    guardar_datos()

# Baja de producto
def baja_producto():
    print("\n--- Baja de producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ")
    producto = busqueda_lineal(productos, codigo)
    
    if producto:
        productos.remove(producto)
        print(f"Producto {producto['nombre']} eliminado.")
        guardar_datos()
    else:
        print("Producto no encontrado.")

# Modificación de producto
def modificar_producto():
    print("\n--- Modificación de producto ---")
    codigo = input("Ingrese el código del producto a modificar: ")
    producto = busqueda_lineal(productos, codigo)
    
    if producto:
        print(f"Producto encontrado: {producto['nombre']}")
        nombre = input(f"Nuevo nombre [{producto['nombre']}]: ") or producto['nombre']
        try:
            precio = input(f"Nuevo precio [{producto['precio']}]: ")
            precio = float(precio) if precio else producto['precio']
            stock = input(f"Nuevo stock [{producto['stock']}]: ")
            stock = int(stock) if stock else producto['stock']
            stock_minimo = input(f"Nuevo stock mínimo [{producto['stock_minimo']}]: ")
            stock_minimo = int(stock_minimo) if stock_minimo else producto['stock_minimo']
        except ValueError:
            print("Error: Valores inválidos.")
            return
        
        producto.update({
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "stock_minimo": stock_minimo
        })
        print("Producto modificado correctamente.")
        guardar_datos()
    else:
        print("Producto no encontrado.")

# Listar todos los productos
def listar_productos():
    print("\n--- Lista de productos ---")
    if not productos:
        print("No hay productos registrados.")
        return
    
    # Ordenar productos por código
    ordenamiento_burbuja(productos)
    
    print(f"{'Código':10} {'Nombre':15} {'Precio':10} {'Stock':7} {'Stock Mínimo':13}")
    print("-" * 60)
    for p in productos:
        print(f"{p['codigo']:10} {p['nombre']:15} {p['precio']:10.2f} {p['stock']:7} {p['stock_minimo']:13}")

