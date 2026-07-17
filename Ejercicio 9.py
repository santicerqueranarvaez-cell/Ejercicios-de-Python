lista = []
opcion = 0



def registrarEstudiantes():
    nombre = input("Registrar nombre del estudiante: ")
    grado = int(input("Registre el grado del estudiante: "))
    documento = int(input("Registre el documento del estudiante: "))
    nota1 = float(input("Digite la nota 1: "))
    nota2 = float(input("Digite la nota 2: "))
    nota3 = float(input("Digite la nota 3: "))
    promedio = (nota1 + nota2 + nota3) / 3
    estudiante = (nombre, grado, documento, nota1, nota2, nota3, promedio)

    lista.append(estudiante)
    print("Registrado Correctamente")

def  Promedios_Finales():
   for estudiante in lista:
       print("Nombre es:", estudiante[0])
       print("Promedio:", estudiante[6])
      
   

def reportesAcademicos():
   for estudiante in lista:
      print("Nombre es: ", estudiante[0])
      print("Grado es: ", estudiante[1])
      print("El documento es: ", estudiante[2])
      print("Primera nota es: ", estudiante[3])
      print("Segunda nota es: ", estudiante[4])
      print("Tercera nota es: ", estudiante[5])
      print("El promedio final es: ", estudiante[6])

      

while opcion != 5:
   print("1. Registrar Estudiantes")
   print("2. Promedios")
   print("3. Reportes Academicos")
   print("4. Salir")
   opcion = int(input("Elija una opcion: "))

   if opcion == 1:
     registrarEstudiantes()
   elif opcion == 2:
     Promedios_Finales()
   elif opcion == 3:
     reportesAcademicos()
   elif opcion == 4:
     print("Salir")
   else:
     print("Error del sistema")


   
