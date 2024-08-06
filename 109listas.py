"""sumar de a 3 si es múltiplo de 3 """


lista= [1, 2, 3, 4, 5, 6, 7, 8, 9]
contador= 0
lista_sumas= []
suma= 0
for i in lista:
    suma+= i
    contador+= 1
    if contador == 3:
        lista_sumas.append(suma)
        contador=0
        suma=0
print(lista_sumas)
