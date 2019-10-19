
lista_compra = []
input_lista = input("Que quieres comprar (Escribe FIN para salir):")

while input_lista != "FIN":
    lista_compra.append(input_lista)
    input_lista = input("Que quieres comprar (Escribe FIN para salir):")

for item_de_compra in lista_compra:
    print("Hay que comprar {}".format(item_de_compra))

print("Esta es la lista de la compra")



