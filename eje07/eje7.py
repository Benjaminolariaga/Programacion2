año=0
mes=0
dia=0


print("cual es tu año de nacimiento")
año=int(input())
print("ingresa tu mes de nacimiento")
mes=int(input())
print("ingresa tu dia de nacimiento")
dia=int(input())

import datetime

nacimiento=datetime.datetime(año,mes,dia)
actual=datetime.datetime.now()
diferencia=actual-nacimiento
anios=diferencia.days //365
meses=(diferencia.days % 365) //30
dias=(diferencia.days % 365) % 30
print(anios,meses,dias)
print(diferencia)
