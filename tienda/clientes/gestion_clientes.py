# def menu_clientes():

#     while True:

#         print("\n ---GESTION DE CLIENTES")
#         print("1. agregar cliente")
#         print("2. listar cliente")
#         print("3. buscar cliente")
#         print("4. volver al menu")

#         opcion  = input("elige una opcion")


clientes = []  

def agregar_cliente():
    rut = input("ingresa el rut del cliente")
    nombre = input("Ingresa el nombre del cliente: ")
    telefono = input("Ingresa el teléfono del cliente: ")
    cliente = {'nombre': nombre, 'telefono': telefono, 'rut': rut}
    clientes.append(cliente)
    print(f"Cliente {nombre} agregado correctamente.")

def listar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        print("\n--- Lista de Clientes ---")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}, rut: {cliente['rut']}")

def buscar_cliente():
    nombre = input("Ingresa el nombre del cliente a buscar: ")
    for cliente in clientes:
        if cliente['nombre'].lower() == nombre.lower():
            print(f"Cliente encontrado: {cliente['nombre']} - Teléfono: {cliente['telefono']}, rut: {cliente['rut']}")
            return
    print("Cliente no encontrado.")

def menu_clientes():
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_cliente()  
        elif opcion == '2':
            listar_clientes()  
        elif opcion == '3':
            buscar_cliente()  
        elif opcion == '4':
            print("Volviendo al menú principal...")
            break  
        else:
            print("Opción no válida. Intenta de nuevo.")
