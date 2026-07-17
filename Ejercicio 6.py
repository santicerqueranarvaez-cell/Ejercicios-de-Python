
lista = []
def Registrar_Libros():
    codigo = input ("Digite el codigo del libro")
    nombre = input("Digite el nombre del libro") 
    catalogo = input("Digite el catalogo del libro")
    registro_libro = (codigo, nombre, catalogo)
    lista.append (registro_libro)
    print("Libro registrado correctamente")

def Registrar_Estudiantes():
    nombre = input("Digite el nombre del estudiante")
    edad = input("Digita tu edad")
    cedula = input("Digite la cedula")
    registro_estudiante = (nombre, edad, cedula)
    lista.append (registro_estudiante)
    print("Estudiante registrado correctamente")

def prestamos():
    prestamo = input("Desea un prestamo Si/No")
    if prestamo == "si":
        print("Prestamo realizado de manera correcta")
    else:
        print("El prestamo no se realizo correctamante")

def devoluciones():
    devolucion = input("Desea un prestamo Si/No")
    if devolucion == "si":
        print("Prestamo realizado de manera correcta")
    else:
        print("El prestamo no se realizo correctamante")

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
    print("1. Registrar Libros")
    print("2. Registrar Estudiantes")
    print("3. Prestamos")
    print("4. Devoluciones")
    print("5. Consultar Inventario")
    print("6. Salir")

    opcion = int(input("Elija una opcion"))

    if opcion == 1:
     Registrar_Libros()
    elif opcion == 2:
     Registrar_Estudiantes()
    elif opcion == 3:
     prestamos()
    elif opcion == 4:
     devoluciones()
    elif opcion == 5:
     Consultar_Inventario()
    elif opcion == 6:
     print("Saliendo del sistema")
    else:
     print("Opcion Invalida")




