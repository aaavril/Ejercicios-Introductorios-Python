"""2. El caso anterior ha sido bien sencillo. Comencemos a agregar un poco de realismo y modifiquemos la clase anterior; 
dentro de los atributos agreguemos la capacidad del tanque y el rendimiento (kilómetros por litro de nafta) 
(estos atributos deberán declararse en el constructor, además llevaremos un kilometraje que inicialmente estará en 0). 
Cuando se defina un auto, el nivel del tanque de nafta deberá ser cero (es decir, está vacío de combustible). 
Por lo tanto tendremos otros métodos que serán:

- recorrer(kms): hace que el auto recorra tantos kms. Para esto debe verificar que el nivel de combustible alcance para 
poder recorrerlos (deberá chequearse si hay combustible disponible, en función del rendimiento del auto). 
Si el combustible no alcanza entonces el auto deberá mostrar por pantalla lo ocurrido (y decir qué cantidad de 
kilómetros podría recorrer con la nafta disponible, pero se queda quieto).

- cargar_nafta(litros): permite cargar litros al tanque. Si la cantidad de litros supera a la capacidad 
del tanque, se llenará el tanque y se informará por pantalla que sobraron tantos litros."""

class Auto:
    def __init__(self, marca, color, año, capacidad, rendimiento):
        self.marca = marca
        self.color = color
        self.año = año
        self.capacidad= capacidad
        self.rendimiento= rendimiento
        self.en_movimiento = False
        self.nivel_combustible= 0
        self.kilometraje= 0
    def __str__(self):
        return f"{self.marca}, {self.color}, {self.año}"
    def arrancar(self):
        if self.en_movimiento == True:
            print("el auto ya esta en movimiento.")
        else:
            print("el auto arranco")
            self.en_movimiento = True
    def frenar(self):
        if self.en_movimiento == False:
            print("el auto ya está detenido.")
        else:
            print("el auto freno")  
            self.en_movimiento = False
    def recorrer(self, kms):
        litros_necesarios = kms / self.rendimiento
        if litros_necesarios > self.nivel_combustible:
            print("No hay suficiente combustible")
            print(f"El tanque tiene {self.nivel_combustible} litros, da para recorrer {self.nivel_combustible*self.rendimiento}kms")
        else:
            print(f"Recorre {kms}")
            self.nivel_combustible -= litros_necesarios
    def cargar_nafta(self, litros):
        if litros + self.nivel_combustible > self.capacidad:
            sobrante = self.nivel_combustible + litros - self.capacidad
            self.nivel_combustible = self.capacidad
            print(f"La cantidad de litros supera la capacidad del tanque, sobran: {sobrante} litros")
        else:
            self.nivel_combustible += litros

# Ejemplos de creación de objetos
auto1 =Auto("Chevrolet","Azul", 1998, 40, 10)
auto2 =Auto("Ford", "Rojo", 2005, 60, 9)

print(auto1)
print(auto2)
print()
auto1.arrancar()
auto1.arrancar()
auto1.frenar()
auto1.frenar()
print()
print("Auto1 carga nafta")
auto1.cargar_nafta(70)
print("Auto 1 despues de cargar combustible:")
print(auto1)
print()
print("Auto 1 intenta recorrer 100km")
auto1.recorrer(100)
print("Auto 1 despues de recorrer 100km:")
print(auto1)
print()
print("Auto 1 intenta recorrer 500km")
auto1.recorrer(500)

