"""
Ejercicio 7
Escriba una función llamada division_correo(correo) que reciba una dirección de correo electrónico y entregue una lista con la parte antes del arroba (@) y luego la parte después del arroba.
Ejemplo:
>> print(division_correo("programacion_algoritmos@duoc.cl"))
>> ["programacion_algoritmos", "duoc.cl"]
"""

def division_correo(correo: str) -> list:
    """
    Función que recibe una dirección de correo electrónico y entrega una lista con la parte antes del arroba y la parte después del arroba

    Args:
        correo (str): Dirección de correo electrónico

    Returns:
        list: Lista con la parte antes del arroba y la parte después del arroba
    """
    posicionArroba = 0
    for i in range(len(correo)):
        print(i)
        if correo[i] == "@":
            posicionArroba = i
    
    usuario = correo[:posicionArroba]
    dominio = correo[posicionArroba + 1:]
    lista = []
    lista.append(usuario)
    lista.append(dominio)
    
    return lista

### MAIN ###
print(division_correo("programacion_algoritmos@duoc.cl"))