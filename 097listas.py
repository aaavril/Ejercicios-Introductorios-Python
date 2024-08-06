"""Escribir una función que transforma una lista de listas con nombres y apellidos, 
en una única lista con cada nombre y apellido concatenados.
Por Ejemplo:

transformar_nombres( [ [‘Rocky’, 'Balboa'] , [‘Muhammad’, 'Ali'] ] )

devuelve [‘Rocky Balboa’, ‘Muhammad Ali’]"""

def transformar_nombres (lista_listas_nombres):
    lista_nombres= []
    for i in lista_listas_nombres:
        delimiter = ' '
        n= delimiter.join(i)
        lista_nombres.append(n)
    return lista_nombres

print(transformar_nombres([['Rocky', 'Balboa'] , ['Muhammad', 'Ali']]))
