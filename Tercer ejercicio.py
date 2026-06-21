
lista = []
def registrar_producto():
    nombre = input("Digita el nombre del producto")
    precio = float(input("Digita el precio del producto"))
    cantidad = int(input("Digita la cantidad del producto"))
    producto = (nombre, precio, cantidad)
    lista.append(producto)

    print("Producto registrado correctamente")

def mostrar_productos():

    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lista) == 0:
        print("No hay productos registrados.")
    else:

        for producto in lista:

            print("Nombre:", producto[0])
            print("Precio:", producto[1])
            print("Cantidad:", producto[2])
        

def Valor_Total():
    valor_total = 0

    for producto in lista:
        precio = producto[1]
        cantidad = producto[2]
        valor_total += precio * cantidad

    print("El valor total de los productos registrados es:", valor_total)


opcion = 0
while opcion !=4:
   print("1. Registrar Producto")
   print("2. Consultar Productos")
   print("3. Valor total")
   print("4. salir")

   opcion = int(input("Seleccione una opcion: "))

   if opcion == 1:
    registrar_producto()
   elif opcion == 2:
    mostrar_productos()
   elif opcion == 3:
    Valor_Total()
   elif opcion == 4:
    print("Saliendo del sistema")
   else:
    print("Opcion Invalida")