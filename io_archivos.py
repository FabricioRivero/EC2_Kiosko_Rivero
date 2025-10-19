import csv, pickle

def cargar_datos(ruta):
    inventario = []
    try:
        with open(ruta, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                inventario.append({
                    'codigo': r['codigo'],
                    'nombre': r['nombre'],
                    'precio': float(r['precio']),
                    'stock': int(r['stock']),
                    'stock_minimo': int(r['stock_minimo']),
                    'vendidos_hoy': int(r.get('vendidos_hoy', 0))
                })
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado, se iniciará vacío.")
    return inventario

def guardar_datos(ruta, inventario):
    campos = ['codigo','nombre','precio','stock','stock_minimo','vendidos_hoy']
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(inventario)

def guardar_binario(ruta, inventario):
    with open(ruta, 'wb') as f:
        pickle.dump(inventario, f)

def exportar_alertas(inventario, ruta="alertas.csv"):
    bajos = [p for p in inventario if p['stock'] < p['stock_minimo']]
    if bajos:
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            campos = ['codigo', 'nombre', 'precio', 'stock', 'stock_minimo', 'vendidos_hoy']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for p in bajos:
                # Solo escribir los campos relevantes
                fila = {c: p[c] for c in campos}
                writer.writerow(fila)
        print(f"📤 Se exportaron {len(bajos)} productos a '{ruta}'.")
    else:
        print("✅ No hay productos bajo el stock mínimo.")
