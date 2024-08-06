'''Escriba la función que dado un número en punto flotante retorne su parte decimal. 
Ej: si la función se llama ParteDecimal entonces ParteDecimal(4.453) devolvería el número 0.453

'''
def partedecimal (n):
    parte_entera_n= n//1
    parte_decimal_n= n-parte_entera_n
    return parte_decimal_n


n= float(input("Ingrese un número decimal: "))
parte_decimal_n_1= partedecimal (n)
print ("La parte decimal del número es: ", parte_decimal_n_1)

#opción con módulo math
'''import math

def partedecimal(n):
    parte_decimal_n, parte_entera_n = math.modf(n)
    return parte_decimal_n

n = float(input("Ingrese un número decimal: "))
parte_decimal_n_1 = partedecimal(n)
print("La parte decimal del número es:", parte_decimal_n_1)'''