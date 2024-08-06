hora1 = int(input("Ingrese la primera hora: "))
minuto1 = int(input("Ingrese el primer minuto: "))
segundo1 = int(input("Ingrese el primer segundo: "))

hora2 = int(input("Ingrese la segunda hora: "))
minuto2 = int(input("Ingrese el segundo minuto: "))
segundo2 = int(input("Ingrese el segundo segundo: "))

es_anterior = (hora1 < hora2) or (hora1 == hora2 and minuto1 < minuto2) or (hora1 == hora2 and minuto1 == minuto2 and segundo1 < segundo2)

print("La primera hora es anterior a la segunda." if es_anterior else "La primera hora es posterior a la segunda.")


