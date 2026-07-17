print("Registro academico de Estudiantes") 

lista = []
continuar = "si"
while continuar.lower () == "si":

   nombre = input("Ingrese su nombre")
   nota1 = float(input("ingrese su primera nota academica del 1 al 5"))
   nota2 = float(input("ingrese su segunda nota academica del 1 al 5 "))
   nota3 = float(input("ingrese su tercera nota academica del 1 al 5"))
   promedio_final = (nota1 + nota2 + nota3)/3
   producto = (nombre, nota1, nota2, nota3, promedio_final)
   continuar = input("Desea continuar si/no")
   lista.append(producto)    
for elemento in lista:
    print("Nombre es:", elemento[0])
    print("Primera nota es:", elemento[1])
    print("Segunda nota es:", elemento[2])
    print("Tercera nota es:", elemento[3])
    print("El promedio final es:", elemento[4])
if promedio_final >= 3.0:
    print("Aprueba")
else:
    print("Reprueba")