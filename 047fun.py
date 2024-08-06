'''9.  Escribir una función que tenga como parámetro un número y que devuelva 
cuantas cifras tiene ese número.
'''
 

def cantidad_cifras(n):
    d= str(n).split(".")
    return (len(d[1])+ len(d[0]))

print (cantidad_cifras (344324.6))