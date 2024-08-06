"""
Vamos a volver al caso del termo visto en clase. Además de las características vistas, para mayor realidad
deberíamos considerar que un termo tiene una capacidad (en cm3), un nivel de agua actual (también en
cm3). Luego, cuando un termo se “crea” inicialmente deberá estar vacío. Ahora bien, un termo se ve
involucrado en cosas tales como llenarlo de agua, cebar mate, etc.
Por otro lado, también tenemos a los mates, que tendrán sus características y métodos. Ahora vamos a
querer una clase Mate y las instancias de mates y termos actuarán de la forma en que interactúan en la
vida real: los termos ceban mates, los mates son tomados, los termos son llenados…
Pensá en términos de atributos que describen a cada clase y sus métodos asociados… y ponete a tomar
mate con objetos.

"""

class Termo:
    def __init__(self, material, color, capacidad, volumen_cebar):
        self.material = material
        self.color = color
        self.capacidad = capacidad
        self.volumen_cebar = volumen_cebar # cantidad de cm3 que ceba el mate
        self.nivel = 0
    def __str__(self):
        return f"Mate: material: {self.material}, color: {self.color}, capacidad:{self.capacidad} cm3, nivel de agua: {self.nivel} cm3"
    def get_nivel(self):
        return self.nivel
    def get_volumen_cebar(self):
        return self.volumen_cebar
    def cargar_agua(self, volumen):
        if self.nivel + volumen > self.capacidad:
            self.nivel = self.nivel + volumen - self.capacidad
        else:
            self.nivel += volumen
    def cebar(self):
        if self.nivel >= self.volumen_cebar:
            self.nivel -= self.volumen_cebar
        else:
            print("No hay suficiente agua para cebar")


# ejemplos de creacion e interaccion de objetos
termo1 = Termo("metal","verde",1000,5)
print(termo1)
print()
termo1.cargar_agua(1000)
print("Cebando un mate")
termo1.cebar()
print(termo1)
print()
termo2 = Termo("plastico","blanco",300,5)
termo2.cargar_agua(300)
print("Cebando el termo 2")
contador = 0
while termo2.get_nivel() >= termo2.get_volumen_cebar():
    termo2.cebar()
    contador += 1
    print(f"Termo2: se pudo cebar {contador} veces")
    print(termo2)