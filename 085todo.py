"""CALCULO DEL DIGITO VERIFICADOR DE LA CEDULA DE IDENTIDAD URUGUAYA
La Cédula de Identidad es el documento expedido por la Dirección Nacional de Identificación Civil a las
personas físicas. Cada cédula tiene un número identificador compuesto por un número de 6 o 7 cifras (para
las cédulas vigentes en la actualidad) y una cifra o dígito llamado dígito verificador. Este dígito verificador
se calcula a partir del número.
Pasos para calcular el digito verificador:
Cada dígito de la cédula se multiplica por un valor pre-definido y se suman, los valores predefinidos
son: 2, 9, 8, 7, 6, 3 y 4. Donde el dígito menos significativo se multiplica por 4, el siguiente por 3 y asi
sucesivamente hasta el más significativo que se multiplica por 2.
ejercicios-preparacion-parcial2.md 2023-10-16
6 / 6
Por ejemplo, para la cédula: 1234567 este primer paso se calcula de la siguiente manera: 7*4 + 6*3 +
5*6 + 4*7 + 3*8 + 2*9 + 1*2 = 148
Se obtiene el resto de la división entera entre el resultado de la suma obtenida en el paso anterior y
10, si el resultado es 0, este es el dígito verificador, sino se toma el resto y se le resta al número 10, el
resultado de esta operación es el digito verificador.
Siguiendo el ejemplo: 148%10 = 8, 10-8 = 2, el digito verificador de la cedula número: 1.234.567 es 2
NOTA: En el caso de una cedula de identidad de 6 dígitos, solo realizamos el calculo con los seis últimos
valores de ponderación, en este caso obviamos el valor de ponderación 2.
Realizar dos funciones:
La función digito_verificador(ci) que retornara el dígito verificador de la cédula de identidad
pasada como parámetro. Considerar que el número de cedula de identidad se pasa como un número
entero y el valor retornado es un número entero. Validar que el número de cédula es un número
entero que esta entre 100000 y 9999999, en el caso que no cumpla esta condición debe devolver el
valor -1, de esta forma se esta indicando que la cédula es invalida.
La función es_valida(ci, digito_verificador), donde ci y digito_verificador son dos
números enteros correspondientes al número de la cédula de identidad y su digito verificador,
debera retornar True si la cédula es válida y False si no lo es.
Prueben las funciones utilizando el número de cédula propia y las de sus compañeros."""

def checkdigit(ci):
    values = "2987634"
    cinumber = f"{ci:07d}"
    if ci <= 100000 or ci > 9999999:
        return -1 # Cedula invalida
    suma = 0
    for i in range(len(cinumber)):
        suma += int(cinumber[i]) * int(values[i])
        digito = suma % 10 
        return (10 - digito) % 10

def ci_isvalid(ci, digitov):
    return digitov == checkdigit(ci)

cedula = int(input("Ingrese el número de cedula sin digito verificador: "))
digito_verificador = int(input("Ingrese el digito verificador --------------: "))
if ci_isvalid(cedula, digito_verificador):
    print("Cedula correcta")
else:
    print("Cedula incorrecta")