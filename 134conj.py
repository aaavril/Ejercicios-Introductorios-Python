"""Python ofrece una forma cómoda de definir conjuntos (y otras estructuras de datos) que es el 
conjunto por compresión (en una forma similar a la descripción por comprensión de un conjunto). 
El conjunto A definido a continuación son los primeros 1000 números naturales elevados al cuadrado, 
mientras que B es el mismo conjunto, pero elevados al cubo.

4.1 - ¿Qué elementos están presentes en ambos conjuntos? ¿cuántos son?

4.2 - ¿El conjunto {576, 676, 784, 529, 625, 729, 7744, 7569} son números obtenidos por elevar un natural al cuadrado?

"""

A={i**2 for i in range(1,1000)}

B={i**3 for i in range(1,1000)}

respuesta_1_a= A & B
respuesta_1_b= len(respuesta_1_a)

C= {576, 676, 784, 529, 625, 729, 7744, 7569}
respuesta_2= C.issubset(A)

print(f"¿Qué elementos están presentes en ambos conjuntos?: {respuesta_1_a}\n¿Cuántos son?: {respuesta_1_b}\n¿El conjunto 576, 676, 784, 529, 625, 729, 7744, 7569 son números obtenidos por elevar un natural al cuadrado?: {respuesta_2} ")

