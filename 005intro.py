'''Realice un programa que lea 3 números correspondiente a las horas, 
minutos y segundos e imprima por pantalla ese horario en formato hh:mm:ss.'''
horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
horario = "El horario es: {:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
print(horario)
# se podía usar también fstring 