
def letras_por_rayas(frase):

    cantidad_rayas = ""

    for item in frase:
        if item.isalpha() or item == "":
            cantidad_rayas += "_"

    return cantidad_rayas

print(letras_por_rayas("Me llamo Gabriel"))
