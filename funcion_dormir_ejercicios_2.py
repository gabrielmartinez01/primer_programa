import random
from time import sleep
import datetime

random_words_0 = ["Felicidad", "Alegria", "Paz"]
random_words_1 = ["Silla", "Mesa", "Cama"]
random_words_2 = ["Cerveza", "Vodka", "Ron"]
random_words_3 = ["Ira", "Odio", "Traicion"]
random_words_4 = ["Pasta", "Hamburguesa", "Pizza"]
random_words_5 = ["Calabaza", "Albaricoque", "Ajoporro"]
random_words_6 = ["Perro", "Gato", "Conejo"]
random_words_7 = ["Tigre", "Leon", "Titan"]
random_words_8 = ["Guau", "Miau", "Shhhh"]
random_words_9 = ["Broken", "Alone", "Depression"]

SECONDS_BETWEEN_WORDS = 1

while True:
    current_time = datetime.datetime.now()
    sleep(SECONDS_BETWEEN_WORDS)

    random_0 = random.choice(random_words_0) + " " + random.choice(random_words_0) + " " + random.choice(random_words_0) + " "
    random_1 = random.choice(random_words_1) + " " + random.choice(random_words_1) + " " + random.choice(random_words_1) + " "
    random_2 = random.choice(random_words_2) + " " + random.choice(random_words_2) + " " + random.choice(random_words_2) + " "
    random_3 = random.choice(random_words_3) + " " + random.choice(random_words_3) + " " + random.choice(random_words_3) + " "
    random_4 = random.choice(random_words_4) + " " + random.choice(random_words_4) + " " + random.choice(random_words_4) + " "
    random_5 = random.choice(random_words_5) + " " + random.choice(random_words_5) + " " + random.choice(random_words_5) + " "
    random_6 = random.choice(random_words_6) + " " + random.choice(random_words_6) + " " + random.choice(random_words_6) + " "
    random_7 = random.choice(random_words_7) + " " + random.choice(random_words_7) + " " + random.choice(random_words_7) + " "
    random_8 = random.choice(random_words_8) + " " + random.choice(random_words_8) + " " + random.choice(random_words_8) + " "
    random_9 = random.choice(random_words_9) + " " + random.choice(random_words_9) + " " + random.choice(random_words_9) + " "

    if current_time.second == 00 or current_time.second == 10 or current_time.second == 20 or current_time.second == 30 or current_time.second == 40 or current_time.second == 50:
        print(random_0)

    if current_time.second == 1 or current_time.second == 11 or current_time.second == 21 or current_time.second == 31 or current_time.second == 41 or current_time.second == 51:
        print(random_1)

    if current_time.second == 2 or current_time.second == 22 or current_time.second == 23 or current_time.second == 32 or current_time.second == 42 or current_time.second == 52:
        print(random_2)

    if current_time.second == 3 or current_time.second == 23 or current_time.second == 33 or current_time.second == 33 or current_time.second == 43 or current_time.second == 53:
        print(random_3)

    if current_time.second == 4 or current_time.second == 14 or current_time.second == 24 or current_time.second == 34 or current_time.second == 44 or current_time.second == 54:
        print(random_4)

    if current_time.second == 5 or current_time.second == 15 or current_time.second == 25 or current_time.second == 35 or current_time.second == 45 or current_time.second == 55:
        print(random_5)

    if current_time.second == 6 or current_time.second == 16 or current_time.second == 26 or current_time.second == 36 or current_time.second == 46 or current_time.second == 56:
        print(random_6)

    if current_time.second == 7 or current_time.second == 17 or current_time.second == 27 or current_time.second == 37 or current_time.second == 47 or current_time.second == 57:
        print(random_7)

    if current_time.second == 8 or current_time.second == 18 or current_time.second == 28 or current_time.second == 38 or current_time.second == 48 or current_time.second == 58:
        print(random_8)

    if current_time.second == 9 or current_time.second == 19 or current_time.second == 29 or current_time.second == 39 or current_time.second == 49 or current_time.second == 59:
        print(random_9)


