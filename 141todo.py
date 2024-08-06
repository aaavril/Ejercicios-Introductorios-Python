"""Ejercicio 7
1. Definir una clase Punto que tenga los siguientes atributos:
pos_x
pos_y
Crear un constructor para esta clase que reciba como parámetros valores iniciales para x e y.
2. Definir una clase Rectángulo que tenga los siguientes atributos:
vértice (instancia de la clase Punto) que determina la posición del vértice superior izquierdo
del rectángulo - valor númerico
alto, que determina la altura del rectángulo, valor númerico
largo, que determina el largo del rectángulo, valor númerico
color, que determina el color del rectángulo, una cadena de caracteres
ejercicios-practica-tercer-parcial.md 2023-11-21
7 / 10
Definir los siguientes métodos:
área(), que devuelve el valor del área del rectángulo.
tamaño(x) que recibe un factor cómo parámetro que se aplicará a las dimensiones del
rectángulo para cambiar su tamaño (Si x es mayor a 1 se agranda, sino se achica).
vértices() que devuelve una lista con dos puntos que representan los vértices
superior izquierdo e inferior derecho
clonar que crea un nuevo objeto Rectángulo con los mismos valores para todos los
atributos que el objeto original.
3. A continuación crear 3 objetos rectángulo:
El primero con el vértice superior izquierdo en la posición (10,10) y con alto 30 y ancho 20.
El segundo, tiene su vértice superior izquierdo a una distancia de 100 (horizontal) del primero
El tercero está a una distancia de 150 (vertical) del primero y es del doble de tamaño.
"""

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return f"Punto({self.x},{self.y})"

class Rectangulo:
    def __init__(self, vertice, alto, largo, color):
        self.vertice = vertice
        self.alto = alto
        self.largo = largo
        self.color = color
    def area(self):
        return self.largo * self.alto
    def tamanio(self, f):
        self.largo *= f
        self.alto *= f
    def vertices(self):
        v = self.vertice
        x = v.getX() + self.largo
        y = v.getY() - self.alto
        return [ self.vertice, Punto( x, y) ]
    def clonar(self):
        return Rectangulo(self.vertice, self.alto, self.largo, self.color)
    def __str__(self):
        return f"Rectangulo({self.vertice},{self.alto}, {self.largo},{self.color})"

vertice_rec1 = Punto(10,10)
rec1 = Rectangulo(vertice_rec1,30, 20,"rojo")
rec2 = Rectangulo(Punto(110, 10), 30, 20,"verde")
rec3 = Rectangulo(Punto(10, 160),60, 40,"rojo")
print(f"Rectangulo 1: {rec1}")
print(f"\tArea: {rec1.area()}")
vertices = rec1.vertices()
print(f"\tVertices: {vertices[0]},{vertices[1]}")
print()
clon = rec1.clonar()
print(f"Rectangulo clon: {clon}")
print(f"\tArea: {clon.area()}")
print()
clon.tamanio(2)
print(f"Rectangulo clon duplicado: {clon}")
print(f"\tArea: {clon.area()}")
print()