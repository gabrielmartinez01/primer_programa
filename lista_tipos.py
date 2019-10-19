
lista_mixta = ["1", "Hola", "2", "Buenas"]
lista_enteros = []
lista_strings = []

for item in lista_mixta:
    if item.isdigit():
        lista_enteros.append(int(item))
    elif item.isalpha():
        lista_strings.append(item)

print(lista_enteros)
print(lista_strings)





