"""Función promedios en una lista de numeros y otra de indices que indica los objetos a los cuales se les hace promedio"""

def promedios (lista, indices):
    suma= 0
    for i in indices:
        suma+= lista[i]
    promedio= suma/len(indices)
    return promedio
    
print(promedios([1, 2, 3, 4, 5, 6], [0, 2, 4]))