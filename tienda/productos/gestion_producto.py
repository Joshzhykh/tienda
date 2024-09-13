 

productos = []  
def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    producto = {'nombre': nombre, 'precio': precio}
    productos.append(producto)
    print(f"Producto {nombre} agregado correctamente.")

def listar_productos():
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        print("\n--- Lista de Productos ---")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}")

def buscar_producto():
    nombre = input("Ingresa el nombre del producto a buscar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']} - Precio: {producto['precio']}")
            return
    print("Producto no encontrado.")

def menu_producto():
    while True:
        print("\n--- GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_producto() 
        elif opcion == '2':
            listar_productos()  
        elif opcion == '3':
            buscar_producto()  
        elif opcion == '4':
            print("Volviendo al menú principal...")
            break  
        else:
            print("Opción no válida. Intenta de nuevo.")

