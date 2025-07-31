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
    categoria = input("CATEGORIAS\n"
                      "-Hombre\n"
                      "-Mujer\n"
                      "-Niño\n"
                      "¿Qué categoria es?: ")
    talla = input("TALLAS\n"
                  "S\n"
                  "M\n"
                  "L\n"
                  "XL\n"
                  "Ingrese la talla: ")
