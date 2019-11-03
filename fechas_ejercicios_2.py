
import datetime

hoy = datetime.datetime.today()
cumpleanos = datetime.datetime(year=2020, month=3, day=22)
tiempo_restante = cumpleanos - hoy

print("Faltan {} dias y {} horas".format(tiempo_restante.days, int(tiempo_restante.seconds / 3600)))
print(cumpleanos.weekday())



