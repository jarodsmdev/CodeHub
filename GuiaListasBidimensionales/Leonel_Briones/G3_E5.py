"""
Considere una lista bidimensional como la siguiente:
[["Juan", "Veloz", 32, "M"],["Marcela", "Nuñez", 17 "F"], ["Pedro", "Orellana", 67, "M"], ["Ana", "González", 40, "F"], ["Leonora", "Veneca", 23, "F"],] 
y ordénela según edad, de menor a mayor
"""

# Datos de entrada
listaPersonas = [
    ["Juan", "Veloz", 32, "M"],
    ["Marcela", "Nuñez", 17, "F"],
    ["Pedro", "Orellana", 67, "M"],
    ["Ana", "González", 40, "F"],
    ["Leonora", "Veneca", 23, "F"],
]

# Lista de personas ordenada por edad
ordenada = []

# Controla el número de pasadas que se hacen sobre la lista sin considerar el último elemento. Cada vez que se completa una pasada, el elemento más grande se coloca en su posición final.
for i in range(len(listaPersonas)):
    # Recorre la lista desde el inicio hasta el elemento que aún no está en su posición correcta en la pasada actual.
    # Se resta i para no considerar los elementos que ya están en su posición correcta.
    # Se resta 1 para no salir del rango de la lista.
    for j in range(0, len(listaPersonas) - i - 1):
        # Compara el elemento actual con el siguiente.
        if listaPersonas[j][2] > listaPersonas[j + 1][2]:
            # Se utiliza una variable temporal temp para almacenar el valor de listaPersonas[j] antes de realizar el intercambio de elementos.
            # Intercambio de elementos sin asignación simultánea
            temp = listaPersonas[j]
            listaPersonas[j] = listaPersonas[j + 1]
            listaPersonas[j + 1] = temp

# Asigna la lista ordenada a la variable ordenada
ordenada = listaPersonas

# Muestra la lista ordenada
print(ordenada)
