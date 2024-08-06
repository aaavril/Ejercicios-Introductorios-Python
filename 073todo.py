"""Considere la liquidación de sueldo de una empresa para un empleado. Al sueldo total acordado con el
empleado (que llamaremos sueldo_acordado) se le debe adicionar la antigüedad, que es de un 1% de
sueldo_acordado por cada año trabajado (por ejemplo, si tiene 7 años trabajados entonces recibe un
adicional del 7%); cuando la antigüedad es de 20 años o más, este adicional es fijo y es 20%
sobresueldo_acordado (por ejemplo, si tiene 20, 23 o 35 años trabajados entonces el adicional que recibe
es del 20%).
Luego, al sueldo_acordado más el adicional por antigüedad deben descontarse los siguientes ítems:
11% para el seguro de retiro,
6% para el seguro médico
Si el sueldo_acordado más el adicional por antigüedad es mayor a $120.000, entonces se descontará un
25% de ese monto en concepto de impuesto a la ganancia; si es mayor a $70.000 y menor o igual a
$120.000) se descontara 20% y si es menor no se descuenta nada. 

Defina las funciones que permitan
calcular el monto de antigüedad, seguro de retiro, seguro médico e impuesto a la ganancia. Luego realice
un programa que utilice estas funciones para pedir al usuario el sueldo_acordado, los años de antigüedad y
muestre el sueldo final que recibirá el trabajador.
"""

def monto_antiguedad (sueldo_acordado, años_antiguedad):
    if años_antiguedad < 20:
        sueldo_antiguedad= sueldo_acordado + sueldo_acordado*(años_antiguedad/100)
    else:
        sueldo_antiguedad= sueldo_acordado + sueldo_acordado*(20/100)
    return sueldo_antiguedad

def seguro_retiro (sueldo_antiguedad):
    monto_seguro_retiro= sueldo_antiguedad*(11/100)
    return monto_seguro_retiro

def seguro_medico (sueldo_antiguedad):
    monto_seguro_medico= sueldo_antiguedad*(6/100)
    return monto_seguro_medico

def impuesto_ganancia (sueldo_antiguedad):
    if sueldo_antiguedad > 120000:
        monto_impuesto= sueldo_antiguedad*(25/100)
    elif sueldo_antiguedad > 70000 and sueldo_antiguedad<= 120000:
        monto_impuesto= sueldo_antiguedad*(20/100)
    else:
        monto_impuesto= 0
    return monto_impuesto

sueldo_acordado1= int(input("Ingrese el sueldo acordado: "))
años_antiguedad1= int(input("Ingrese los años de antiguedad: "))
sueldo_antiguedad1 = monto_antiguedad (sueldo_acordado1, años_antiguedad1)
sueldo_final= sueldo_antiguedad1 - (seguro_retiro (sueldo_antiguedad1) + seguro_medico (sueldo_antiguedad1) + impuesto_ganancia (sueldo_antiguedad1))
print ("El sueldo final del empleado es ", sueldo_final)