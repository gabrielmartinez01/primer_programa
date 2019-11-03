
import random
finish = False

while finish is False:
    number_to_guess = int(random.randint(1, 10))
    user_number = int(input("Tell me a number between 1 and 10"))
    if user_number == number_to_guess:
        print("That's correct")
        finish = True
    else:
        print("That's not correct")









