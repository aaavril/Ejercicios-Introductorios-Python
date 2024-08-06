"""2. Escribir un código que lea por teclado números y los guarde en una lista, 
el proceso finaliza cuando se ingrese un número negativo. Mostrar los números pares."""

lista= []
n= int(input("Ingrese un número, negativo para finalizar"))
lista.append(n) 
while n >= 0:
    n= int(input("Ingrese un número, negativo para finalizar"))
    lista.append(n)
lista_pares= []
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i) 
print(lista_pares)



