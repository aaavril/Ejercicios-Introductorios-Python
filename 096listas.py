"""Implementar la diferencia simétrica de dos listas. La diferencia simétrica consiste en todos 
los elementos de la primera lista que no están en la segunda y de todos los elementos de la segunda 
lista que no están en la primera.
Por ejemplo difsim([1, 2, 3], [3, 4, 5]) devuelve [1, 2, 4, 5]. El resultado no debe tener duplicados.
"""

def diferencia_simetrica (lista1, lista2):
    nueva_lista= []
    for i in lista1:
        if i  not in nueva_lista and i not in lista2:
            nueva_lista.append(i)
    for i in lista2:
        if i  not in nueva_lista and i not in lista1:
            nueva_lista.append(i)
    return nueva_lista

lista1= [1, 2, 3]
lista2= [3, 4, 5]
print(diferencia_simetrica(lista1, lista2))