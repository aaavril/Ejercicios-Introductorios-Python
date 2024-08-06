"""6. Escribir una función que recibe el nombre de una canción y retorna el/los artista que la 
interpretan (utilizando diccionarios). Por ejemplo:

get_artistas(‘All my loving’) -> ‘The Beatles’
get_artistas(‘All along the watchtower’) -> [‘Bob Dylan’, ‘Jimi Hendrix']
"""

def get_artistas(nombre_cancion): 
    dicc_canciones = {"All my loving": ["The Beatles"], "Tusa": ["Karol G", "Nicki Minaj"], "Yendo a la casa de Damian": ["El Cuarteto de Nos"], "All along the watchtower": ['Bob Dylan’, ‘Jimi Hendrix']}
    
    if(nombre_cancion in dicc_canciones):
        return dicc_canciones[nombre_cancion]
    else:
        return "No tenemos disponible esa canción"
    

print(get_artistas("Tusa")) # ['Karol G', 'Nicki Minaj']
print(get_artistas("Despacito")) # "No tenemos disponible esa canción"
print(get_artistas('All my loving')) # ‘The Beatles’
print(get_artistas('All along the watchtower')) # [‘Bob Dylan’, ‘Jimi Hendrix']

 
