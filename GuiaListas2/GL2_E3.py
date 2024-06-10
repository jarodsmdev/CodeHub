"""
Ejercicio 3
Haga un programa que reciba palabras hasta que se ingresa un string vacío ("", de largo cero). Esas palabras deben ser almacenadas en una lista y mostrar la lista. Luego, debe mostrar la lista ordenada alfabéticamente, pero descendentemente.
Ejemplo:
Ingrese palabra: saber
Ingrese palabra: programar
Ingrese palabra: es
Ingrese palabra: importante
Ingrese palabra:
La lista es: ["saber", "programar", "es", "importante"]
La lista ordenada es: ["saber", "programar", "importante", "es"]
"""

# Declaración de lista vacía
lista = []

# Solicitar palabras
while True:
    # Recibe un texto y le quita los espacio al inicio y al final
    palabra = input("[+] Ingrese palabra: ").strip()
    # En caso de ser un string vacío rompe el ciclo
    if palabra == "":
        break
    else:
        # Agrega la palabra a la lista
        lista.append(palabra)

# Muestra la lista por terminal formateada con un texto
print(f"La lista es: {lista}")
# Ordena la lista de manera ascendente
lista.sort()
# Invierte la lista
lista.reverse()
# Muestra la lista por terminal formateada con un texto
print(f"La lista ordenada descendientemente es: {lista}")
