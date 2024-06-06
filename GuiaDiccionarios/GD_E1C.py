"""
Ejercicio 1C
Haga un programa que permita ingresar por teclado un número de camiseta y entregue los jugadores (de ambos equipos si fuese el caso) que usan ese número.
"""

def validarEntero(numero):
    esNumero = False
    try:
        numero = int(numero)
        esNumero = True
    except:
        pass
    return esNumero

def ingresarData(mensaje):
    return input(mensaje)


def buscarJugador(diccionario, numCamiseta):
    for camiseta in diccionario:
        if camiseta == int(numCamiseta):
            print(diccionario[camiseta])


Chile = {
    1: 'Claudio Bravo',
    4: 'Mauricio Isla',
    17: 'Gary Medel',
    18: 'Gonzalo Jaro',
    15: 'Jean Beausejour',
    8: 'Arturo Vidal',
    21: 'Marcelo Díaz',
    20: 'Charles Aranguiz',
    6: 'José Pedro Fuenzalida',
    7: 'Alexis Sánchez',
    11: 'Eduardo Vargas'
}

Argentina = {
    1: 'Sergio Romero',
    4: 'Gabriel Mercado',
    17: 'Nicolás Otamendi',
    13: 'Ramiro Funes Mori',
    16: 'Marcos Rojo ',
    6: 'Lucas Biglia',
    14: 'Javier Mascherano',
    19: 'Éver Banega',
    10: 'Lionel Messi',
    9: 'Gonzalo Higuaín',
    7: 'Ángel Di María'
}

### MAIN ###
numCamiseta = ingresarData("[+] Escriba un número de camiseta: ")

# Validar si el número de camiseta es un número entero
if not validarEntero(numCamiseta):
    print("[!] ERROR: Ingrese un valor numérico")
else:
    # Agrega ambos diccionarios en una lista para reccoerlos
    diccionarios = [Chile, Argentina]
    
    # Recorrer lista de diccionarios en busca del número de camiseta
    for diccionario in diccionarios:
        # Imprimir el nombre del pais (Chile o Argentina)
        if diccionario == Chile:
            print("\n[!] Jugadores de Chile:")
        else:
            print("\n[!] Jugadores de Argentina:")
        # Buscar el jugador con el número de camiseta ingresado
        buscarJugador(diccionario, numCamiseta)

print("\n[!] Fin del programa")