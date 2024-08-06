
"""
DESAFÍO EXTRA


PyFIFA

1.       Crear una clase Jugador que tenga los atributos:

-       Nombre (string)

-       Cedula (numérico, 8 digitos)

-       Número de camiseta (numérico)

-       Posición (string, "Golero", "Defensa", "Mediocampista" o "Delantero")

-       Valoración (numérico, de 1 a 100)7


A.       Implementar un método jugar que reciba la acción a realizar como string (atajar, marcar, mover con pelota, pasar, pase largo, interceptar pase, patear al arco, despejar) que imprima el número y nombre de jugador y la acción que realizó.

B.       Implementar un método mover que reciba la dirección a moverse el jugador como string (arriba, abajo, izquierda y derecha) y la velocidad como un número de 1 a 100 e imprima el número y nombre de jugador, el movimiento que realizó y si éste fue LENTO (velocidad <60) o RÁPIDO (velocidad >=60).

C.       Implementar un método interaccion que reciba otro jugador, la acción de ese otro jugador y una acción (de este jugador -self-). El método debe:

a.             Si acción de un jugador es "atajar" y del otro es "patear al arco", debe imprimir GOL o ATAJADA según las valoraciones de los jugadores. Se debe imprimir quién hace gol y quién ataja. Si las valoraciones son iguales es GOL.

b.             Si acción de un jugador es "marcar" y del otro es "mover con pelota", debe imprimir MARCA o AVANCE según las valoraciones de los jugadores. Se debe imprimir quién marca y quién avanza. Si las valoraciones son iguales es AVANCE.

c.              Si acción de un jugador es "pasar", "pase largo" o "despejar" y del otro es "interceptar pase", debe imprimir PASE CON EXITO o INTERCEPCION según las valoraciones de los jugadores. Se debe imprimir quién hace el pase y quién lo intercepta. Si las valoraciones son iguales es PASE CON EXITO.

d.             Si acciones de los jugadores son otras debe imprimir INTERACCION NO VALIDA.

D.       Implementar el método __str__(self) que imprima los datos del jugador con un formato agradable.

Realizar los controles de cédula (que sea de 8 dígitos), de la posición (que sea una posición valida) y de la valoración (que sea un número de 1 a 100) cuando se crea un objeto jugador. En caso de que haya un error en los datos no debe asignar ese valor al jugador y debe arrojar un mensaje de error."""

class Jugador:
    def __init__(self, nombre, cedula, camiseta, posicion, valoracion):
        posiciones_validas = ["Golero", "Defensa", "Mediocampista", "Delantero"]
        
        if not isinstance(cedula, int) or len(str(cedula)) != 8:
            raise ValueError("Cédula debe ser un número de 8 dígitos")
        if not isinstance(camiseta, int):
            raise ValueError("Número de camiseta debe ser un número")
        if posicion not in posiciones_validas:
            raise ValueError("Posición no válida. Debe ser 'Golero', 'Defensa', 'Mediocampista' o 'Delantero'")
        if not (1 <= valoracion <= 100):
            raise ValueError("Valoración debe ser un número entre 1 y 100")
        
        self.nombre = nombre
        self.cedula = cedula
        self.camiseta = camiseta
        self.posicion = posicion
        self.valoracion = valoracion
        print("Jugador ingresado con éxito")

    def __str__(self):
        return (f"Jugador {self.nombre}:\n\tCédula: {self.cedula}\n\tNúmero de camiseta: {self.camiseta}\n\tPosición: {self.posicion}\n\tValoración: {self.valoracion}")

    def jugar(self, accion):
        acciones_validas = ["atajar", "marcar", "mover con pelota", "pasar", "pase largo", "interceptar pase", "patear al arco", "despejar"]
        if accion not in acciones_validas:
            print("Acción no válida")
        else:
            print(f"Jugador número {self.camiseta}, {self.nombre}: {accion}")

    def mover(self, direccion, velocidad):
        direcciones_validas = ["arriba", "abajo", "izquierda", "derecha"]
        if direccion not in direcciones_validas:
            print("Dirección no válida")
            return
        
        rapidez = "lento" if velocidad < 60 else "rápido"
        print(f"Jugador número {self.camiseta}, {self.nombre}: Se movió a la {direccion} y fue {rapidez}")

    def interaccion(self, otro_jugador, accion_otro, accion):
        if accion == "atajar" and accion_otro == "patear al arco":
            if self.valoracion >= otro_jugador.valoracion:
                print(f"ATAJADA: {self.nombre} ataja el tiro de {otro_jugador.nombre}")
            else:
                print(f"GOL: {otro_jugador.nombre} marca un gol contra {self.nombre}")

        elif accion == "marcar" and accion_otro == "mover con pelota":
            if self.valoracion >= otro_jugador.valoracion:
                print(f"MARCA: {self.nombre} marca a {otro_jugador.nombre}")
            else:
                print(f"AVANCE: {otro_jugador.nombre} avanza con el balón contra {self.nombre}")

        elif accion in ["pasar", "pase largo", "despejar"] and accion_otro == "interceptar pase":
            if self.valoracion >= otro_jugador.valoracion:
                print(f"PASE CON EXITO: {self.nombre} hace un pase exitoso contra la intercepción de {otro_jugador.nombre}")
            else:
                print(f"INTERCEPCION: {otro_jugador.nombre} intercepta el pase de {self.nombre}")

        else:
            print("INTERACCION NO VALIDA")

# Ejemplo de uso
jugador1 = Jugador("Julián Boehmwald", 12345678, 39, "Delantero", 100)
jugador2 = Jugador("Carlos Sanchez", 87654321, 5, "Defensa", 78)
jugador3 = Jugador("Sergio Rochet", 87654111, 1, "Golero", 80)


print(jugador1)
print(jugador2)
print(jugador3)

jugador1.mover("derecha", 70)
jugador1.interaccion(jugador2, "interceptar pase", "pase largo")
jugador3.interaccion(jugador1, "patear al arco", "atajar")
