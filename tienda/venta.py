# from productos.gestion_producto import productos  # Importar la lista de productos

# ventas = []  # Lista para almacenar las ventas

# def mostrar_productos():
#     if len(productos) == 0:
#         print("No hay productos disponibles para la venta.")
#     else:
#         print("\n--- Productos Disponibles ---")
#         for i, producto in enumerate(productos, 1):
#             print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}")
#     return len(productos)

# def vender_producto():
#     if mostrar_productos() == 0:
#         return  # Si no hay productos, no se puede hacer una venta

#     try:
#         indice = int(input("Selecciona el número del producto que deseas vender: ")) - 1
#         if indice < 0 or indice >= len(productos):
#             print("Producto no válido.")
#             return

#         cantidad = int(input(f"¿Cuántas unidades de {productos[indice]['nombre']} deseas vender? "))
#         if cantidad <= 0:
#             print("Cantidad no válida.")
#             return

#         total = productos[indice]['precio'] * cantidad
#         venta = {
#             'producto': productos[indice]['nombre'],
#             'precio_unitario': productos[indice]['precio'],
#             'cantidad': cantidad,
#             'total': total
#         }
#         ventas.append(venta)
#         print(f"Venta registrada: {cantidad} unidades de {productos[indice]['nombre']} por un total de {total:.2f}")

#     except ValueError:
#         print("Entrada no válida. Por favor ingresa un número.")

# def listar_ventas():
#     if len(ventas) == 0:
#         print("No se han registrado ventas.")
#     else:
#         print("\n--- Historial de Ventas ---")
#         for i, venta in enumerate(ventas, 1):
#             print(f"{i}. Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Total: {venta['total']:.2f}")

# def menu_ventas():
#     while True:
#         print("\n--- GESTIÓN DE VENTAS ---")
#         print("1. Vender producto")
#         print("2. Listar ventas")
#         print("3. Volver al menú principal")

#         opcion = input("Elige una opción: ")

#         if opcion == '1':
#             vender_producto()  # Llama a la función para vender un producto
#         elif opcion == '2':
#             listar_ventas()  # Llama a la función para listar las ventas
#         elif opcion == '3':
#             print("Volviendo al menú principal...")
#             break  # Sale del bucle para volver al menú principal
#         else:
#             print("Opción no válida. Intenta de nuevo.")





from productos.gestion_producto import productos 
from clientes.gestion_clientes import clientes 

ventas = []  

def mostrar_productos():
    if len(productos) == 0:
        print("No hay productos disponibles para la venta.")
    else:
        print("\n--- Productos Disponibles ---")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}")
    return len(productos)

def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        print("\n--- Clientes Registrados ---")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}")
    return len(clientes)

def vender_producto():
    if mostrar_clientes() == 0:
        print("Primero debes registrar clientes.")
        return 

    try:
        indice_cliente = int(input("Selecciona el número del cliente que está comprando: ")) - 1
        if indice_cliente < 0 or indice_cliente >= len(clientes):
            print("Cliente no válido.")
            return

        if mostrar_productos() == 0:
            return  

        indice_producto = int(input("Selecciona el número del producto que deseas vender: ")) - 1
        if indice_producto < 0 or indice_producto >= len(productos):
            print("Producto no válido.")
            return

        cantidad = int(input(f"¿Cuántas unidades de {productos[indice_producto]['nombre']} deseas vender? "))
        if cantidad <= 0:
            print("Cantidad no válida.")
            return

        total = productos[indice_producto]['precio'] * cantidad
        venta = {
            'cliente': clientes[indice_cliente]['nombre'],
            'producto': productos[indice_producto]['nombre'],
            'precio_unitario': productos[indice_producto]['precio'],
            'cantidad': cantidad,
            'total': total
        }
        ventas.append(venta)
        print(f"Venta registrada: {cantidad} unidades de {productos[indice_producto]['nombre']} a {clientes[indice_cliente]['nombre']} por un total de {total:.2f}")

    except ValueError:
        print("Entrada no válida. Por favor ingresa un número.")

def listar_ventas():
    if len(ventas) == 0:
        print("No se han registrado ventas.")
    else:
        print("\n--- Historial de Ventas ---")
        for i, venta in enumerate(ventas, 1):
            print(f"{i}. Cliente: {venta['cliente']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Total: {venta['total']:.2f}")

def menu_ventas():
    while True:
        print("\n--- GESTIÓN DE VENTAS ---")
        print("1. Vender producto")
        print("2. Listar ventas")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            vender_producto() 
        elif opcion == '2':
            listar_ventas() 
        elif opcion == '3':
            print("Volviendo al menú principal...")
            break  
        else:
            print("Opción no válida. Intenta de nuevo.")
