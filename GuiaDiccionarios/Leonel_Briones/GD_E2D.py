"""
Ejercicio 2D:
Trabajaremos con un diccionario que tiene como llaves poderes, y como valores listas de nombres de superhéroes.

A. Agregar Superhéroe a Poder

Haga un programa que permita ingresar un poder y un nombre de superhéroe, y agregue ese superhéroe a la lista de ese poder. Considere que si el poder no existe en el diccionario, debe crearlo junto con la lista y el superhéroe recién ingresado por teclado. Si el poder existe y el superhéroe también, entonces no debe ingresarlo para que así no se repitan nombres.

B. Eliminar Superhéroe

Haga un programa que permita ingresar por teclado un superhéroe y elimine ese superhéroe de todo el diccionario.

C. Consultar Superhéroes por Poderes

Haga un programa que permita ingresar por teclado 2 poderes y entregue una lista con todos los superhéroes que tienen al menos uno de esos poderes. Los nombres en la lista no deben repetirse.

D. Consultar Superhéroes por Poderes Combinados

Haga un programa que permita ingresar por teclado 2 poderes y entregue una lista con los superhéroes que tienen ambos poderes. Si no hay superhéroe que tenga ambos poderes, debe entregar un mensaje que diga: “No existe superhéroe que tenga esos poderes”.
"""

# Función que verifica si el poder (key) existe en el diccionario
def existePoder(poder: str, diccionario: dict) -> bool:
    if poder in diccionario:
        return True
    else:
        return False

# Función que verifica si el superhéroe existe en la lista de un poder(key)
def existeSuperheroe(superheroe: str, diccionario: dict, poder) -> bool:
    for nombre in diccionario[poder]:
        if nombre == superheroe:
            return True
    return False

# Función que elimina un superhéroe de todo el diccionario
def eliminarSuperheroe(superheroe: str, diccionario: dict):
    eliminado = False
    contador = 0
    for poder in diccionario:
        for s in diccionario[poder]:
            if s == superheroe:
                diccionario[poder].remove(superheroe)
                eliminado = True
                contador = contador + 1
    if eliminado:
        print(f"[!] Superhéroe {superheroe} eliminado correctamente, {contador} veces")
    else:
        print("[!] No se ha encontrado el superhéro a eliminar")
    

# Función que valida si un número es entero
def validarNumeroEntero(numero: any) -> bool:
    try:
        numero = int(numero)
        return True
    except:
        return False
    
# Muestra por terminal diccionario sin formato
def mostrarDiccionario(diccionario: dict):
    print(diccionario)

# Función que agrega un superhéroe a un poder (key) del diccionario
def agregarSuperheroe():
    # Solicitar al usuario el poder y el superhéroe
    poder = input("[+] Ingrese un poder: ").capitalize()
    superHeroe = input("[+] Ingrese un nombre de superhéroe: ").capitalize()

    # Verificar si el poder Existe como clave en el diccionario
    if existePoder(poder, poderes):
        # Verfificar si existe el superhéroe con el poder
        if not existeSuperheroe(superHeroe, poderes, poder):
            # No existe superhéroe con ese poder en los values del diccionario. Se agrega a la lista
            poderes[poder].append(superHeroe)
            print(f"[!] Superhéroe {superHeroe} agregado correctamente a la lista {poder}")
        else:
            print(f"[!] Superhéroe {superHeroe} ya existe con el poder {poder}")
    else:
        # No existe se agrega como Key el poder y el nombre como value como una lista
        poderes[poder] = [superHeroe]
        print(f"[!] Poder: {poder}, Superhéroe: {superHeroe} agregado correctamente!")

def solicitarPoderes(cantidadPoderes: int, diccionario: dict) -> list:
    listaPoderes = []
    contador = 0
    while contador < cantidadPoderes:
        # Solicitar poder al usuario
        poder = input(f"[+] Ingrese poder {contador + 1} a filtrar: ").capitalize()
        
        # Verificar si el poder (key) ingresado existe en el diccionario
        if not existePoder(poder, diccionario):
            print("[!] ERROR: El poder ingresado no existe")
        else:
            # Verificar si el poder ya se encuentra en la lista de poderes (evitar repetidos)
            if poder in listaPoderes:
                print("[!] Poder ya se encuentra seleccionado")
            else:
                # Agregar poder a la lista de poderes
                contador += 1
                listaPoderes.append(poder)
        # FIN WHILE
    return listaPoderes

