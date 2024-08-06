"""
a) Realice un programa en Python donde se cree un set llamado departamentos que incluya todos 
los nombres de departamentos de Uruguay (declararlo en forma explícita en el código, es decir 
departamentos = {"Canelones", "Artigas", "Montevideo", .....}

b) Realice un set donde figuren los departamentos que tienen fronteras con otro país 
(tener en cuenta que departamentos como Colonia -y departamentos más al norte sobre el río- 
son fronteras fluviales, ver aquí )

c) El siguiente set departamentos_serranos={"Maldonado", "Lavalleja", "Rocha", "Treinta y Tres", "Cerro Largo"}
 contiene los departamentos de Uruguay con formaciones serranas, mientras que 
 departamentos_playas={"Maldonado", "Rocha"} son los departamentos con playas denominadas "oceánicas".

d) Usando operaciones de conjuntos en Python conteste:

- ¿Qué departamentos de Uruguay no tienen fronteras con otro país?

- ¿Cuáles de los departamentos que no tienen fronteras otros países tampoco tienen sierras?

- Si un turista te pregunta qué departamentos visitar que incluya ambas atracciones (sierras y playas oceánicas), ¿cuál sería la respuesta? 

- Si un turista te pregunta qué departamentos tienen alguna atracción turística, ¿cuál sería la respuesta?

- ¿Qué departamentos no ofrecen ninguna atracción turística de las aquí mencionadas? (ninguna de las dos)

"""

departamentos = {"Artigas", "Canelones","Cerro Largo", "Colonia", "Durazno",
"Flores", "Florida", "Lavalleja", "Maldonado", "Montevideo", "Paysandú",
"Río Negro", "Rivera", "Rocha", "Salto", "San José", "Soriano", "Tacuarembó",
"Treinta y Tres" }
departamentos_frontera = {"Artigas", "Cerro Largo", "Colonia", "Paysandú",
"Río Negro", "Rivera", "Rocha", "Salto", "Soriano", "Treinta y Tres" }
departamentos_serranos = {"Maldonado", "Lavalleja", "Rocha", "Treinta y Tres",
"Cerro Largo"}
departamentos_playas = {"Maldonado", "Rocha"}

a= departamentos - departamentos_frontera
print("¿Qué departamentos de Uruguay no tienen fronteras con otro país?: ", a)
print()

b= departamentos -(departamentos_frontera|departamentos_serranos)
print("¿Cuáles de los departamentos que no tienen fronteras otros países tampoco tienen sierras?: ", b)
print()

c= departamentos_serranos&departamentos_playas
print("Si un turista te pregunta qué departamentos visitar que incluya ambas atracciones (sierras y playas oceánicas), ¿cuál sería la respuesta?", c)
print()

d= departamentos_serranos|departamentos_playas
print("Si un turista te pregunta qué departamentos tienen alguna atracción turística, ¿cuál sería la respuesta?", d)
print()

e= departamentos-d
print("¿Qué departamentos no ofrecen ninguna atracción turística de las aquí mencionadas? (ninguna de las dos))", e)
print()

