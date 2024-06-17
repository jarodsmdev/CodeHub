"""
Ejercicio 1A
Haga un programa que permita escribir por teclado un equipo (Chile o Argentina), un número de camiseta y entregue el nombre del jugador. Considere el caso en el cual el número entregado por teclado no exista.
"""

def validarEntero(numero: str | int | float) -> bool:
    esNumero = False
    try:
        numero = int(numero)
        esNumero = True
    except:
        pass
    return esNumero

def ingresarData(mensaje: str):
    return input(mensaje)

def seleccionarEquipo(opcion: str, Chile: dict, Argentina: dict) -> dict | None:
    if opcion == "chile":
        return Chile

    elif opcion == "argentina":
        return Argentina

    else:
        return None

def buscarJugador(diccionario: dict):
    num = ingresarData("[+] Ingrese un numero de camiseta: ")
    
    if not validarEntero(num):
        print("[!] ERROR: Ingrese un valor numérico")
    else:
        existe = False
        for camiseta in diccionario:
            if camiseta == int(num):
                print(diccionario[camiseta])
                existe = True
                
        if existe == False:
            print("No existe el jugador con la camiseta", num)

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
equipo = ingresarData("[+] Escriba un país: ").lower()

# Asignación del diccionario en base a la selección del usuario
if seleccionarEquipo(equipo, Chile, Argentina) != None:
    diccionario = seleccionarEquipo(equipo, Chile, Argentina)
    buscarJugador(diccionario)
else:
    print("[!] ERROR: No ha seleccionado un equipo válido (Chile o Argentina)")

print("\n[!] Fin del programa")