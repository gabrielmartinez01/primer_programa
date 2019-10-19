
operacion = input("Que operacion quieres hacer? (Suma / Resta / Multiplicacion / Division): ").upper()
primer_numero = int(input("Cual es el primer numero de tu operacion?"))
segundo_numero = int(input("Cual es el segundo numero de tu operacion?"))
simbolo = "No elegido"
resultado = 0

if operacion == "SUMA":
    simbolo = "+"
    resultado = primer_numero + segundo_numero

elif operacion == "RESTA":
    simbolo = "-"
    resultado = primer_numero - segundo_numero

elif operacion == "MULTIPLICACION":
    simbolo = "*"
    resultado = primer_numero * segundo_numero

elif operacion == "DIVISION":
    simbolo = "/"
    resultado = primer_numero / segundo_numero

print("Tu operacion es {} {} {} y su resultado es: {}".format(primer_numero, simbolo, segundo_numero, resultado))



