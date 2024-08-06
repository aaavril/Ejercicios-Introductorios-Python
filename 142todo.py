"""Ejercicio 8
Sea la función promedios(lista, indices), donde lista es una lista de números e índices es una
lista de índices (al estilo de python). La función debe retornar el promedio de los números en la lista lista
ubicados en las posiciones indicadas en la lista indices.
Ejemplo, promedios([5, 8, 2, 1, 0, 7], [3, 1, 0]) deberá calcular el promedio de los valores
del primer argumento ubicados en las posiciones del segundo argumento, es decir, el promedio del valor en
la posición 3 (que es 1), en la posición 1 (8) y en la posición 0 (5). El promedio entonces es (1+8+5)/3.
Una posible función para resolver este problema sería:
def promedios(lista, indices):
 suma=0
 for i in indices:
 suma = suma+lista[i]
 p=suma/len(indices)
 return p
Sin embargo pueden darse situaciones que generen errores, como por ejemplo:
promedios([5, 8, 2, 1, 0, 7], [7, 1, 0]) generaría un error ya que no existe un índice 7
en la lista
promedios([5, 8, 2, 1, 0, 7], []) ya que len(indices) sería cero y al hacer
p=suma/len(indices) habría un división por cero
Usando el código anterior, modifíquelo agregando solamente try:except para controlar esos errores."""

#nodimos errores