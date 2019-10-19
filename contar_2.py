
frase = input("Escribe una frase:")
n_mayusculas = 0
mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I," "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for letra in frase:
    if letra in mayusculas:
        n_mayusculas += 1

print("Este es el numero de mayusculas {}:".format(n_mayusculas))
