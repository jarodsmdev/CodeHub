"""
Ejercicio 6:
Haga un programa que reciba 3 nombres y 3 apellidos. Estos deben ser almacenados en 2 listas, una para nombres y otra para apellidos. Luego, el programa debe preguntar por un apellido y se debe mostrar por pantalla el nombre asociado a ese apellido. Si el apellido se repite una o más veces, debe mostrar todos los nombres asociados a ese apellido, sino, debe mostrar el mensaje: apellido no encontrado.

Ejemplo 1:
Ingrese nombre: max
Ingrese apellido: diaz
Ingrese nombre: juan
Ingrese apellido: diaz
Ingrese nombre: marcela
Ingrese apellido: gonzalez
Pregunte por un apellido: diaz
Nombre encontrado: max
Nombre encontrado: juan

Ejemplo 2:
Ingrese nombre: max
Ingrese apellido: diaz
Ingrese nombre: juan
Ingrese apellido: diaz
Ingrese nombre: marcela
Ingrese apellido: gonzalez
Pregunte por un apellido: soto
Apellido no encontrado
"""

def devolverNombres(apellido: str, listaNombres: list, listaApellidos: list) -> list:
    """
    Dado un apellido busca su correspondiente nombre y retorna una lista
    
    Args:
        apellido (str): Apellido a buscar en una lista
        listaNombres (list): Lista de nombres para ser filtrada
        listaApellidos (list): Lista de apellidos para realizar la búsqueda
    
    Returns:
        list : Retorna una lista de nombres que coincidan con el apellido previamente indicado
    """
    nombres = []
    for i in range(len(listaApellidos)):
        if apellido == listaApellidos[i]:
            nombres.append(listaNombres[i])
    return nombres

def imprimirNombres(listNombres: list):
    """
    Imprime por pantalla (terminal) nombres en cado de incluirlos en la lista, caso contrario imprimirá que no se encuentra apellido
    
    Args:
        listNombres (list): Lista de nombres para realizar la impresión por pantalla (terminal)
    """
    if len(listNombres) == 0:
        print("[!] Apellido no encontrado")
    else:
        for nombre in listNombres:
            print(f"[!] Nombre encontrado: {nombre}")

### MAIN ###

MAX_INGRESOS = 3

nombres = []
apellidos = []

for i in range(MAX_INGRESOS):
    # Solicitar nombre y apellido, se guardan en formato Capitalize
    nombre = input("[+] Ingrese nombre: ").capitalize()
    apellido = input("[+] Ingrese apellido: ").capitalize()
    # Se almacenan por separado tanto nombre como apellido en lista individuales
    nombres.append(nombre.strip())
    apellidos.append(apellido.strip())
    
# Solicitar un apellido al usuario
apellido = input("[+] Pregunte por un apellido: ").capitalize().strip()

# Devolver nombres que coincidan con el apellido ingresado anteriormente
resultado = devolverNombres(apellido, nombres, apellidos)

# Imprimir por pantalla nombres que coincidan con el apellido
imprimirNombres(resultado)

