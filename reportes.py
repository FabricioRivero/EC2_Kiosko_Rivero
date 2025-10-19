def mostrar_inventario(inventario):
    print("\n📦 INVENTARIO")
    print("-"*50)
    for p in inventario:
        print(f"{p['codigo']} | {p['nombre']} | {p['stock']}u | Bs {p['precio']} | Vendidos: {p['vendidos_hoy']}")
    print("-"*50)

def productos_bajos(inventario):
    bajos = [p for p in inventario if p['stock'] < p['stock_minimo']]
    if bajos:
        print("\n⚠️ Productos bajo stock mínimo:")
        for p in bajos:
            print(f"{p['nombre']} ({p['stock']} < {p['stock_minimo']})")
    else:
        print("✅ Todo con stock suficiente.")

def valor_total(inventario):
    total = sum(p['stock'] * p['precio'] for p in inventario)
    print(f"\n💰 Valor total: Bs {total:.2f}")

def top_3_vendidos(inventario):
    top = sorted(inventario, key=lambda x: x['vendidos_hoy'], reverse=True)[:3]
    print("\n🏆 Top 3 más vendidos hoy:")
    for p in top:
        print(f"{p['nombre']} - {p['vendidos_hoy']} vendidos")

def ticket_promedio_y_total(ventas_dia):
    if not ventas_dia:
        print("⚠️ No hubo ventas.")
        return
    total = sum(ventas_dia)
    promedio = total / len(ventas_dia)
    print(f"\n🧾 Ticket promedio: Bs {promedio:.2f}")
    print(f"💵 Total del día: Bs {total:.2f}")
