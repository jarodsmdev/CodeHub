"""
Ejercicio 1D
Eliminar Jugador por Nombre
Haga un programa que permita ingresar el nombre de un jugador y elimine ese jugador del diccionario. Note que no se ingresa por teclado el equipo (debe buscar el nombre en ambos diccionarios). Si el nombre del jugador no existe, entonces debe entregar un mensaje diciendo: “jugador no existe”.
"""

def ingresarData(mensaje):
    return input(mensaje)


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
# Solicitar el nombre del jugador a eliminar
nombreJugador = ingresarData("[+] Escriba el nombre del jugador a eliminar: ").lower()

# Agregar ambos diccionarios en una lista para recorrerlos
equipos = [Chile, Argentina]

# Recorrer ambos diccionarios
jugagorEncontrado = False
for equipo in equipos:
    # Recorrer los jugadores de cada equipo
    for camiseta in equipo:
        # Si el nombre del jugador es igual al nombre del jugador en el diccionario
        if equipo[camiseta].lower() == nombreJugador:
            jugagorEncontrado = True
            print(f"[+] El jugador {nombreJugador.capitalize()} ha sido eliminado")
            # Eliminar el jugador del diccionario
            del equipo[camiseta]
            # Salir del bucle
            break
    break
# Si el jugador no fue encontrado en ninguno de los equipos
if not jugagorEncontrado:
    print("[!] Jugador no existe")

print("\n[!] Fin del programa")