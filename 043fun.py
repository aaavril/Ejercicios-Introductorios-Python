'''Dado el peso y altura de un adulto, desarrollar una función que devuelva un 
string donde se indique la categoría del índice de masa corporal.
'''
def imc_calculator (altura, peso):
    calculo= (peso/(altura/100)**2)
    if calculo<18.5:
        resultado= "Bajo peso"
    elif calculo>=18.5 and calculo<=24.9:
        resultado= "Peso adecuado"
    elif calculo>=25 and calculo<=29.9:
        resultado= "Sobrepeso"
    else:
        resultado= "Obesidad"
    return resultado

altura= float(input("Ingrese su altura en cm: "))
peso= float(input("Ingrese su peso en Kg:  "))
resultado1= imc_calculator (altura, peso)
print (resultado1)