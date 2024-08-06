"""apertura ocular, respuesta verbal y eso para Glasgow"""

ao= 0
rv= 0
rm= 0

while ao<1 or ao>4:
    ao= int(input("ingrese la apertura ocular: "))
while rv<1 or rv>5:
    rv= int(input("ingrese la respuesta verbal: "))
while rm<1 or rm>5:
    rm= int(input("ingrese la respuesta motora: "))

score= ao+rv+rm
if score < 9:
    print ("GRAVE")
elif score < 13:
    print ("MODERADO")
else:
    print ("LEVE")
