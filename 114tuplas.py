"""Implementar una función que reciba por parámetro una lisyta de tuplas, y retorne una tupla de la forma: a1, a2, a3, ..., an)
Donde ai corresponde a la suma de los elementos """

def sumatuplas(listatuplas):
    listaaux = []
    for i in range (len(listatuplas[0])):
        listaaux.append(0) 
    print(listaaux)
    for fila in range(len(listatuplas)):
        for elemento in range(len(listatuplas[0])):
            listaaux[fila]+= listatuplas[fila][elemento]  
    return tuple(listaaux)          


tuplas1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
resultado1 = sumatuplas(tuplas1)
print(resultado1)  # Salida esperada: (6, 15, 24)

