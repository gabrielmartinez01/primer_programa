
def numeros_pares(lista_de_numeros):

    lista_de_numeros_pares = []

    for item in lista_de_numeros:
        if item % 2 == 0:
            lista_de_numeros_pares.append(item)

    return lista_de_numeros_pares

print(numeros_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))