
def mayor_de_tres(primer_numero, segundo_numero, tercer_numero):
    numero_mayor = primer_numero

    if segundo_numero > numero_mayor:
        numero_mayor = segundo_numero

    if tercer_numero > numero_mayor:
        numero_mayor = tercer_numero

    return numero_mayor

print(mayor_de_tres(1, 2, 3))






