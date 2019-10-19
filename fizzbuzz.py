
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

    if numero % 3 == 0 and numero % 5 == 0:
        numeros[indice] = "Bazinga"

    if numero % 3 == 0 and numeros[indice] != "Bazinga":
            numeros[indice] += "Fizz"

    if numero % 5 == 0 and numeros[indice] != "Bazinga":
            numeros[indice] += "Buzz"

print(numeros)
