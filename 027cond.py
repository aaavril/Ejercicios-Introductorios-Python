''' Escribir un programa que reciba una fecha dada por tres números (día, mes y año) 
e indica si es una fecha valida. Tener en cuenta que los meses de Enero, Marzo, Mayo, Julio, 
Agosto, Octubre y Diciembre tienen 31 días, Febrero 28 (o 29 días si es bisiesto) 
y el resto de los meses 30 días.
Ej: para el 29/02/2016 es válido, pero 29/02/2015 no lo es.'''

ano= int(input("Ingrese el año: "))
mes= int(input("Ingrese el mes: "))
dia= int(input("Ingrese el dia: "))

if 2024 > ano >= 1 and 12 >= mes >= 1:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            print("La fecha es válida.")
        else:
            print("La fecha es inválida.")
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            print("La fecha es válida.")
        else:
            print("La fecha es inválida.")
    elif mes == 2:
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) and 1 <= dia <= 29:
            print("La fecha es válida.")
        elif not (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) and 1 <= dia <= 28:
            print("La fecha es válida.")
        else:
            print("La fecha es inválida.")
else:
    print("La fecha es inválida.")