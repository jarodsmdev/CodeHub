"""
Ejercicio 5
Haga un programa que permita ingresar un número entero positivo. Dado este número, debe generar una lista con números del 0 hasta el número ingresado usando la función range(). El programa debe entregar la desviación estándar de los números de la lista.
Ejercicio 1:

Ingrese número: 5
La desviación estándar es: 1.7
Ejercicio 2:

Ingrese número: 1
La desviación estándar es: 0.5
"""
def esNumero(numero: str) -> bool:
    """
    Verifica si una cadena puede convertirse en un número.
    
    Args:
        numero (str): La cadena a verificar.
        
    Returns:
        bool: True si la cadena puede convertirse en un número.
    """
    try:
        numero = float(numero)
        return True
    except:
        print("[!] ERROR: Valor ingresado no es numérico")
    return False

def ingresoEnteroPositivo() -> int:
    """
    Solicita un número por teclado y valida que sea positivo.
    
    Returns:
        int: Número entero positivo

    """
    while True:
        numero = input("[+] Ingrese un número: ")
        if esNumero(numero):
            numero = int(numero)
            if numero > 0:
                return numero
            else:
                print("[!] Debe ser un número positivo")

def promedio(lista: list) -> float:
    """
    Calcula el promedio de una lista.
    
    Args:
        lista (list): La lista a utilizar para el cálculo.
        
    Returns:
        float: promedio calculado mediante los datos de una lista.
    """
    if len(lista) == 0:
        return 0
    else:
        prom = sum(lista)/len(lista)
        return prom
    
def desviacion_estandar(lista: list) -> float:
    """
    Calcula la desviación estándar
    
    Args:
        lista (list): Una lista con números para realizar los cálculos
    
    Returns:
        float: Resultado calculado mediante fórmula implementada
    """
    if len(lista) == 0:
        return 0
    else:
        media = promedio(lista)
        suma_cuadrados = 0
        for x in lista:
            suma_cuadrados += (x - media) ** 2
        varianza = suma_cuadrados / len(lista)
        return varianza ** 0.5

### MAIN ###
numero = ingresoEnteroPositivo()
lista = range(numero + 1)

print(f"La desviación estándar es: {round(desviacion_estandar(lista),1)}")

