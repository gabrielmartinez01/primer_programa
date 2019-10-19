
def letras_por_rayas(frase):

    cantidad_rayas = ""

    for item in frase:
        if item.isalpha() or item == "":
            cantidad_rayas += "-"

    return cantidad_rayas

print(letras_por_rayas("Hola buenos dias como estamos chavales"))
