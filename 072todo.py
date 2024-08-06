"""Implementar la función obtener_entero(mensaje, min, max), que debe imprimimir el mensaje
(incluyendo el rango min:max) y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es
un número entero entre min y max (inclusive), se le debe avisar al usuario y pedir el ingreso de otro valor.
Una vez que el usuario ingresa un valor válido, la función lo debe devolver.
Ejemplo:

n = obtener_entero("¿Cúal es su número favorito?", -10,50)
Debe imprimir:
¿Cúal es su número favorito? [-10:50]:
¿Cúal es su número favorito? [10,50]: 5
Debe ingresar un número entre 10 y 50
¿Cúal es su número favorito? [10,50]: 52
Debe ingresar un número entre 10 y 50
¿Cúal es su número favorito? [10,50]: 25
El número ingresado es: 25"""

def obtener_entero(mensaje, min, max):
    print (f"{mensaje} [{min}:{max}]: ")
    numero= int(input(mensaje))
    while numero<min or numero>max:
        numero= int(input(f"Debe ingresar un numero entre {min} y {max}: "))
    print ("El numero ingresado es: ", numero)    

n = obtener_entero("¿Cúal es su número favorito?", -10,50)
