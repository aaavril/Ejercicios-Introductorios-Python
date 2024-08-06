'''Dada una hora (leyendo tres datos, horas, minutos y segundos), 
calcule e imprima por pantalla  la cantidad total de segundos.'''
horas = int(input("Ingrese las horas "))
minutos = int(input("Ingrese los minutos "))
segundos = int(input("Ingrese los segundos "))
total_segundos = horas * 3600 + minutos * 60 + segundos
print("La cantidad total de segundos es: ", total_segundos)