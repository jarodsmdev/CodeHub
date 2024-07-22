"""
Ejercicio Adicional 3: Tuplas y Conjuntos en Combinación
Creen un programa que solicite a los usuarios ingresar nombres y edades. Almacenen estos datos en una lista de tuplas. Luego, utilicen un conjunto para identificar las edades únicas presentes en la lista.
"""

datos_personales = []

while True:
    nombre = input("[+] Ingrese un nombre: ")
    if nombre.lower() == "fin":
        break
    edad = int(input("[+] Ingrese la edad: "))
    datos_personales.append((nombre, edad))

# Explicación de _ en este código:
# _ es una convención en Python para indicar que no se va a utilizar el valor de la variable en el bucle
edades_unicas = {edad for _, edad in datos_personales}

print("Edades únicas Presentes:", edades_unicas)