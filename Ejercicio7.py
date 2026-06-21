print("Sistema de ventas")

valores_totales = 0
Total_Ventas = 0
Cantidad_Ventas = 0
total = 0


lista = []

def Registrar_Productos():
    nombre = str(input("Digita el nombre del producto"))
    codigo = int(input("Digita el codigo del producto"))
    precio = float(input("Digite el precio del producto"))
    cantidad = int(input("Digite la cantidad del producto"))
    producto = (codigo, nombre, precio, cantidad)
    lista.append(producto)
    print ("Producto Registrado correctamente")

def Realizar_Ventas():
    global Total_Ventas
    global Cantidad_Ventas

    print("\n--- REALIZAR VENTA ---")

    codigo_buscar = input("Ingrese el codigo del producto: ")

    encontrado = False

    # Recorrer productos
    for i in range(len(lista)):

        producto = lista[i]

        if producto[0] == codigo_buscar:

            encontrado = True

            print("Producto encontrado:", producto[1])

            cantidad_compra = int(input("Cantidad a comprar: "))

            stock = producto[3]

            # Validar stock
            if cantidad_compra <= stock:

                subtotal = producto[2] * cantidad_compra
                iva = subtotal * 0.19
                total = subtotal + iva

                nuevo_stock = stock - cantidad_compra

                # Actualizar producto
                lista[i] = (
                    producto[0],
                    producto[1],
                    producto[2],
                    nuevo_stock
                )

                Total_Ventas += total
                Cantidad_Ventas += 1

                print("\n======= FACTURA =======")
                print("Producto:", producto[1])
                print("Cantidad:", cantidad_compra)
                print("Subtotal: $", subtotal)
                print("IVA: $", round(iva, 2))
                print("TOTAL: $", round(total, 2))
                print("=======================\n")

            else:
                print("No hay suficiente stock.")

    if encontrado == False:
        print("Producto no encontrado.")

def Valores_Totales():
    valores_totales = Total_Ventas
    print("El valor total es: ",valores_totales)

def Resumen_Transacciones():
    print("\n--- REPORTE DIARIO ---")

    print("Cantidad de ventas:", cantidad_ventas)
    print("Total vendido: $", round(total_ventas, 2))

    if cantidad_ventas > 0:

        promedio = total_ventas / cantidad_ventas

        print("Promedio por venta: $", round(promedio, 2))

    else:
        print("No hay ventas registradas.")




def Consultar_Inventario():
     if len(lista) == 0:
        print("No hay registrados.")

     else:
        for producto in lista:

            print("Codigo:", producto[0])
            print("Nombre:", producto[1])
            print("Catalago:", producto[2])


opcion = 0

while opcion != 6:
    print("1. Registrar Productos")
    print("2. Realizar Ventas")
    print("3. Valores Totales")
    print("4. Resumen Transacciones")
    print("5. Consultar Inventario")
    print("6. Salir")

    opcion = int(input("Elija una opcion"))

    if opcion == 1:
     Registrar_Productos()
    elif opcion == 2:
     Realizar_Ventas()
    elif opcion == 3:
     Valores_Totales()
    elif opcion == 4:
     Resumen_Transacciones()
    elif opcion == 5:
     Consultar_Inventario()
    elif opcion == 6:
     print("Saliendo del sistema")
    else:
     print("Opcion Invalida")

































