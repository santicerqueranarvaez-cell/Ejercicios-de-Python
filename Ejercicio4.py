texto = input("Ingrese una frase o texto: ")

caracteres = len(texto)
palabras = len(texto.split())
vocales = 0

for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales = vocales + 1
    elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        vocales = vocales + 1

print("ANÁLISIS DEL TEXTO")
print("Cantidad de caracteres:", caracteres)
print("Cantidad de palabras:", palabras)
print("Cantidad de vocales:", vocales)
print("Texto en mayúsculas:", texto.upper())
print("Texto en minúsculas:", texto.lower())

opcion = input("¿Desea analizar otro texto? (S/N): ")

while opcion == "S" or opcion == "s":
    texto = input("\nIngrese una frase o texto: ")

    caracteres = len(texto)
    palabras = len(texto.split())
    vocales = 0

    for letra in texto:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales = vocales + 1
        elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            vocales = vocales + 1

    print("ANÁLISIS DEL TEXTO ")
    print("Cantidad de caracteres:", caracteres)
    print("Cantidad de palabras:", palabras)
    print("Cantidad de vocales:", vocales)
    print("Texto en mayúsculas:", texto.upper())
    print("Texto en minúsculas:", texto.lower())

    opcion = input("\n¿Desea analizar otro texto? (S/N): ")

print("Programa finalizado.")