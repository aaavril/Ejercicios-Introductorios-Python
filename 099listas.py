"""DESAFÍO 2: TRADUCTOR
Definir una función “traductor” que recibe por parámetro 2 listas con palabras, 
una lista con palabras en español y la otra con palabras en inglés. 
De acuerdo a la posición de la lista, se conoce la traducción de la misma, 
es decir en la posición x de la lista con palabras en inglés, está la traducción 
de la palabra en la posición x de la lista con palabras en español. La función 
recibe un tercer parámetro que es una frase y retorna una traducción sencilla de la frase.

Ej.: traducir([“es”,“hoy”,“viernes”],[“is,“today”,“friday”],“Hoy es viernes”)  devuelve:  “today is friday”"""

def traductor (lista_esp, lista_ing, frase):
    lista_traducida= [] #inicializar lista de la traducción
    frase= frase.lower()
    lista_frase= frase.split() #trasnformar a la frase en lista

    for i in lista_frase: #recorrer la frase 
        indice= lista_esp.index(i) #buscar la posicion de cada palabra en lista esp
        palabra= lista_ing[indice] #agregar a una nueva lista la posición esa en inglés
        lista_traducida.append(palabra)

    traduccion= ' '.join(lista_traducida) #retornar frase traducida como cadeba
    return traduccion

print(traductor(['es','hoy','viernes'],['is','today','friday'],'hoy es viernes')) #devuelve:  “today is friday”"""

