"""1. Pensemos en un Auto que tiene las siguientes características: marca, color, año. 

También Recordá lo siguiente:

-       existen atributos que describen las características del objeto (o su estado) y existen métodos, que son 
        las acciones asociadas a un objeto

-       toda clase tiene un método que se llama constructor (en el caso de Python toma el nombre __init__) y que 
        se ejecuta automáticamente al declarar una variable como una instancia de una clase.

-       todos los métodos deben incluir como primer parámetro a self (que hace referencia a la instancia misma)

-       así como tenemos __init__, existen otros métodos que ya están contemplados por Python. Por ejemplo, si hacemos 
        print(objeto), si la clase del objeto tiene definido el método __str__ entonces se invocará y retornará un string asociado. 
        Como el resultado de ejecutar __str__ es una cadena, Python la mostrará por pantalla.

Creá una clase Auto, con los atributos mencionados anteriormente, con un método __str__ asociado que devuelva 
un string con las características del auto y los métodos arrancar y frenar. (cuando se invoca arrancar, 
el auto está en movimiento y solo se podrá frenar, de modo que si se vuelve a arrancar deberá mostrar el cartel 
“el auto ya está en movimiento”. De la misma manera, si el auto está frenado y se invoca frenar deberá decir que 
“el auto ya está detenido”)."""

class Auto:
    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año
        self.en_movimiento = False
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
   
    # Ejemplos de creación de objetos
auto1 =Auto("Chevrolet","Azul", 1998)
auto2 =Auto("Ford", "Rojo", 2005)

print(auto1)
print(auto2)
print()
auto1.arrancar()
auto1.arrancar()
auto1.frenar()
auto1.frenar()
