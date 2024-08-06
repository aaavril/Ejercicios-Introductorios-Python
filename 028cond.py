'''Escribir un programa que recibe como parámetros dos horas dadas por horas, 
minutos y segundos e imprime "es anterior" si la primera hora (contemplando horas, minutos y segundos) 
es anterior que la segunda o "es posterior". 
Resuélvalo de dos maneras: utilizando if y utilizando únicamente expresiones lógicas.'''

hora1 = int(input("Ingrese la primera hora: "))
minuto1 = int(input("Ingrese el primer minuto: "))
segundo1 = int(input("Ingrese el primer segundo: "))

hora2 = int(input("Ingrese la segunda hora: "))
minuto2 = int(input("Ingrese el segundo minuto: "))
segundo2 = int(input("Ingrese el segundo segundo: "))

if hora1 < hora2 or (hora1 == hora2 and minuto1 < minuto2) or (hora1 == hora2 and minuto1 == minuto2 and segundo1 < segundo2):
    print("La primera hora es anterior a la segunda.")
else:
    print("La primera hora es posterior a la segunda.") 

#ver 18