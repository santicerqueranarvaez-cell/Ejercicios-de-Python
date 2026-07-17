
agenda = []

def Registrar_Paciente():

    nombre = input("Digite el nombre del paciente: ")
    documento = int(input("Digite el documento: "))
    fecha = input("Digite la fecha (dd/mm/aaaa): ")
    hora = input("Digite la hora: ")

    encontrado = False

    for cita in agenda:
        if cita[2] == fecha and cita[3] == hora:
            encontrado = True

    if encontrado == True:
        print("Ese horario ya está ocupado.")
    else:
        paciente = (nombre, documento, fecha, hora)
        agenda.append(paciente)
        print("Cita registrada correctamente.")


def Consultar_Horarios():

    fecha = input("Digite la fecha a consultar: ")

    encontrado = False

    print("Horarios ocupados:")

    for cita in agenda:
        if cita[2] == fecha:
            print(cita[3])
            encontrado = True

    if encontrado == False:
        print("No hay citas registradas para esa fecha.")


def Cancelar_Cita():

    documento = int(input("Digite el documento del paciente: "))

    encontrado = False

    for cita in agenda:
        if cita[1] == documento:
            agenda.remove(cita)
            encontrado = True
            print("Cita cancelada correctamente.")
            break

    if encontrado == False:
        print("No se encontró una cita con ese documento.")


def Agenda_Diaria():

    if len(agenda) == 0:
        print("No hay citas registradas.")
    else:
        print("\n===== AGENDA MÉDICA =====")

        for cita in agenda:
            print("Paciente:", cita[0])
            print("Documento:", cita[1])
            print("Fecha:", cita[2])
            print("Hora:", cita[3])


opcion = 0

while opcion != 5:

    print("1. Registrar paciente y programar cita")
    print("2. Consultar horarios disponibles")
    print("3. Cancelar cita")
    print("4. Visualizar agenda médica")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        Registrar_Paciente()

    elif opcion == 2:
        Consultar_Horarios()

    elif opcion == 3:
        Cancelar_Cita()

    elif opcion == 4:
        Agenda_Diaria()

    elif opcion == 5:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida.")