def crearTitulo(titulo: str) -> str:
    longitud = len(titulo)
    linea = "=" * (longitud + 4)  # Se suman 4 para los espacios antes y después del título
    return f"\t{linea}\n\t  {titulo}  \n\t{linea}"

def menu(menu: str, juegos: list, tipoJugador: list, id: int, registros: list):
    while True:
        print(crearTitulo("== eSPORT GAMES =="))
        print(menu)
        opcion = input("[+] Ingrese opción: ")
        if opcion == "1":
            print(crearTitulo("REGISTRAR PUNTAJES"))
            registros = registrarPuntaje(id, juegos,tipoJugador, registros)
            print(registros) #TODO: BORRAR
        elif opcion == "2":
            print(crearTitulo("LISTAR TODOS LOS PUNTAJES"))
            
            #TODO: BORRAR DATOS DE PRUEBA
            if len(registros) == 0:
                registros = [{'id': 1, 'nombre': 'Jugador A', 'categoria': 'Experto', 'juegos': {'Fornite': 125000}},
                             {'id': 2, 'nombre': 'Jugador B', 'categoria': 'Experto', 'juegos': {'FIFA': 3500, 'Valorant': 0}},
                             {'id': 3, 'nombre': 'Jugador C', 'categoria': 'Avanzado', 'juegos': {'Fornite': -9, 'FIFA': 5, 'Valorant': 1500}}]
            
            listarPuntajes(registros)
        elif opcion == "3":
            print(crearTitulo("IMPRIMIR POR TIPO"))
        elif opcion == "4":
            print(crearTitulo("SALIR"))
            print("[!] Saliendo...")
            break
        else:
            print("[!] ERROR: Opción ingresada no es válida")
            
def guardarPuntaje(juego: str) -> int:
    while True:
        puntos = input(f"[+] Ingrese puntaje para el juego {juego}: ")
        if esNumero(puntos):
            return int(puntos)
    #END WHILE

def registrarPuntaje(id: int, juegos: list, tipoJugador: list, registros: list) -> list:
    
    jugador = {}
    id = idSiguiente(id)
    NOMBRE_COMPLETO = solicitarNombreApellido()
    JUEGOS_A_PARTICIPAR = seleccionarJuegos(juegos)
    CATEGORIA = seleccionarTipoJugador(tipoJugador)
    
    jugador['id'] = id
    jugador['nombre'] = NOMBRE_COMPLETO
    jugador['categoria'] = CATEGORIA
    #Guarda en este formato: key juegos {"FIFA":3500, "FORNITE": 125000, "VALORANT": 0}
    jugador['juegos'] = {}
    for juego in JUEGOS_A_PARTICIPAR:
        # Permitir guardar un valor numérico para registrar el puntaje
        jugador['juegos'][juego] = guardarPuntaje(juego)
    
    registros.append(jugador)

    return registros

def idSiguiente(id: int) -> int:
    global id_jugador
    id_jugador += 1
    return id_jugador

def solicitarNombreApellido():
    while True:
        nombreCompleto = input("[+] Ingrese nombre y apellido: " ).title().strip()
        if len(nombreCompleto) > 0:
            return nombreCompleto
        
def esNumero(numero: str | int) -> bool:
    try:
        int(numero)
        return True
    except Exception as e:
        print(f"[!] ERROR: Valor ingresado debe ser numérico")
        return False

def cantidadJuegos(juegos: list) -> int:
    cantidad = input(f"[+] Ingrese cantidad de juegos a participar (Máximo {len(juegos)}): ")
    if esNumero(cantidad):
        cantidad = int(cantidad)
        if cantidad < 0:
            print("[!] ERROR: Valor ingresado debe ser mayor a cero")
        else:
            return cantidad

def seleccionarJuegos(juegos: list) -> list:
    contador = 1
    seleccionMenu = list(juegos)
    seleccionJuegos = []
    print(seleccionMenu) #TODO: BORRAR
    
    maxJuegos = cantidadJuegos(juegos)
    
    if maxJuegos == len(juegos):
        seleccionJuegos = juegos
    else:
        for i in range(maxJuegos):
            for j in range(len(seleccionMenu)):
                print(f"\t{j + 1}. {seleccionMenu[j]}")

            while True:
                sel = input(f"[+] Ingrese juego {contador} a participar: ")
                if esNumero(sel):
                    sel = int(sel)
                    if sel < 1 or sel > len(seleccionMenu):
                        print("[!] ERROR: Valor ingresado no está disponible")
                    else:
                        seleccionJuegos.append(seleccionMenu.pop(sel - 1))
                        contador += 1
                        break
            #END WHILE
        #END FOR
    #END IF
    return seleccionJuegos

def seleccionarTipoJugador(TIPO_JUGADOR: list) -> str:
    MIN = 0
    MAX = len(TIPO_JUGADOR)
    for i in range(MAX):
            print(f"\t{i + 1}. {TIPO_JUGADOR[i]}")
    while True:
        sel = input("[+] Ingrese tipo jugador: ")
        if esNumero(sel):
            sel = int(sel)
            if sel < MIN or sel > MAX:
                print("[!] ERROR: Valor ingresado no está en las opciones")
            else:
                return TIPO_JUGADOR[sel - 1]
        #END WHILE
        
def listarPuntajes():
    print("Id Jugador | Nombre | VALORANT | FORNITE | FIFA | Tipo")

if __name__ == "__main__":
    JUEGOS = ["Fornite", "FIFA", "Valorant"]
    TIPO_JUGADOR = ["Principiante", "Avanzado", "Experto"]
    id_jugador = 0
    MENU = "\n1. Registrar puntajes de torneo\n2. Listar todos los puntajes\n3. Imprimir por tipo\n4. Salir del programa\n"
    registros = []
    
    menu(MENU, JUEGOS, TIPO_JUGADOR, id_jugador, registros)