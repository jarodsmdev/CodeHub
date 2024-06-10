"""
Ejercicio 1B
HHaga un programa que permita ingresar el nombre de un jugador y un equipo, y entregue el número de camiseta de ese jugador. Si el nombre no existe, debe entregar un mensaje diciendo: “jugador no existe”.
"""

def ingresarData(mensaje):
    return input(mensaje)

def seleccionarEquipo(opcion):
    if opcion == "chile":
        return Chile

    elif opcion == "argentina":
        return Argentina

    else:
        return None

def seleccionarJugador(jugador, diccionario):
    existe = False
    for camiseta in diccionario:
        if diccionario[camiseta].lower() == jugador:
            print("[!] Camiseta N°:",camiseta) # Imprime el número de camiseta
            existe = True
    return existe

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

# Main
jugador = ingresarData("[+] Escriba un nombre de Jugador: ").lower()
equipo = ingresarData("[+] Escriba un país: ").lower()

# Asignación del diccionario en base a la selección del usuario

if seleccionarEquipo(equipo) != None:
    diccionario = seleccionarEquipo(equipo)
    jugador = seleccionarJugador(jugador, diccionario)
    if not jugador:
        print("[!] ERROR: Jugador no existe")
else:
    print("[!] ERROR: No ha seleccionado un equipo válido (Chile o Argentina)")

print("\n[!] Fin del programa")