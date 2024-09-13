
from productos.gestion_producto import menu_producto
from clientes.gestion_clientes import menu_clientes
from venta import menu_ventas




def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar productos")
        print("2. Gestionar clientes")
        print("3. venta de producto")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            menu_producto()  
        elif opcion == '2':
            menu_clientes()  
        elif opcion == '3':
            menu_ventas()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break  
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()



