"""1. Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dolar':'us$', 'Yen':'¥', 'Peso':'$', 'Real':'R$'}, 
luego pregunte al usuario por una divisa y muestre su símbolo 
(o un mensaje de aviso si la divisa no está en el diccionario). 
"""

divisas= {"Euro":"€", "Dolar":"US$", "Peso": "$", "Yen": "¥"}
divisa= input("Ingrese divisa: ")
divisa= divisa.capitalize()

if divisa in divisas:
    print (f"{divisa} --------> {divisas[divisa]}")
else:
    print("No se encontró")


