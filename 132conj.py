"""Realice un programa en Python que pida números positivos por teclado y los vaya almacenando en un conjunto. 
La carga de estos números deberá hacerse hasta que se haya alcanzado un máximo de 5 elementos en el conjunto 
o hasta que se haya ingresado un número negativo. Si el número ingresado ya existe el programa debe mostrar 
un cartel que avise que ese número ya existía. Al finalizar la carga debe mostrar el conjunto resultante.
"""

bandera= True
contador= 0
conjunto= set()

while bandera== True and contador< 5:
    n= int(input("Ingrese números positivos (-1 para terminar): "))
    nset= set()
    nset.add(n)
    if n == -1:
        bandera= False
    elif nset.issubset(conjunto):
        print("El numero ya existía")
    else:
        conjunto.add(n)
        contador+=1
print(conjunto)

