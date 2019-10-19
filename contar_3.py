frase = input("Escribe una frase:")
vocales = ["a", "e", "i", "o", "u"]

for letra in frase:
    if letra in vocales:
        print(letra)