def filtrarPorPoderes(diccionario: dict) -> list:
    # Constante para el filtro de superhéroes
    MAX_FILTRO_PODER = 2
    
    # Variables para el filtro
    listaPoderes = []
    listaSuperheroes = []


    # Pedir 2 poderes para realizar el filtro de superhéroes, sin repetir
    listaPoderes = solicitarPoderes(MAX_FILTRO_PODER, diccionario)
    
    # Se crea un conjunto vacío, el cual recibirá los superhéroes filtrados
    # Se utiliza un conjunto para evitar duplicados, ya que por definición no permite elementos repetidos
    filtro = set()
    
    # Filtrar superhéroes que tengan al menos uno de los poderes seleccionados
    for p in listaPoderes:
        for p in diccionario[p]:
            filtro.add(p)
            
    # Convertir el conjunto a lista
    listaSuperheroes = list(filtro)
    
    # Retornar lista de superhéroes filtrados
    return listaSuperheroes

# Función que filtra superhéroes por poderes combinados
def filtrarPorPoderesCombinados(diccionario: dict):
    
    # Constante para el filtro de superhéroes
    # Llama a la función solicitarPoderes para obtener los poderes a filtrar
    PODERES = solicitarPoderes(2, diccionario)
    
    # Se crea un conjunto vacío, el cual recibirá los superhéroes filtrados
    interseccion = set()
    
    # Recorro los poderes sólo hasta la penúltima posición ya que se compara con el siguiente poder
    # Si el superhéroe tiene ambos poderes, se agrega al conjunto intersección
    for i in range(len(PODERES) - 1):
        interseccion = set(diccionario[PODERES[i]]).intersection(set(diccionario[PODERES[i + 1]]))
    
    # Si no hay superhéroes con ambos poderes, se imprime un mensaje
    if (len(interseccion)) == 0:
        print("[!] No existe superhéroe que tenga esos poderes")
    else:
        print(list(interseccion))

# Diccionario con los poderes y superhéroes
poderes = {
    "Volar": ["Superman", "Mujer maravilla", "Ironman"],
    "Rayos": ["Superman", "Ironman", "Ciclope", "Capitana marvel"],
    "Velocidad": ["Flash", "Superman"],
    "Fuerza": ["Hulk", "Mujer maravilla", "Superman"],
    "Inteligencia": ["Ironman", "Profesor-X"]
}

MENU = """
1. Agregar Superhéroe a Poder
2. Eliminar Superhéroe
3. Consultar Superhéroes por Poderes
4. Consultar Superhéroes por Poderes Combinados
5. Mostrar diccionario
0. Salir
"""

### MAIN ###
while True:
    print(MENU)
    opcion = input("[+] Ingrese una opción: ")
    if validarNumeroEntero(opcion):
        opcion = int(opcion)
        if opcion == 1:
            print("--- AGREGAR SUPERHÉROE ---\n")
            agregarSuperheroe()
        elif opcion == 2:
            print("--- ELIMINAR SUPERHÉROE ---\n")
            superheroe = input("[+] Ingrese nombre de superhéroe: ").capitalize()
            eliminarSuperheroe(superheroe, poderes)
        elif opcion == 3:
            print("--- CONSULTAR SUPERHEROES ---\n")
            print(filtrarPorPoderes(poderes))
        elif opcion == 4:
            print("--- CONSULTAR PODERES COMBINADOS ---\n")
            filtrarPorPoderesCombinados(poderes)
        elif opcion == 5:
            print("--- MOSTRAR SUPERHÉROES ---\n")
            mostrarDiccionario(poderes)
        elif opcion == 0:
            print("[!] Saliendo del programa")
            break
    else:
        print("[!] ERROR: Ingrese un valor numérico")



print("\n",poderes)
