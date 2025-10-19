def buscar_producto(inventario, codigo):
    for p in inventario:
        if p['codigo'] == codigo:
            return p
    return None

def agregar_producto(inventario, nuevo):
    inventario.append(nuevo)
    print("✅ Producto agregado.")

def eliminar_producto(inventario, codigo):
    p = buscar_producto(inventario, codigo)
    if p:
        inventario.remove(p)
        print("🗑️ Producto eliminado.")
    else:
        print("⚠️ No encontrado.")

def actualizar_stock(inventario, codigo, nuevo_stock):
    p = buscar_producto(inventario, codigo)
    if p:
        p['stock'] = nuevo_stock
        print("🔄 Stock actualizado.")
    else:
        print("⚠️ No encontrado.")

def vender_producto(inventario, codigo, cantidad):
    p = buscar_producto(inventario, codigo)
    if not p:
        print("⚠️ No encontrado.")
        return 0
    if p['stock'] < cantidad:
        print("❌ Stock insuficiente.")
        return 0
    p['stock'] -= cantidad
    p['vendidos_hoy'] += cantidad
    total = cantidad * p['precio']
    print(f"✅ Venta registrada: {p['nombre']} ({cantidad} u.) Total Bs {total:.2f}")
    return total
