def buscar_por_nombre(inventario, nombre):
    print(f"\n🔍 Resultados de búsqueda para: {nombre}")
    encontrados = [p for p in inventario if nombre.lower() in p['nombre'].lower()]
    if encontrados:
        for p in encontrados:
            print(f"{p['codigo']} | {p['nombre']} | {p['categoria']} | {p['cantidad']} unidades | Bs {p['precio']}")
    else:
        print("⚠️ No se encontraron productos con ese nombre.")


def buscar_por_categoria(inventario, categoria):
    print(f"\n📂 Productos en la categoría: {categoria}")
    encontrados = [p for p in inventario if categoria.lower() in p['categoria'].lower()]
    if encontrados:
        for p in encontrados:
            print(f"{p['codigo']} | {p['nombre']} | {p['categoria']} | {p['cantidad']} unidades | Bs {p['precio']}")
    else:
        print("⚠️ No se encontraron productos en esa categoría.")


def ordenar_por_precio(inventario, descendente=False):
    print("\n💲 Inventario ordenado por precio:")
    lista_ordenada = sorted(inventario, key=lambda x: x['precio'], reverse=descendente)
    for p in lista_ordenada:
        print(f"{p['nombre']} | {p['precio']} Bs | {p['cantidad']} unidades")
    return lista_ordenada


def ordenar_por_cantidad(inventario, descendente=False):
    print("\n📦 Inventario ordenado por cantidad:")
    lista_ordenada = sorted(inventario, key=lambda x: x['cantidad'], reverse=descendente)
    for p in lista_ordenada:
        print(f"{p['nombre']} | {p['cantidad']} unidades | Bs {p['precio']}")
    return lista_ordenada
