print("Bienvenido a la tienda Zulia")

lista_de_productos = []
lista_de_precios = []

while True:
    print("1. Agregar un nuevo elemento al carrito")
    print("2. Mostrar el contenido del carrito")
    print("3. Eliminar un elemento del carrito")
    print("4. Sumar el total")
    print("5. Salir")

    dato = input("Ingresa una de las opciones (1-5): ")

    if dato == "1":
        nombre_producto = input("Ingresa el nombre del producto: ")
        precio = float(input(f"¿Cuál es el precio de {nombre_producto}?: "))
        lista_de_productos.append(nombre_producto)
        lista_de_precios.append(precio)

    elif dato == "2":
        if lista_de_productos:
            print("Contenido del carrito:")
            for i in range(len(lista_de_productos)):
                print(f"{lista_de_productos[i]} - ${lista_de_precios[i]:.
                
    else:
     print("Opción no válida. Intenta de nuevo.")
