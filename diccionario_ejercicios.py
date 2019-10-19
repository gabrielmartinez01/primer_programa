
exit = False
agenda = dict()

while not exit:
    pregunta_inicial = input("Que quieres hacer? (Añadir un cumpleaños (A) / Consultar un cumpleaños (B) / Salir / (C): ")

    if pregunta_inicial == "A":
        print("Añadiendo cumpleaños: ")
        nombre = input("Cual es su nombre?: ")
        fecha = input("Cuando cumple años?: ")
        agenda[nombre] = fecha

    elif pregunta_inicial == "B":
        print("Consultando cumpleaños: ")
        nombre = input("De quien quieres consultar su cumpleaños?: ")
        print(agenda[nombre])

    elif pregunta_inicial == "C":
        exit = True




