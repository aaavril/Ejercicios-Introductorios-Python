'''Leer un número entero positivo (mayor que 0) desde teclado e imprimir la suma de los dígitos que lo componen. 
Tenga en cuenta que para esto vamos a utilizar las siguientes funciones (que deberá implementar):

- ultimodigito( n ): dado un número n (por ejemplo 456), deberá retornar el último de los dígitos (ej: 6)

- sacarultimodigito( n ): dado un número n (ej: 456) deberá retornar el mismo número pero sin su último dígito (ejL 45)

Con estas dos funciones componga el programa solicitado. Tenga en cuenta que dado un número podemos sumar sus dígitos 
identificando uno por uno de derecha a izquierda. Por ejemplo, para el número 1456 podemos obtener ultimodigito 
(es decir, identificamos el 6) y luego achicar el número con sacarultimodigito (quedaría 145). 
Si repetimos este procedimiento identificaremos todos los dígitos y el número se irá reduciendo hasta 0.  
'''

def ultimodigito(n):
    ult = n % 10 
    return ult

def sacarultimodigito(n):
    n_sin_ult = n // 10 
    return n_sin_ult

n = int(input("Ingrese un número: "))
suma = 0

while n >= 1:
    ultimo = ultimodigito(n)
    suma += ultimo
    n = sacarultimodigito(n)

print("La suma de los dígitos es:", suma)
