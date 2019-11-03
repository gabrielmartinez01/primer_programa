import datetime

fecha = datetime.datetime(year=2019, month=3, day=22)
hoy = datetime.datetime.now()
tiempo_transcurrido = hoy - fecha
horas_1 = tiempo_transcurrido.days * 24
horas_2 = tiempo_transcurrido.seconds / 3600
horas_3 = int(horas_1 + horas_2)

print("Estas son las horas que han transcurrido: {}".format(horas_3))



