"""
3. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número
 de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. 
 Repetir las preguntas hasta que el usuario ingrese la palabra  fin (fin puede estar en mayúsculas o minúsculas).
Fruta Precio
Banana 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70

"""

diccionario_frutas= {"Banana":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
bandera= True

while bandera:
    fruta= input("Ingrese fruta: ")
    if fruta== "fin" or fruta== "FIN" or fruta== "Fin":
        bandera= False 
    elif fruta in diccionario_frutas:
        print (f"{fruta} --------> {diccionario_frutas[fruta]}")
    else:
        print("No se encontró")