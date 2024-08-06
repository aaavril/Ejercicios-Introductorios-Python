'''Considere la liquidación de sueldo de una empresa para un empleado. 
Al sueldo total acordado con el empleado (que llamaremos SueldoAcordado) 
se le debe adicionar la antigüedad, que es de un 1% de SueldoAcordado 
por cada año trabajado (por ejemplo, si tiene 7 años 
trabajados entonces recibe un adicional del 7%); cuando la antigüedad 
es de 20 años o más, este adicional es fijo y es 20% sobre SueldoAcordado 
(por ejemplo, si tiene 20, 23 o 35 años trabajados entonces el adicional que recibe es del 20%).

Luego, al SueldoAcordado más el adicional por antigüedad deben descontarse los siguientes ítems:
-        11% para el seguro de retiro,
-        6% para el seguro médico
-        Si el SueldoAcordado más el adicional por antigüedad es mayor a 120.000$, entonces se descontará un 
25% de ese monto en concepto de impuesto a la ganancia; si es mayor a 70.000$ (y menor a 120.000$) 
se descontará 20%; si es menor a 70.000$ no se descuenta nada.
Defina el código que permita calcular el monto de antigüedad, seguro de retiro, 
seguro médico e impuesto a la ganancia. Luego realice un programa para pedir al usuario el SueldoAcordado, 
los años de antigüedad y muestre el sueldo final que recibirá el trabajador.'''

def calcular_antiguedad(sueldo_acordado, anos_trabajados):
    if anos_trabajados >= 20:
        return sueldo_acordado * 0.20
    else:
        return sueldo_acordado * (anos_trabajados * 0.01)

def calcular_seguro_retiro(sueldo_total):
    return sueldo_total * 0.11

def calcular_seguro_medico(sueldo_total):
    return sueldo_total * 0.06

def calcular_impuesto_ganancia(sueldo_total):
    if sueldo_total > 120000:
        return sueldo_total * 0.25
    elif sueldo_total > 70000:
        return sueldo_total * 0.20
    else:
        return 0

sueldo_acordado = float(input("Ingrese el sueldo acordado: "))
anos_trabajados = int(input("Ingrese los años de antigüedad: "))

monto_antiguedad = calcular_antiguedad(sueldo_acordado, anos_trabajados)
sueldo_total = sueldo_acordado + monto_antiguedad

descuento_retiro = calcular_seguro_retiro(sueldo_total)
descuento_medico = calcular_seguro_medico(sueldo_total)
descuento_impuesto = calcular_impuesto_ganancia(sueldo_total)

sueldo_final = sueldo_total - descuento_retiro - descuento_medico - descuento_impuesto

print("El sueldo final del trabajador es:", sueldo_final)