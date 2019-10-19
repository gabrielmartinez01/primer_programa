
def in_rango(numero, rango):

    if numero in rango:
        verdadero_falso = True

    else:
        verdadero_falso = False

    return verdadero_falso

print(in_rango(25, range(0,10)))
