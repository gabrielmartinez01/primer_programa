
numeros = [1, 10, 70, 30, 50, 55]

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 2 == 0:
        multiplos_dos.append(numero)

    if numero % 3 == 0:
        multiplos_tres.append(numero)

    if numero % 5 == 0:
        multiplos_cinco.append(numero)

    if numero % 7 == 0:
        multiplos_siete.append(numero)

print(multiplos_dos)
print(multiplos_tres)
print(multiplos_cinco)
print(multiplos_siete)

