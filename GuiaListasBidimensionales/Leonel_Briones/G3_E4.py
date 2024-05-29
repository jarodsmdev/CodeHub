"""
Ejercicio 4
Dada una lista bidimensional como:
["Juan", "Veloz", 32, "M"], ["Marcela", "Nuñez", 17, "F"], ["Pedro", "Orellana", 67, "M"], ["Ana", "González", 40, "F"], ["Leonora", "Veneca", 23, "F"]]
donde los datos de cada persona son: nombre, apellido, edad y género.
Haga un programa que lea una lista como la anteriormente mostrada y separe las personas por género.
Debe dejar a todas las personas de género masculino en una lista y las de género femenino en otra lista. El programa debe mostrar las listas creadas.

Ejemplo:
La lista de mujeres es: [['Marcela', 'Nuñez', 17, 'F'], ['Ana', 'González', 40, 'F'], ['Leonora', 'Veneca', 23, 'F']]
La lista de hombres es: [['Juan', 'Veloz', 32, 'M'], ['Pedro', 'Orellana', 67, 'M']]
"""
# Declaración de variables
male_list = []
female_list = []

# Lista con los datos
lista = [
    ["Juan", "Veloz", 32, "M"],
    ["Marcela", "Nuñez", 17, "F"],
    ["Pedro", "Orellana", 67, "M"],
    ["Ana", "González", 40, "F"],
    ["Leonora", "Veneca", 23, "F"],
]
        
# Recorrer la lista
for persona in range(len(lista)):
    # Identificar género
    if lista[persona][3] == "M":
        male_list.append(lista[persona])
    else:
        female_list.append(lista[persona])
        
# Mostrar listas
print("La lista de mujeres es:", female_list)
print("La lista de hombres es:", male_list)
