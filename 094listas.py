"""5. Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por 
un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, 
la nota media, la nota más alta que ha sacado y la menor."""

suma= 0
lista= []
for i in range(5):
    n = int(input("Ingrese su calificación: "))
    suma += n
    lista= lista.append(n)
print(f"Sus calificaciones son: {lista}, la nota más alta es {max(lista)}, la más baja es {min(lista)}, y la nota promedio es {suma/len(lista)} ")