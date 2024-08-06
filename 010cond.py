''' Para calcular el sueldo de un empleado, el requisito básico es conocer la cantidad
de horas trabajadas en el mes y el valor por hora que se paga. Hacer un algoritmo
en diagrama de flujo que pida estos datos. Luego, en el caso de que el número de
horas trabajadas sea mayor a 40, esas horas adicionales (las que superan las 40)
deben pagarse al doble de su valor por hora. Ejemplo: si un empleado cobra
10$xhora y trabaja 30 horas, su sueldo se calculará como 300$. En cambio, si
trabajara 50 horas, cobrará 40x10$ las primeras 40 horas + 10x20$ las horas extras.'''

horas_mensuales= float(input("ingrese la cantidad de horas trabajadas "))
valor_hora= int(input("Ingrese el valor por hora "))
horas_extra= horas_mensuales-40

if horas_mensuales>40:
    pago_total= ((horas_mensuales-horas_extra)*valor_hora)+(horas_extra*(valor_hora*2))
else:
    pago_total= horas_mensuales*valor_hora

print("El sueldo del mes es de ", pago_total, " pesos.")
