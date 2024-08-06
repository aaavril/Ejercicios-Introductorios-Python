"""5. Escribir una clase que permita representar al personaje de un videojuego. Un personaje tiene un nombre (o nickname), un porcentaje de vida (o salud), un poder (su nombre, por ejemplo, “patada giratoria”), y una medida de daño (número entero entre 0 y 100).

      1. Implementar un método que permite imprimir la información de un 

          personaje utilizando la instrucción print()

      2. Implementar un método que permite atacar a otro personaje (que se 

          recibe cómo parámetro). El ataque del personaje (p1) le quita vida al 

          personaje que es atacado (p2), utilizando la siguiente función:

          nueva_vida(p2) = vida_actual(p2) - medida_de_daño(p1)

     3. Implementar un método que indica (devolviendo True) si un personaje 

         está con vida (salud > 0)

     4. Crear 3 personajes llamados pj1, pj2 y pj3 (con el porcentaje de salud 

         y poder que ustedes desee), pj1 debe atacar a pj2 y pj3"""

#Crear la clase con sus parametros de nickname y eso
#Darle método print
#Darle método de atacar que tenga parámetro del otro personaje
#Metodo de si esta vivo con la fucin esa
#Crear a los 3 personajes y hacer que se ataquen y imprimir sus datos antes y despues para probar

class Personaje:
    def __init__(self, nombre, poder, daño):
        self.nombre = nombre
        self.poder = poder
        self.vida = 100 # Cuando se cera el personaje la vida es 100%
        self.daño = daño
    def get_daño(self):
        return self.daño
    def set_vida(self, valor):
        self.vida = valor
    def get_vida(self):
        return self.vida
    def __str__(self):
        return f"Personaje:\n\tNombre: {self.nombre}\n\tPoder: {self.poder}\n\tSaludo o Vida: {self.vida}"
    def atacar(self, otro):
        otro.set_vida(otro.get_vida() - self.get_daño())
    def salud(self):
        return self.vida > 0

# Ejemplos de creación e interacción
pj1 = Personaje("Batman", "Puñetazo",75)
pj2 = Personaje("Robin","Parada giratoria", 65)
pj3 = Personaje("El pinguino","Paraguazo",70)

print(pj1)
print(pj2)
print(pj3)
print()

print("Personaje 2 ataca al Personaje 3")
pj2.atacar(pj3)

if pj3.salud():
    print("el personaje 3 aun tiene vida")
else:
    print("el personaje 3 murio")
    print()
    print("Personaje 2 vuelve a atacar al Personaje 3")
    pj2.atacar(pj3)

if pj3.salud():
    print("el personaje 3 aun tiene vida")
else:
    print("el personaje 3 murio")
    print()
    print(pj3)
    print()