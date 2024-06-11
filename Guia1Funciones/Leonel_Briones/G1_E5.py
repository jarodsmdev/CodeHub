"""
Ejercicio 5
Los tres lados a,b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.
Escriba un programa que reciba desde teclado los 3 lados de un triángulo (código main) y llame a una función verificar_triangulo(lista) que reciba una lista con los 3 lados ingresados y devuelva un mensaje:
● Si acaso el triángulo es invalido; y
● Si no lo es, qué tipo de triángulo es (Escaleno, Isósceles o Equilátero).
Considere que un triángulo Escaleno tiene todos sus lados distintos, un triángulo Isósceles tiene 2 lados iguales y un triángulo Equilátero tiene sus 3 lados iguales.
Nota: Debe tener un código main, una función definida y desde el código main debe llamar a
la función solicitada.
"""


def ingresarLados() -> list:
    """
    Función que solicita al usuario los 3 lados del triángulo y los almacena en una lista
    
    Returns:
        list: Lista con los 3 lados del triángulo
    """
    lados = []
    for i in range(3):
        lado = int(input("[+] Ingrese los 3 lados del triángulo: "))
        lados.append(lado)
    return lados

def verificar_triangulo(lista: list) -> str:
    """
    Función que recibe una lista con los 3 lados de un triángulo y devuelve un mensaje indicando si es un triángulo válido y de qué tipo es
    
    Args:
        lista (list): Lista con los 3 lados del triángulo
    
    Returns:
        str: Mensaje indicando si es un triángulo válido y de qué tipo es
    """
    # Convertir la lista en una tupla
    lados = tuple(lista)
    l1, l2, l3 = lados

    # Verificar si los lados forman un triángulo válido
    if not (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
        return "No es un triángulo"

    # Es un triángulo
    if l1 == l2 and l1 == l3:
        return "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Isósceles"
    else:
        return "Escaleno"

### MAIN ###

resp = "s"
while resp.lower() == "s":
    
    # Validar que sea un triángulo
    print(verificar_triangulo(ingresarLados()))

    resp = input("[+] Desea continuar? (s/n): ") 
