lista_numero = []
numero_usuario = ""

while len(lista_numero) < 5:
    while not numero_usuario.isdigit():
        numero_usuario = input("Dime un numero:")
    lista_numero.append(int(numero_usuario))
    numero_usuario = ""
    print("Numero añadido")

suma = lista_numero[0] + lista_numero[1] + lista_numero[2] + lista_numero[3] + lista_numero[4]

print("Esta es la media de los numeros en la lista: {}.".format(suma / 5))






