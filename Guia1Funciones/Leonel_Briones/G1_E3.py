"""
## Ejercicio 3
Escriba una función `ordenar(lista_numeros)` que reciba un argumento asociado a una lista de números enteros y devuelva la lista de números ordenada de mayor a menor.
**Ejemplo:**
print(ordenar([23, 1, 47]))
[47, 23, 1]
"""

def ordenar(lista: list) -> list:
    """
    funcion que recibe una lista de numeros enteros y devuelve la lista ordenada de mayor a menor
    
    Args:
        lista: lista de numeros enteros
        
    Returns:
        lista ordenada de mayor a menor
    """
    lista.sort()
    lista.reverse()
    return lista

print(ordenar([23, 1, 47]))