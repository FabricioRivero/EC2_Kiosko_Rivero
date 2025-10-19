def mostrar_inventario(inventario):
    print("\n📦 INVENTARIO ACTUAL")
    print("-" * 50)
    for p in inventario:
        print(f"{p['codigo']} | {p['nombre']} | {p['categoria']} | {p['cantidad']} unidades | Bs {p['precio']}")
    print("-" * 50)

def productos_bajos(inventario, minimo=10):
    print("\n⚠️ PRODUCTOS CON BAJO STOCK")
    for p in inventario:
        if p['cantidad'] < minimo:
            print(f"{p['nombre']} ({p['cantidad']} unidades)")

def valor_total(inventario):
    total = sum(p['cantidad'] * p['precio'] for p in inventario)
    print(f"\n💰 Valor total del inventario: Bs {total:.2f}")
