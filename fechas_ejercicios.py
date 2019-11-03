
import datetime

hoy = datetime.datetime.today()

time_remaining = hoy - datetime.timedelta(days=5)
dia_semana = time_remaining.weekday()

print(time_remaining)
print(dia_semana)





