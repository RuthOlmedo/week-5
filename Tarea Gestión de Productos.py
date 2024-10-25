productos = []

def añadir_producto():
    # Lógica para añadir un producto
    producto={
        "nombre":"",
        "precio":"",
        "cantidad":"",
    }
    for i in producto.keys():
        while True:
            producto[i]=input(f"{i}: ")
            if i=="precio" or i=="cantidad":
                try:
                    producto[i]=int(producto[i])
                    break
                except ValueError:
                    print("Por favor, ingresa un valor numerico.")
            else:
                break
    productos.append(producto.copy())
    return productos

def ver_productos():
    # Lógica para ver todos los productos
    for producto in productos:
        print(producto)


def actualizar_producto():
    # Pedir al usuario el nombre del producto a actualizar
    organizar = input("nombre del producto?: ")

    for producto in productos:
        if producto["nombre"] == organizar:
            print(f"Actualizando el producto: {producto['nombre']}")
            for clave in producto.keys():
                while True:
                    nuevo_valor = input(f"{clave} (actual: {producto[clave]}): ")
                    if clave=="precio" or clave=="cantidad":
                        try:
                            nuevo_valor=int(nuevo_valor)
                            break
                        except ValueError:
                            print("Por favor, ingresa un valor numerico.")
                    else:
                        break
                producto[clave] = nuevo_valor
            print("Producto actualizado.")
            break
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    # Lógica para eliminar un producto
    name=input("cual es el nombre del producto que quieres eliminar? ")
    for producto in productos:
        if producto["nombre"] == name:
            productos.remove(producto)
            break
    else:
        print("Producto no encontrado.")

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)

    print("Datos guardados en productos.txt.")


def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open("productos.txt", "r") as archivo:  # Abrir el archivo en modo lectura
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")  # Separar por comas
                producto = {
                    "nombre": nombre,
                    "precio": int(precio),  # Convertir el precio a entero
                    "cantidad": int(cantidad)  # Convertir la cantidad a entero
                }
                productos.append(producto)  # Añadir el producto a la lista
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("El archivo productos.txt no existe. Comenzando con lista vacía.")


def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
cargar_datos()
menu()