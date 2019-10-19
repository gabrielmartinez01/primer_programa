
frase = input("Escribe una frase:")
lista_signos = [",", ".", " "]

n_comas = 0
n_puntos = 0
n_espacios = 0

for signo in frase:
    if signo in lista_signos[0]:
        n_comas += 1
    elif signo in lista_signos[1]:
        n_puntos += 1
    elif signo in lista_signos[2]:
        n_espacios += 1

print("Este es el numero de comas: {}, este el de puntos: {} y este el de espacios: {}".format(n_comas, n_puntos, n_espacios))





