inventario = {}
cantidad_productos = int(input("Ingrese la cantidad de productos que desea ingresar: "))
for i in range(cantidad_productos):
    while True:
        codigo = input("Ingrese el código del producto: ")
        if codigo not in inventario:
            break
        else:
            print("Este código ya existe, ingrese otro")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("CATEGORÍAS\n- Hombre\n- Mujer\n- Niño\n¿Qué categoría es?: ")
    talla = input("TALLAS\nS\nM\nL\nXL\nIngrese la talla: ")
    while True:
        precio = float(input("Ingrese el precio unitario del producto: "))
        if precio <= 0:
            print("El precio debe ser mayor a Q0.00")
        else:
            break
    while True:
        stock = int(input("¿Cuánt@s hay en stock?: "))
        if stock <= 0:
            print("El stock debe ser una cantidad positiva")
        else:
            break
    inventario[codigo] = [nombre, categoria, talla, precio, stock]
while True:
    print("---OPCIONES---\n"
          "1.- Mostrar lista completa de productos\n"
          "2.- Mostrar detalles de un producto por su código\n"
          "3.- Calcular valor total del inventario\n"
          "4.- Mostrar cuántos productos hay por cada categoría\n"
          "5.- Salir")
    opciones = input("Ingrese el número de la opción que desea seleccionar: ")
    match opciones:
        case "1":
            print("---MOSTRAR LISTA COMPLETA DE PRODUCTOS---\n")
            for cod, datos in inventario.items():
                print(f"{cod}: {datos}")
        case "2":
            print("---MOSTRAR DETALLES DE PRODUCTOS POR SU CÓDIGO---\n")
            buscar_codigo = input("Ingrese un código para ver sus detalles: ")
            if buscar_codigo in inventario:
                print("Detalles del producto:", inventario[buscar_codigo])
            else:
                print("Producto no encontrado")
        case "3":
            print("---CALCULAR VALOR TOTAL DE INVENTARIO---\n")
            suma_total = sum(p[3] * p[4] for p in inventario.values())
            print(f"Valor total del inventario: Q{suma_total:.2f}")
        case "4":
            print("---MOSTRAR CUÁNTOS PRODUCTOS HAY POR CADA CATEGORÍA---\n")
            categorias = {}
            for p in inventario.values():
                cat = p[1]
                if cat in categorias:
                    categorias[cat] += 1
                else:
                    categorias[cat] = 1
            print("Cantidad de productos por categoría:")
            for cat, cant in categorias.items():
                print(f"{cat}: {cant}")
        case "5":
            print("Gracias por utilizar el programa. Programa terminado.")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
