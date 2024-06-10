"""
Ejercicio 2:
Haga un programa que permita agregar 3 nombres en una lista y un nombre a buscar. El programa debe entregar las veces que aparece ese nombre en la lista. Considere que el programa debe funcionar para nombres en minúsculas y mayúsculas.

Ejemplo 1:
Ingrese nombre: Mabel
Ingrese nombre: ANA
Ingrese nombre: pedro
Ingrese nombre a buscar: ana
El nombre aparece 1 vez

Ejemplo 2:
Ingrese nombre: ana
Ingrese nombre: ANA
Ingrese nombre: pedro
Ingrese nombre a buscar: Ana
El nombre aparece 2 veces
"""

def ingresoNombres(cantidadIngresos):
    """
    Funcion que permite ingresar nombres a una lista

    Parametros:
    cantidadIngresos: Cantidad de nombres a ingresar

    Retorna:
    lista: Lista con los nombres ingresados (list)
    """
    lista = []
    for i in range(cantidadIngresos):
        while True:
            nombre = input(f"[+] Ingrese nombre {i + 1}: " ).capitalize()
            if nombre != None or len(nombre) > 0:
                lista.append(nombre)
                break
            else:
                print("[!] ERROR: No ha ingresado un nombre.  Vuelva a intentar")
    return lista

def contarNombres(nombre, listaNombres):
    """
    Funcion que cuenta la cantidad de veces que aparece un nombre en una lista
    
    Parametros:
    nombre: Nombre a buscar
    listaNombres: Lista de nombres
    
    Retorna:
    contador: Cantidad de veces que aparece el nombre en la lista de nombres (int)
    """
    contador = 0
    for n in listaNombres:
        if n == nombre:
            contador += 1
    return contador

### MAIN ###
# Constante de cantidad de nombres a ingresar
CANT_NOMBRE_MAX = 3

# Ingreso de nombres a la lista invocando una funcion
lista = ingresoNombres(CANT_NOMBRE_MAX)

# Ingreso de nombre a buscar
nombre = input("[+] Ingrese nombre a buscar: ").capitalize()

# Contar la cantidad de veces que aparece el nombre en la lista involucrando una funcion
cantidadRepeticiones = contarNombres(nombre, lista)

# Mostrar resultado
print(f"El nombre aparece {cantidadRepeticiones} {"vez" if cantidadRepeticiones == 1 else "veces"}")