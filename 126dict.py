"""8. Escribir una función que permite organizar el envío masivo de emails para propagandas publicitarias. 
La función recibe un diccionario donde la clave es el nombre de una persona y el valor asociado es una 
lista de sus direcciones de correo electrónico (“emails”).

Por ejemplo:
emails={"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], 
"Marcela Rodríguez":["mleites@gmail.com", "rodriguez@gmail.com"], 
"Juan Lamas":["jlamasucu.edu.uy", "juan.lamas@gmail.com"]}

La función debe devolver el diccionario, eliminando cualquier email que esté duplicado 
(dos personas pueden estar con el mismo email) y además debe eliminar cualquier email 
que no contenga al menos un carácter “@” y un carácter “.”

Devolución con parámetro anterior:
emails={"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], 
"Marcela Rodríguez":["mleites@gmail.com"], "Juan Lamas":["juan.lamas@gmail.com"]}

Se eliminó "rodriguez@gmail.com" de Marcela porque ya existía y "jlamasucu.edu.uy" porque no tiene @."""

emails={"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], 
"Marcela Rodríguez":["mleites@gmail.com", "rodriguez@gmail.com"], 
"Juan Lamas":["jlamasucu.edu.uy", "juan.lamas@gmail.com"]}


def envio_masivo(emails):
 # creo el dicc resultado y una lista para controlar los emails repetidos
    dicc_resultado = {}
    lista_emails = [] # Lista para control de repetidos
 # recorro el dicc y para cada persona verifico si el email tiene "@" y ".",
 # y si no está en la lista de repetidos agrego al dicc nuevo el nombre
 # de la persona y los emails válidos (y no repetidos)
    for nombre in emails:
        emails_persona = emails[nombre]
        if nombre not in dicc_resultado:
            dicc_resultado[nombre] = []
            for email in emails_persona:
                if "@" in email and "." in email and email not in lista_emails:
                    dicc_resultado[nombre].append(email)
                    lista_emails.append(email)
    return dicc_resultado

emails={"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], "Marcela Rodríguez":["mleites@gmail.com", "rodriguez@gmail.com"], "Juan Lamas":["jlamasucu.edu.uy", "juan.lamas@gmail.com"]}

print(envio_masivo(emails))
