def buscar_por_nombre(inventario, nombre):
    encontrados = [p for p in inventario if nombre.lower() in p['nombre'].lower()]
    if encontrados:
        for p in encontrados:
            print(f"{p['codigo']} | {p['nombre']} | {p['stock']}u | Bs {p['precio']}")
    else:
        print("⚠️ No encontrado.")

def busqueda_binaria_por_codigo(lista_ordenada, codigo):
    izq, der = 0, len(lista_ordenada) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if lista_ordenada[mid]['codigo'] == codigo:
            return lista_ordenada[mid]
        elif lista_ordenada[mid]['codigo'] < codigo:
            izq = mid + 1
        else:
            der = mid - 1
    return None

def ordenar_burbuja_por_precio(lista, descendente=False):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (lista[j]['precio'] > lista[j+1]['precio']) ^ descendente:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
