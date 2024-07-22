"""
EJERCICIO 1 Frecuencia de palabras de un texto
Creen un programa que solicite a los usuarios ingresar un texto. Luego, el programa debe analizar el texto y mostrar la frecuencia de cada palabra. Utilicen un diccionario para almacenar
las palabras como claves y la frecuencia como valores.
"""

texto = input("[+] Ingrese un texto: ")

# Dividir el texto en palabras
palabras = texto.split()
# Crear un diccionario para almacenar las palabras y su frecuencia
frecuencia_palabras = {}

# Contar la frecuencia de cada palabra
for palabra in palabras:
    palabra = palabra.lower()
    # explicación de get() en este codigo: 
    # get recibe 2 argumentos, el primero es la clave que se quiere buscar en el diccionario, el segundo es el valor que se le asigna a la clave si no se encuentra en el diccionario
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra} : {frecuencia}")