print ("Sistema de Reservas para Hotel")
opcion = 0
reservar_habitaciones = 0
habitaciones = 20
habitacion_final = 0
lista = []


def Registrar_Huespedes():
    cedula = int(input("Digite su cedula"))
    nombre = str(input("Digite su nombre"))
    edad = int(input("Digite su edad"))
    numero = int(input("Digite su numero de telefono"))
    registros = (cedula, nombre, edad, numero)
    lista.append(registros)
    print ("Registro exitoso")

def Reservar_Habitaciones():
    global habitaciones
    global reservar_habitaciones
    reservar_habitaciones = int(input("¿Cuantas habitaciones desea reservar?"))
    if reservar_habitaciones == habitaciones:
        print("Reserva de manera exitosa")
    elif reservar_habitaciones < habitaciones:
        print("Reserva de manera exitosa")
    else:
        print("No hay habitaciones suficientes")

def Consultar_Disponibilidad():
    global habitaciones
    global reservar_habitaciones
    global habitacion_final
    habitacion_final = habitaciones - reservar_habitaciones
    print("La cantidad de habitaciones disponible es: ",habitacion_final )

def Cancelar_Reservas():
    global reservar_habitaciones

    cancelar = input("¿Desea cancelar la reserva? Si/No: ")

    if cancelar.lower() == "si":
        reservar_habitaciones = 0
        print("Se canceló de manera exitosa")
    else:
        print("Se rechazó la cancelación de la reserva")

def Calcular_Hospedaje():
    global reservar_habitaciones
    precio = 100000
    total = 100000 * reservar_habitaciones
    print("El total es: ", total)


opcion = 0
while opcion != 6:
    print("1. Registrar Huespedes")
    print("2. Reservar Habitaciones")
    print("3. Consultar Disponibilidad")
    print("4. Cancelar Reservas" )
    print("5. Calcular Hospedaje")
    print("6. salir")

    opcion = int(input("Elije una opcion"))


    if opcion == 1:
        Registrar_Huespedes()
    elif opcion == 2:
        Reservar_Habitaciones()
    elif opcion == 3:
        Consultar_Disponibilidad()
    elif opcion == 4:
        Cancelar_Reservas()
    elif opcion == 5:
        Calcular_Hospedaje()
    elif opcion == 6:
        print("Saliendo del sistema...")
    else:
        print("opcion invalida")

