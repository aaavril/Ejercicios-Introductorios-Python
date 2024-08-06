'''Determinar el índice de masa corporal (IMC) de una persona a partir de su peso
y su altura. Comunicarle al usuario si su peso corresponde a “Bajo Peso” (IMC < 18.5),
“Peso adecuado” (IMC entre 18.5 y 24.9), “Sobrepeso” (IMC entre 25 y 29.9) u
“Obesidad” (IMC mayor a 30). '''

altura= float(input("Ingrese su altura en cm "))
peso= float(input("Ingrese su peso en Kg "))
imc= (peso/(altura/100)**2)
if imc<18.5:
    print("Bajo peso")
elif imc>=18.5 and imc<=24.9:
    print("Peso adecuado")
elif imc>=25 and imc<=29.9:
    print("Peso adecuado")
else:
    print("Peso adecuado")


