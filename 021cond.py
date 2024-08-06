'''Escriba un programa que lea tres números (n, linf, lsup). Esta función debería imprimir "verdadero" 
o "falso" si linf <= n <= lsup (es decir, si n está entre linf y lsup).'''
n= int(input("ingrese numero"))
linf= int(input("ingrese numero inferior"))
lsup= int(input("ingrese numero superior"))
if linf<=n and n<= lsup:
    print("verdadero")
else: print("falso")    
