"""
Ejercicio 2B:
Trabajaremos con un diccionario que tiene como llaves poderes, y como valores listas de nombres de superhéroes.

A. Agregar Superhéroe a Poder

Haga un programa que permita ingresar un poder y un nombre de superhéroe, y agregue ese superhéroe a la lista de ese poder. Considere que si el poder no existe en el diccionario, debe crearlo junto con la lista y el superhéroe recién ingresado por teclado. Si el poder existe y el superhéroe también, entonces no debe ingresarlo para que así no se repitan nombres.

B. Eliminar Superhéroe

Haga un programa que permita ingresar por teclado un superhéroe y elimine ese superhéroe de todo el diccionario.
"""

# Función que verifica si el poder existe en el diccionario
def existePoder(poder, diccionario):
    if poder in diccionario:
        return True
    else:
        return False

# Función que verifica si el superhéroe existe en la lista de un poder
def existeSuperheroe(superheroe, diccionario, poder):
    for nombre in diccionario[poder]:
        if nombre == superheroe:
            return True
    return False

# Función que elimina un superhéroe de todo el diccionario
def eliminarSuperheroe(superheroe, diccionario):
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
def validarNumeroEntero(numero):
    try:
        numero = int(numero)
        return True
    except:
        return False

def mostrarDiccionario(diccionario):
    print(diccionario)

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


# Diccionario con los poderes y superhéroes
poderes = {
    "Volar": ["Superman", "Mujer maravilla", "Ironman"],
    "Rayos": ["Superman", "Ironman", "Ciclope", "Capitana marvel"],
    "Velocidad": ["Flash", "Superman"],
    "Fuerza": ["Hulk", "Mujer maravilla", "Superman"],
    "Inteligencia": ["Ironman", "Profesor-X"]
}

menu = """
1. Agregar Superhéroe a Poder
2. Eliminar Superhéroe
4. Mostrar diccionario
0. Salir
"""

### MAIN ###
while True:
    print(menu)
    opcion = input("[+] Ingrese una opción: ")
    if validarNumeroEntero(opcion):
        opcion = int(opcion)
        if opcion == 1:
            agregarSuperheroe()
        elif opcion == 2:
            superheroe = input("[+] Ingrese nombre de superhéroe: ").capitalize()
            eliminarSuperheroe(superheroe, poderes)
        elif opcion == 4:
            mostrarDiccionario(poderes)
        elif opcion == 0:
            print("[!] Saliendo del programa")
            break
    else:
        print("[!] ERROR: Ingrese un valor numérico")



print("\n",poderes)
