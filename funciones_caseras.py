
def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Haz dicho esto: {}, estas seguro (Si / No)".format(dato_usuario))
        if seguro == "SI":
            confirmacion = True
        return dato_usuario

nombre = input_con_confirmacion("Como te llamas?")
print("Has confirmado que te llamas {}".format(nombre))

edad = input_con_confirmacion("Dime tu edad")
print("Has confirmado que tu edad es: {}".format(edad))

