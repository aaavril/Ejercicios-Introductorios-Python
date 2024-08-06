"""Ejercicio 3
Sea un personaje de nuestro videojuego. El personaje se mueve en un mundo de dos dimensiones (x, y) y
cuando comienza el juego se encuentra ubicado en la posición (0,0) y su nivel de energía están en 10 (ese
valor se inicializa siempre con 10).
El personaje tiene estos métodos asociados:
Constructor: __init__(): el método constructor -además de definir el estadio inicial- deberá
recibir como parámetro el nombre del personaje (string)
avanzar(lista_movimientos): lista_movimientos es una lista de tuplas, donde cada tupla
tiene el siguiente formato (dirección, casilleros). El string dirección puede ser "norte",
"sur", "este", "oeste", mientras que casilleros indica la cantidad de casilleros a moverse. Si el
personaje ha sido recién creado (está en el origen) entonces invocar a este método
avanzar([("norte", 1), ("este", 2)]) dejaría a nuestro personaje en la posición (2, 1).
Tener en cuenta que cada vez que se mueve un casillero se consume una unidad de energía (en el
ejemplo anterior, el primer movimiento consumió 1 y el segundo 2, por lo tanto como arrancó en 10,
luego de invocar al método avanzar() el nivel de energía estará en 7). Un detalle: solo se realiza un
movimiento si existe energía disponible para ir en esa dirección; si en el ejemplo la lista de
movimientos es [("norte", 9), ("este", 2)], avanzaría hasta (0, 9), tendría 1 unidad de
energía remanente y con eso no le alcanza para el segundo movimiento, por lo tanto se quedará en
ese último lugar y no seguirá con el resto de los movimientos, es decir, hará todos los movimientos
posibles. Cuando puede hacer todos los movimientos, los hace y listo; cuando no puede seguir con
los movimientos, se queda en el último posible y debe imprimir un cartel que diga "No he podido
completar el avance. Me he detenido en la posición (x, y)" donde x e y es la posición real donde
quedó.
cargar_energia(unidades): aumenta (es decir agrega) la energía indicada al personaje
ubicación(): devuelve una tupla con las coordenadas (x,y) del personaje
distancia(otro_personaje): devuelve la distancia que existe entre el personaje del objeto y
otro_personaje que se pasa como parámetro
El getter/obtener del nivel de energía del personaje
Un método que cuando se haga print(personaje) imprima información del personaje: nombre,
ubicación, energía.
Se pide crear esta clase y utilizarla exactamente de la siguiente manera (respetar la secuencia de pasos):
1. Crear un personaje p1 que se llame "Bear"
2. Que "Bear" avance (usando una única llamada al método avanzar) 2 casillas hacia el norte, 2 al este.
3. Imprimir información de "Bear"
4. Crear un segundo personaje llamado "Carman
5. Que "Carman" avance (usando una única llamada al método avanzar) 2 casillas hacia el sur, 1 al
oeste y 4 al sur.
6. Que "Bear" avance (usando una única llamada al metodo avanzar) 7 casilla hacia el este, 2 al norte.
7. Aumentar la energía de "Bear" en 10
8. Imprime el estado de "Bear" y repite el paso 6.
9. Calcula (e imprime) la distancia entre "Bear" y "Carman"
Consideraciones:
El avance es siempre positivo y entero
La posición puede ser negativa (si se crea un personaje y avanza 2 casilleros al sur entonces se
encontrará en la posición (0, -2)
la función raíz cuadrada en Python puede realizarse fácilmente elevando a la ½.

"""

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.x = 0
        self.y = 0
        self.energia = 10
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_energia(self):
        return self.energia

    def get_nombre(self):
        return self.nombre

    def avanzar(self, lista_movimientos):
        for movimiento in lista_movimientos:
            if self.energia-movimiento[1] > 0:
                if movimiento[0] == "norte":
                    self.y += movimiento[1]
                elif movimiento[0] == "este":
                    self.x += movimiento[1]
                elif movimiento[0] == "oeste":
                    self.x -= movimiento[1]
                else:
                    self.y -= movimiento[1]
                    self.energia -= movimiento[1]
            else:
                print(f"No he podido completar el avance. Me he detenido en la posición ({self.x},{self.y})")

    def cargar_energia(self, unidades):
        self.energia += unidades
    
    def ubicacion(self):
        return (self.x,self.y)
    
    def distancia(self, otro_personaje):
        distancia = ((self.x - otro_personaje.get_x())**2 + (self.y - otro_personaje.get_y())**2)**(1/2)
        return distancia
    
    def __str__(self):
        return f"{self.nombre}, ({self.x},{self.y}), {self.energia}"

# Programa principal
p1 = Personaje("Bear") # 1
p1.avanzar([("norte", 2), ("este",2)]) # 2
print(p1) # 3
p2 = Personaje("Carman") # 4
p2.avanzar([("sur", 2), ("oeste", 1), ("sur", 4)]) # 5
p1.avanzar([("este", 7), ("norte", 2)]) # 6
p1.cargar_energia(10) # 7
p1.avanzar([("este", 7), ("norte", 2)]) # 7
print(p1)
distancia = p1.distancia(p2)
print()
print(p1)
print(p2)
print(f"distancia entre {p1.get_nombre()} y {p2.get_nombre()}:{distancia:.2f}")