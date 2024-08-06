'''3. Escribir un programa que permita al usuario ingresar 6 números enteros, 
que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos 
y el promedio de los positivos. No olvides que no es posible dividir por cero, por lo que es necesario 
evitar que el programa arroje un error si no se ingresaron números positivos.

'''

suma_negativos=0
suma_positivos=0
contador_positivos=0
for i in range(6):
    n= int(input("Ingrese un número entero: "))
    if n==0:
        print("Ingrese de nuevo un número que no sea 0: ")
    else:    
        n= int(input("Ingrese un número entero: "))
        if n>1:
            suma_positivos=suma_positivos+n 
            contador_positivos=contador_positivos+1
        elif n<1:
            suma_negativos= suma_negativos+n    
            

promedio_positivos= suma_positivos/contador_positivos
print ("la suma de los negativos es: ", suma_negativos, "y el promedio de los positivos es ", promedio_positivos)
