"""funcion que cuenta la cantidad de veces que aparece un digito en un numero. 
El resto de la division entre 10 da el ultimo digito"""

def contar(d, numero):
    contador = 0
    numero_original = numero
    while numero > 0:
        nn = numero % 10
        if nn == d:
            contador += 1
        numero = numero // 10    
    print(f"El dígito {d} aparece {contador} veces en {numero_original}")

contar(5, 555599993)