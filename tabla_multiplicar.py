
numero_tabla = int(input("De que numero quieres la tabla?"))

for multiplo in range(5, 16):
        print("{} x {} = {}".format(numero_tabla, multiplo, multiplo * numero_tabla))