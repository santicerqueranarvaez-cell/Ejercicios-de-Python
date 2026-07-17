Total_Ventas = 0
Cantidad_Ventas = 0
opcion = 0
encontrado = 0
lista = []

def Registrar_Productos():
    nombre = str(input("Digite el nombre del producto:"))
    codigo = int(input("Digite el codigo"))
    precio = int(input("Digite el precio"))
    cantidad = int(input("Digite la cantidad del producto"))
    producto = (nombre, codigo, precio, cantidad, 0)
    lista.append(producto)
    print("Se registro correctamente el producto")

def Realizar_Venta():
    global Total_Ventas
    global Cantidad_Ventas

    codigo_buscar = input("Ingrese el codigo del producto: ")

    encontrado = False

    for i in range(len(lista)):

        producto = lista[i]

        if producto[1] == codigo_buscar:

            encontrado = True

            print("Producto encontrado:", producto[0])

            cantidad_compra = int(input("Cantidad a comprar: "))

            stock = producto[3]

            
        if cantidad_compra >= stock:

         subtotal = producto[2] * cantidad_compra
         iva = subtotal * 0.19
         total = subtotal + iva
         subtotal = producto[2]
         iva = subtotal * 0.19
         total = subtotal + iva

         nuevo_stock = stock - cantidad_compra

            
         lista[i] = (
         producto[0],
         producto[1],
         producto[2],
         nuevo_stock
         )

         Total_Ventas += total
         Cantidad_Ventas += 1

         print("Producto:", producto[0])
         print("Cantidad:", cantidad_compra)
         print("Subtotal: $", subtotal)
         print("IVA: $", round(iva, 2))
         print("TOTAL: $", round(total, 2))

        else:
            print("No hay suficiente stock")


if encontrado == False:
    print("Producto no encontrado.")

def producto_mas_vendido():
    mayor = 0
    nombre_mayor = ""

    for producto in lista:
        ventas = producto[4]
        if ventas > mayor:
            mayor = ventas 
            nombre_mayor = producto[0]
            print ("Producto mas vendido", nombre_mayor)
            print ("Cantidad de producto", mayor)


    
def Consultar_Inventario():

    if len(lista) == 0:
        print("No hay productos Registrados")

    else:
        for producto in lista:

          print("El nombre del producto es:", producto[0])
          print("El codigo del producto es:", producto[1])
          print("El precio del producto es:", producto[2])
          print("La cantidad del producto es:", producto[3])




while opcion != 6:
    print ("1. Registrar Productos")
    print ("2. Realizar Venta")
    print ("3. Consultar inventario")
    print ("4. Producto Mas Vendido")
    print ("5. Salir")


    opcion = int(input("Digite una opcion"))
    
    if opcion == 1:
        Registrar_Productos()
    elif opcion == 2:
        Realizar_Venta()
    elif opcion == 3:
        Consultar_Inventario()
    elif opcion == 4:
        producto_mas_vendido()
    elif opcion == 5:
        print("Salir del sistema")
    else:
        print("Opcion Incorrecta")
    




