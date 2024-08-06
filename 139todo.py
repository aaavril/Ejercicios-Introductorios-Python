"""Ejercicio 5
En un campeonato de básquetbol intervienen 20 equipos de hasta 10 miembros cada uno (y un mínimo de
7).
Se quiere desarrollar un programa que lleve a cabo las siguientes operaciones:
1. Formar una selección de 20 miembros integrada por el jugador más alto de cada equipo.
2. Listar los equipos y sus miembros ordenados por altura.
3. Indicar el nombre del jugador más alto del campeonato.
Los jugadores son almacenados en un diccionario donde la clave es el nombre del equipo y el valor es la
lista con los jugadores.
Cada jugador está representado por objetos de la clase:
class Jugador():
 def __init__(self, nombre,altura):
 self.nombre = nombre
 self.altura = altura
 def __str__(self):
 pass
Se pide escribir los métodos necesarios para cumplir con los 3 requerimientos indicados anteriormente.
Además debe completar y usar las siguientes clases:
class Equipo():
 def __init__(self, nombre):
 def agregar_jugador(self, jugador):
 def mas_alto_del_equipo(self):
 def __str__(self):
class Liga():
 def __init__(self, nombre):
 def agregar_equipo(self, equipo):
 def Seleccion_mas_altos(self): #retorna la seleccion de los 20 más
altos
"""

class Jugador():
    def __init__(self, nombre,altura):
        self.nombre = nombre
        self.altura = altura
    def __str__(self):
        return f"{self.nombre}, {self.altura}"

class Equipo():
    def __init__(self, nombre):
        self.jugadores = []
        self.nombre = nombre
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    def mas_alto_del_equipo(self):
        mas_alto = None
        jugador_mas_alto = None
        for jugador in self.jugadores:
            if mas_alto == None or jugador.altura > mas_alto:
                mas_alto = jugador.altura
                jugador_mas_alto = jugador
        return jugador_mas_alto
    def __str__(self):
        return f"{self.nombre}"
    
class Liga():
    def __init__(self, nombre):
        self.liga = nombre
        self.equipos = []
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
    def Seleccion_mas_altos(self): #retorna la seleccion de los 20 más altos
        jugadores_mas_altos = []
        for equipos in self.equipos:
            jugadores_mas_altos.append(equipos.mas_altos_del_equipo())
            jugadores_mas_altos.sort()
        if len(jugadores_mas_altos) >= 20:
            return jugadores_mas_altos[len(jugadores_mas_altos) - 20:]
        else:
            return jugadores_mas_altos

    def __str__(self):
        return f"{self.nombre}"