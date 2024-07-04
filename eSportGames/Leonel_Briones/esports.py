

def menu(menu: str, juegos: list, tipoJugador: list, id: int, registros: list):
    while True:
        print(menu)
        opcion = input("[+] Ingrese opción: ")
        if opcion == "1":
            print("REGISTRAR PUNTAJES")
            registros = registrarPuntaje(id, juegos,tipoJugador, registros)
            print(registros)
        elif opcion == "2":
            print("LISTAR TODOS LOS PUNTAJES")
        elif opcion == "3":
            print("IMPRIMIR POR TIPO")
        elif opcion == "4":
            print("SALIR")
            break
        else:
            print("[!] ERROR: Opción ingresada no es válida")

def registrarPuntaje(id: int, juegos: list, tipoJugador: list, registros: list) -> list:
    
    jugador = {}
    id = idSiguiente(id)
    NOMBRE_COMPLETO = solicitarNombreApellido()
    JUEGOS_A_PARTICIPAR = seleccionarJuegos(juegos)
    CATEGORIA = seleccionarTipoJugador(tipoJugador)
    
    jugador['id'] = id
    jugador['nombre'] = NOMBRE_COMPLETO
    jugador['juegos'] = JUEGOS_A_PARTICIPAR
    jugador['categoria'] = CATEGORIA
    
    #print(jugador)
    registros.append(jugador)
    #print(registros)
    return registros

def idSiguiente(id: int) -> int:
    global id_jugador
    id_jugador += 1
    return id_jugador

def solicitarNombreApellido():
    while True:
        nombreCompleto = input("[+] Ingrese nombre y apellido: " ).capitalize().strip()
        if len(nombreCompleto) > 0:
            return nombreCompleto
        
def esNumero(numero: str | int) -> bool:
    try:
        int(numero)
        return True
    except Exception as e:
        print(f"[!] ERROR: Valor no numérico")
        return False

def cantidadJuegos(juegos: list) -> int:
    cantidad = input(f"[+] Ingrese cantidad de juegos a participar (Máximo {len(juegos)}): ")
    if esNumero(cantidad):
        cantidad = int(cantidad)
        if cantidad < 0:
            print("[!] ERROR: Valor ingreado debe ser mayor a cero")
        else:
            return cantidad

def seleccionarJuegos(juegos: list) -> list:
    
    seleccionMenu = list(juegos)
    seleccionJuegos = []
    print(seleccionMenu) # TODO: BORRAR
    
    maxJuegos = cantidadJuegos(juegos)
    
    for i in range(maxJuegos):
        for j in range(len(seleccionMenu)):
            print(f"{j + 1}. {seleccionMenu[j]}")

        while True:
            sel = input("[+] Ingrese juego a participar: ")
            if esNumero(sel):
                sel = int(sel)
                if sel < 1 or sel > len(seleccionMenu):
                    print("[!] ERROR: Valor ingresado no está disponible")
                else:
                    seleccionJuegos.append(seleccionMenu.pop(sel - 1))
                    break
        #END WHILE
    #END FOR
    return seleccionJuegos

def seleccionarTipoJugador(TIPO_JUGADOR: list) -> str:
    MIN = 0
    MAX = len(TIPO_JUGADOR)
    for i in range(MAX):
            print(f"{i + 1}. {TIPO_JUGADOR[i]}")
    while True:
        sel = input("[+] Ingrese tipo jugador: ")
        if esNumero(sel):
            sel = int(sel)
            if sel < MIN or sel > MAX:
                print("[!] ERROR: Valor ingresado no está en las opciones")
            else:
                return TIPO_JUGADOR[sel - 1]
        #END WHILE

if __name__ == "__main__":
    JUEGOS = ["Fornite", "FIFA", "Valorant"]
    TIPO_JUGADOR = ["Principiante", "Avanzado", "Experto"]
    id_jugador = 0
    MENU = "\n1. Registrar puntajes de torneo\n2. Listar todos los puntajes\n3. Imprimir por tipo\n4. Salir del programa"
    registros = []
    
    menu(MENU, JUEGOS, TIPO_JUGADOR, id_jugador, registros)