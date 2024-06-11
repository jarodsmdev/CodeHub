"""
Ejercicio 6
Escriba una función llamada cuenta_letra(palabra) que recibe una palabra en formato string y retorne una lista con el número de vocales y consonantes que tiene la palabra.
Ejemplo:
>> print(cuenta_letra(‘programacion’))
>> [5, 7]
"""

def cuenta_letra(palabra: str) -> list:
    """
    Función que recibe una palabra y retorna una lista con el número de vocales y consonantes que tiene la palabra

    Args:
        palabra (str): Palabra a analizar
    
    Returns:
        list: Lista con el número de vocales y consonantes que tiene la palabra
    """
    
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚüÜ"
    lista = []
    cantVocales = 0
    
    # Contar vocales y consonantes
    for c in palabra:
        if c in vocales:
            cantVocales += 1

    # Agregar a la lista
    lista.append(cantVocales)
    lista.append(len(palabra) - cantVocales)
    return lista

print(cuenta_letra('programacion'))