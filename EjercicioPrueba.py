lista = []
promedio_final = 0



def datosEstudiante():
    global promedio_final
    global continuar
    nombre = str(input("Digite el nombre del estudiante"))
    nota1 = float(input("Digite la primera nota academica"))
    nota2 = float(input("Digite la segunda nota academica"))
    nota3 = float(input("Digite la tercera nota academica"))
    producto = (nombre, nota1, nota2, nota3)
    promedio_final = (nota1 + nota2 + nota3) / 3
    lista.append(producto) 
def Promedio():
    print("El promedio" , promedio_final)
    if promedio_final >= 3.0:
     print("aprueba")
    else:
       ("No Aprueba")

def mostrarLista():
   for elemento in lista:
      print("El nombre es: ", elemento[0])
      print("La nota1 es: ", elemento[1])
      print("La nota 2 es: ", elemento[2])
      print("La nota3 es: ", elemento[3])


opcion = 0

while opcion != 4:
   print("1. Datos del estudiante")
   print("2. Datos del promedio")
   print("3. mostrar lista")
   print("4. Salir")

   opcion = int(input("Digite una opcion: "))

   if opcion == 1:
      datosEstudiante()
   if opcion == 2:
      Promedio()
   if opcion == 3:
      mostrarLista()
   if opcion == 4:
      print("Salir") 
   else:
      print("Error del sistema")
     


   
   

