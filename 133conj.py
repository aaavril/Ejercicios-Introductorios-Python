"""

Realice un programa en Python que muestre el siguiente menú:
A: Agregar elemento al conjunto

B: Borrar elemento del conjunto

T: Borrar todos los elementos del conjunto

M: Mostrar conjunto

F: FInalizar

Si el usuario elije la opción A o B, el programa debe pedir qué número agregar o cuál borrar 
(si al agregar ya existe, indicarlo con un mensaje, si el elemento que se quiere borrar no existe, 
}avisar al usuario con otro mensaje).

Una vez que se ejecuta la opción deseada se debe volver a mostrar el menú, hasta que se elija la opción de finalizar. 
Si la opción no es ninguna de las indicadas, mostrar un mensaje adecuado y volver a mostrar el menú.

OBS: para borrar los elementos de un conjunto disponemos del método clear(). Investigue su uso.

"""
bandera= True
conjunto= set()

while bandera== True:
    opcion= input("""A: Agregar elemento al conjunto

B: Borrar elemento del conjunto

T: Borrar todos los elementos del conjunto

M: Mostrar conjunto

F: Finalizar
      
Opción seleccionada: """)
    if opcion== "F":
        bandera= False
    elif opcion== "A":
        n= int(input("Ingrese numero a agregar: "))
        if n in conjunto:
            while n in conjunto:
                print("elemento no válido")
                n= int(input("Ingrese numero a agregar: "))
            conjunto.add(n)
        else:
            conjunto.add(n)
    elif opcion== "B": 
        n1= int(input("Ingrese numero a borrar: "))
        if n1 not in conjunto:
            while n not in conjunto:
                print("elemento no válido")
                n= int(input("Ingrese numero a borrar: "))
            conjunto.discard(n)
        else:
            conjunto.discard(n)
    elif opcion== "T":
        conjunto.clear()
    elif opcion== "M":
        print(conjunto)
    else:
        print("Opción no válida \n")

