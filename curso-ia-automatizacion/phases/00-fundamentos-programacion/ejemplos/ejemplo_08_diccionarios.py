# ============================================================================
# EJEMPLO 08: DICCIONARIOS - DATOS ESTRUCTURADOS
# ============================================================================
# Tema: Estructuras de datos - Diccionarios
# Objetivo: Organizar datos con clave-valor
# Nivel: Intermedio
# Prerrequisito: ejemplo_07_listas.py

print("=== SISTEMA DE INVENTARIO DE TIENDA ===")

# Inicializar inventario como diccionario
inventario = {}

# Función para mostrar el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print("\n=== INVENTARIO ACTUAL ===")
    print("-" * 50)
    print(f"{'Producto':<20} {'Cantidad':<10} {'Precio':<10} {'Total':<10}")
    print("-" * 50)
    
    total_valor_inventario = 0
    for producto, datos in inventario.items():
        cantidad = datos['cantidad']
        precio = datos['precio']
        total_producto = cantidad * precio
        total_valor_inventario += total_producto
        
        print(f"{producto:<20} {cantidad:<10} ${precio:<9.2f} ${total_producto:<9.2f}")
    
    print("-" * 50)
    print(f"Valor total del inventario: ${total_valor_inventario:.2f}")

# Función para agregar producto
def agregar_producto():
    nombre = input("Nombre del producto: ")
    
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe.")
        cantidad_adicional = int(input("¿Cuántas unidades agregar? "))
        inventario[nombre]['cantidad'] += cantidad_adicional
        print(f"Se agregaron {cantidad_adicional} unidades de '{nombre}'")
    else:
        cantidad = int(input("Cantidad inicial: "))
        precio = float(input("Precio por unidad: $"))
        categoria = input("Categoría: ")
        
        inventario[nombre] = {
            'cantidad': cantidad,
            'precio': precio,
            'categoria': categoria
        }
        print(f"Producto '{nombre}' agregado al inventario")

# Función para buscar producto
def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"\n=== INFORMACIÓN DE '{nombre.upper()}' ===")
        print(f"Cantidad disponible: {datos['cantidad']} unidades")
        print(f"Precio por unidad: ${datos['precio']:.2f}")
        print(f"Categoría: {datos['categoria']}")
        print(f"Valor total: ${datos['cantidad'] * datos['precio']:.2f}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario")

# Función para vender producto
def vender_producto():
    nombre = input("Producto a vender: ")
    
    if nombre not in inventario:
        print(f"El producto '{nombre}' no existe en el inventario")
        return
    
    cantidad_vender = int(input("Cantidad a vender: "))
    cantidad_disponible = inventario[nombre]['cantidad']
    
    if cantidad_vender > cantidad_disponible:
        print(f"No hay suficiente stock. Disponible: {cantidad_disponible}")
        return
    
    # Realizar venta
    precio_unitario = inventario[nombre]['precio']
    total_venta = cantidad_vender * precio_unitario
    
    inventario[nombre]['cantidad'] -= cantidad_vender
    
    print("\n=== RECIBO DE VENTA ===")
    print(f"Producto: {nombre}")
    print(f"Cantidad vendida: {cantidad_vender}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Total de la venta: ${total_venta:.2f}")
    
    # Si se agotó el producto, preguntar si eliminarlo
    if inventario[nombre]['cantidad'] == 0:
        eliminar = input(f"'{nombre}' se agotó. ¿Eliminarlo del inventario? (s/n): ")
        if eliminar.lower() == 's':
            del inventario[nombre]
            print(f"'{nombre}' eliminado del inventario")

# Función para estadísticas por categoría
def estadisticas_categoria():
    if not inventario:
        print("No hay productos en el inventario")
        return
    
    categorias = {}
    
    # Agrupar por categoría
    for producto, datos in inventario.items():
        categoria = datos['categoria']
        if categoria not in categorias:
            categorias[categoria] = {
                'productos': 0,
                'cantidad_total': 0,
                'valor_total': 0
            }
        
        categorias[categoria]['productos'] += 1
        categorias[categoria]['cantidad_total'] += datos['cantidad']
        categorias[categoria]['valor_total'] += datos['cantidad'] * datos['precio']
    
    print("\n=== ESTADÍSTICAS POR CATEGORÍA ===")
    for categoria, stats in categorias.items():
        print(f"\n{categoria.upper()}:")
        print(f"  Productos diferentes: {stats['productos']}")
        print(f"  Unidades totales: {stats['cantidad_total']}")
        print(f"  Valor total: ${stats['valor_total']:.2f}")

# Programa principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Ver inventario completo")
    print("3. Buscar producto")
    print("4. Vender producto")
    print("5. Estadísticas por categoría")
    print("6. Productos con bajo stock")
    print("7. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        vender_producto()
    elif opcion == "5":
        estadisticas_categoria()
    elif opcion == "6":
        # Productos con bajo stock
        limite = int(input("¿Cuál consideras bajo stock? (cantidad): "))
        productos_bajo_stock = []
        
        for producto, datos in inventario.items():
            if datos['cantidad'] <= limite:
                productos_bajo_stock.append((producto, datos['cantidad']))
        
        if productos_bajo_stock:
            print(f"\n=== PRODUCTOS CON STOCK ≤ {limite} ===")
            for producto, cantidad in productos_bajo_stock:
                print(f"⚠️  {producto}: {cantidad} unidades")
        else:
            print(f"No hay productos con stock menor o igual a {limite}")
            
    elif opcion == "7":
        print("¡Gracias por usar el sistema de inventario!")
        break
    else:
        print("Opción no válida")

# Ejercicio: Implementar descuentos por cantidad en las ventas