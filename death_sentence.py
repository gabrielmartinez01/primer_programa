
import datetime
import random

AVERAGE_LIFESPAN = random.randint(65, 80)

SMOKER_PENALIZATION = 6
DRINKER_PENALIZATION = 6
NO_WORKOUT = 10
NOT_HEALTHY_DIET = 6
penalization = 0

def print_with_underscores(message):
    print(message)
    print(len(message) * "_")

def only_right_answers(message):
    response = None
    while response != "Y" and response != "N" and response != "M":
        response = input(message + "(Y/N/M): ")
        if response == "Y":
            penalization = 1
        elif response == "N":
            penalization = 0
        elif response == "M":
            penalization = 0.5
    return response

print_with_underscores("Descubre cuanto de vida te queda")
print_with_underscores("Completa esta encuesta")

birth_date = input("Cuando naciste? (Formato: dd/mm/yyyy)")
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost = 0

only_right_answers("Fumas?")
years_lost += int(SMOKER_PENALIZATION * penalization)

only_right_answers("Bebes?")
years_lost += int(DRINKER_PENALIZATION * penalization)

only_right_answers("Haces ejercicio?")
years_lost += int(NO_WORKOUT * penalization)

only_right_answers("Comes saludable?")
years_lost += int(NOT_HEALTHY_DIET * penalization)

lifespan = AVERAGE_LIFESPAN - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de muerte {}, te quedan {} días para morir".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))
print(death_day.weekday())

