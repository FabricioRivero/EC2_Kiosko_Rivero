# main.py (versión corregida: precio y cantidad > 0, chequear código duplicado antes)
from io_archivos import cargar_datos, guardar_datos
from inventario import agregar_producto, eliminar_producto, actualizar_stock, buscar_producto
from reportes import mostrar_inventario, productos_bajos, valor_total
from busquedas_ordenamiento import buscar_por_nombre, buscar_por_categoria, ordenar_por_precio, ordenar_por_cantidad

RUTA = "datos.csv"

# ----------------- funciones de validación -----------------
def input_no_vacio(mensaje):
    """Pide un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("⚠️ Este campo no puede estar vacío.")
        else:
            return valor

def input_entero_positivo(mensaje):
    """Pide un número entero estrictamente mayor que 0."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("⚠️ Debe ser un número entero mayor a 0. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("❌ Ingrese un número entero válido (ejemplo: 5).")

def input_flotante_mayor_cero(mensaje):
    """Pide un número decimal estrictamente mayor que 0."""
    while True:
        try:
            valor = float(input(mensaje))
            # Rechazar 0 y negativos
            if valor <= 0:
                print("⚠️ Debe ser un valor mayor a 0. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("❌ Ingrese un número decimal válido (ejemplo: 5.50).")
# ------------------------------------------------------------

def menu():
    print("""
===== 🏫 KIOSKO UNIVERSITARIO UCB =====
1. Ver inventario
2. Agregar producto
3. Eliminar producto
4. Actualizar stock
5. Reporte de productos con bajo stock
6. Calcular valor total del inventario
7. Buscar producto
8. Ordenar inventario
9. Guardar y salir
""")

def main():
    inventario = cargar_datos(RUTA)

    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_inventario(inventario)

        elif opcion == '2':
            print("\n🆕 Agregar producto")
            # pedir código primero y verificar duplicado antes de continuar
            codigo = input_no_vacio("Código: ")
            if buscar_producto(inventario, codigo):
                print("❌ Ya existe un producto con ese código. Usa otro código o edita el producto existente.")
                continue   # vuelve al menú sin pedir más datos

            # si pasa la verificación del código, pedimos el resto con validaciones
            nombre = input_no_vacio("Nombre: ")
            categoria = input_no_vacio("Categoría: ")
            cantidad = input_entero_positivo("Cantidad (entero > 0): ")
            precio = input_flotante_mayor_cero("Precio (mayor a 0): ")

            nuevo = {
                'codigo': codigo,
                'nombre': nombre,
                'categoria': categoria,
                'cantidad': cantidad,
                'precio': precio
            }
            agregar_producto(inventario, nuevo)

        elif opcion == '3':
            print("\n🗑 Eliminar producto")
            codigo = input_no_vacio("Código a eliminar: ")
            eliminar_producto(inventario, codigo)

        elif opcion == '4':
            print("\n✏️ Actualizar stock")
            codigo = input_no_vacio("Código: ")
            if not buscar_producto(inventario, codigo):
                print("⚠️ No existe ese producto.")
                continue
            nueva_cantidad = input_entero_positivo("Nueva cantidad (entero > 0): ")
            actualizar_stock(inventario, codigo, nueva_cantidad)

        elif opcion == '5':
            productos_bajos(inventario)

        elif opcion == '6':
            valor_total(inventario)

        elif opcion == '7':
            print("\n1. Buscar por nombre")
            print("2. Buscar por categoría")
            sub = input("Elige una opción: ")
            if sub == '1':
                nombre = input_no_vacio("Nombre del producto: ")
                buscar_por_nombre(inventario, nombre)
            elif sub == '2':
                categoria = input_no_vacio("Nombre de la categoría: ")
                buscar_por_categoria(inventario, categoria)
            else:
                print("❌ Opción inválida.")

        elif opcion == '8':
            print("\n1. Ordenar por precio (ascendente)")
            print("2. Ordenar por precio (descendente)")
            print("3. Ordenar por cantidad (ascendente)")
            print("4. Ordenar por cantidad (descendente)")
            sub = input("Elige una opción: ")
            if sub == '1':
                ordenar_por_precio(inventario)
            elif sub == '2':
                ordenar_por_precio(inventario, True)
            elif sub == '3':
                ordenar_por_cantidad(inventario)
            elif sub == '4':
                ordenar_por_cantidad(inventario, True)
            else:
                print("❌ Opción inválida.")

        elif opcion == '9':
            guardar_datos(RUTA, inventario)
            print("✅ Cambios guardados. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
