'''Leer números desde teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números positivos ingresados (solo de los números que sean positivos).'''

numero= float(input("Ingrese un número, 0 para terminar"))
suma= 0
while numero != 0:
    suma= suma+numero
    numero= float(input("Ingrese un número, 0 para terminar"))
    
print("la suma es ", suma)