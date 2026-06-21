print("Simulación de Cajero Automatico")


lista = []
saldo = 1000000
continuar ="si"


def Consultar_Saldo():
    print("Su saldo actual es:", saldo)

def Realizar_Deposito():
    global saldo
    deposito = int(input("¿Cuanto desea depositar?"))
    saldo += deposito

def Efectuar_Retiro():
    global saldo
    retiro = int(input("¿Cuanto desea retirar?"))
    saldo += retiro
    if saldo < retiro:
        print("Fondos insuficientes")
    else:
        print("Retiro exitoso")




opcion = 0
while opcion !=4:
   print("1. consultar saldo")
   print("2. Realizar Depositos")
   print("3. Efectuar Retiros")
   print("4. salir")

   opcion = int(input("Seleccione una opcion: "))

   if opcion == 1:
    Consultar_Saldo()
   elif opcion == 2:
    Realizar_Deposito()
   elif opcion == 3:
    Efectuar_Retiro()
   elif opcion == 4:
    print("Saliendo del sistema")
   else:
    print("Opcion Invalida")
