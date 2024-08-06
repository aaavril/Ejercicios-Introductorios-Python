'''10. Escribir una función que dados 3 números, devuelva cuál es el mayor.
'''

def nmayor (n1, n2, n3):
    if n1>n2 and n1>n3:
        mayor= n1
    elif n2>n1 and n2>n3:
        mayor= n2
    elif n3>n1 and n3>n2:
        mayor= n3
    else:
        mayor= "Hay más de un número mayor"
    return mayor 

n1= int(input("ingrese número: "))
n2= int(input("ingrese número: "))
n3= int(input("ingrese número: "))

mayor1= nmayor(n1, n2, n3)
print (mayor1)