"""
Ejercicio 1
Haga un programa que considere la lista [2, 8, 4, 12, 1, 19], y entregue la suma de todos sus valores, pero sin usar la función sum().
"""

# Define la lista
lista = [2, 8, 4, 12, 1, 19]

# Define la función sumarLista
def sumarLista(lista):
    """
    sumarLista: list -> int
    Recibe una lista de valores y retorna la suma de todos los valores de la lista.
    """
    suma = 0
    for valor in lista:
        suma += valor
    return suma


### MAIN ###
# Imprime la suma de los valores de la lista
print(sumarLista(lista))