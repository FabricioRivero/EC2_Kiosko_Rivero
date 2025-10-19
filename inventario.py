def buscar_producto(inventario, codigo):
    for p in inventario:
        if p['codigo'] == codigo:
            return p
    return None

def agregar_producto(inventario, nuevo):
    if buscar_producto(inventario, nuevo['codigo']):
        print("❌ Ya existe un producto con ese código.")
        return
    inventario.append(nuevo)
    print("✅ Producto agregado correctamente.")

def eliminar_producto(inventario, codigo):
    producto = buscar_producto(inventario, codigo)
    if producto:
        inventario.remove(producto)
        print("🗑️ Producto eliminado.")
    else:
        print("⚠️ No se encontró el producto.")

def actualizar_stock(inventario, codigo, nueva_cantidad):
    producto = buscar_producto(inventario, codigo)
    if producto:
        producto['cantidad'] = nueva_cantidad
        print("🔄 Stock actualizado.")
    else:
        print("⚠️ No se encontró el producto.")
