
number_to_guess = 77
user_number = int(input("Dime un numero del 1 al 100"))

while user_number != number_to_guess:
    print("Respuesta incorrecta, intentalo otra vez")
    user_number = int(input("Dime un numero del 1 al 100"))

if user_number == number_to_guess:
    print("Felicidades, has ganado")