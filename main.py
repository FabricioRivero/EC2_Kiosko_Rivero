from io_archivos import cargar_datos, guardar_datos, guardar_binario, exportar_alertas
from inventario import agregar_producto, eliminar_producto, actualizar_stock, vender_producto
from reportes import mostrar_inventario, productos_bajos, valor_total, top_3_vendidos, ticket_promedio_y_total
from busquedas_ordenamiento import busqueda_binaria_por_codigo, buscar_por_nombre, ordenar_burbuja_por_precio
import datetime

RUTA = "datos.csv"
BINARIO = "datos.bin"

# ------------------- Entradas validadas -------------------
def input_no_vacio(mensaje):
    while True:
        v = input(mensaje).strip()
        if v == "":
            print("⚠️ No puede estar vacío.")
        else:
            return v

def input_entero(mensaje, minimo=0):
    while True:
        try:
            n = int(input(mensaje))
            if n < minimo:
                print(f"⚠️ Debe ser >= {minimo}.")
            else:
                return n
        except ValueError:
            print("❌ Ingrese un número válido.")

def input_flotante(mensaje, minimo=0):
    while True:
        try:
            n = float(input(mensaje))
            if n <= minimo:
                print(f"⚠️ Debe ser > {minimo}.")
            else:
                return n
        except ValueError:
            print("❌ Ingrese un número decimal válido.")
# ------------------------------------------------------------

def menu():
    print("""
===== 🏫 KIOSKO UNIVERSITARIO UCB =====
1. Ver inventario
2. Agregar producto
3. Eliminar producto
4. Actualizar stock
5. Registrar venta
6. Reportes
7. Guardar y salir
""")

def menu_reportes(inventario, ventas_dia):
    print("""
--- REPORTES ---
1. Productos con bajo stock
2. Valor total del inventario
3. Top 3 más vendidos
4. Ticket promedio y total del día
""")
    op = input("Opción: ")
    if op == "1":
        productos_bajos(inventario)
    elif op == "2":
        valor_total(inventario)
    elif op == "3":
        top_3_vendidos(inventario)
    elif op == "4":
        ticket_promedio_y_total(ventas_dia)
    else:
        print("❌ Opción inválida.")

def main():
    inventario = cargar_datos(RUTA)
    ventas_dia = []

    while True:
        menu()
        op = input("Elige una opción: ")

        if op == "1":
            mostrar_inventario(inventario)

        elif op == "2":
            codigo = input_no_vacio("Código: ")
            if busqueda_binaria_por_codigo(sorted(inventario, key=lambda x: x['codigo']), codigo):
                print("❌ Código duplicado.")
                continue
            nombre = input_no_vacio("Nombre: ")
            precio = input_flotante("Precio: ", 0)
            stock = input_entero("Stock inicial: ", 0)
            stock_min = input_entero("Stock mínimo: ", 0)
            nuevo = {'codigo': codigo, 'nombre': nombre, 'precio': precio,
                     'stock': stock, 'stock_minimo': stock_min, 'vendidos_hoy': 0}
            agregar_producto(inventario, nuevo)

        elif op == "3":
            eliminar_producto(inventario, input_no_vacio("Código a eliminar: "))

        elif op == "4":
            actualizar_stock(inventario, input_no_vacio("Código: "), input_entero("Nuevo stock: ", 0))

        elif op == "5":
            codigo = input_no_vacio("Código: ")
            cant = input_entero("Cantidad a vender: ", 1)
            monto = vender_producto(inventario, codigo, cant)
            if monto:
                ventas_dia.append(monto)

        elif op == "6":
            menu_reportes(inventario, ventas_dia)

        elif op == "7":
            guardar_datos(RUTA, inventario)
            guardar_binario(BINARIO, inventario)
            exportar_alertas(inventario)
            print("✅ Datos guardados. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
6