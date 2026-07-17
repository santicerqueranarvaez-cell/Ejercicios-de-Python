
lista = []
def Registrar_Contacto():
    
    nombre = str(input("Digite su nombre: "))
    edad = int(input("Digite su edad: "))
    contacto = int(input("Digite su contacto: "))
    informacion = (nombre, edad, contacto)
    lista.append (informacion)
    print("Registrado Correctamente")

def Mostrar_Informacion():
    if len(lista) == 0:
      print("Ningun Contacto Registrado")
    else:
        for informacion in lista:
            print("El nombre de la persona es: ", informacion[0])
            print("Su edad es: ", informacion[1])
            print("Su contacto es: ", informacion[2] )

def Mostrar_Contactos():
    if len(lista) == 0:
        print("Ningun contacto esta registrado")
    else:
        for informacion in lista:
            print("Su contacto es:", informacion[2])


def Eliminar_Contactos():
    eliminar = int(input("Digite el contacto que quieres eliminar: "))
    encontrado = "no"
    for informacion in lista:
        if informacion[2] == eliminar:
            lista.remove(informacion)
            encontrado = "si"
            print("Contacto eliminado correctamente:")
        break
    if encontrado == "no":
        print("Contacto no encontrado")
        

opcion = 0
while opcion != 5:
    print("1. Registrar nuevo contactos")
    print("2. Mostrar informacion")
    print("3. Mostrar lista de contactos")
    print("4. Eliminar Contactos")
    print("5. Salir")

    opcion = int(input("Elija una opcion"))

    if opcion == 1:
        Registrar_Contacto()
    elif opcion == 2:
        Mostrar_Informacion()
    elif opcion == 3:
        Mostrar_Contactos()
    elif opcion == 4:
        Eliminar_Contactos()
    elif opcion == 5:
        print("saliendo del sistema")
    else:
        print("opcion invalida")


