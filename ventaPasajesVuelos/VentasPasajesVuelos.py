### DECLARACIÓN DE FUNCIONES ###
import signal
import sys

def signal_handler(sig: int, frame: signal):
    print("\n[!] Saliendo del programa...")
    sys.exit(0)
    
def calcularDescuentoBanco(banco, precio):
    if banco in CONVENIOS_BANCO:
        precioRebajado = precio * CONVENIOS_BANCO[banco]
        print(f"[!] Su banco tiene oferta de un 15% de descuento\n[!] El valor del asiento es: {precio}\n[!] Precio con descuento es: ${round(precioRebajado)}")
    else:
        print(f"[+] El valor del asiento es: ${precio}")

def mostrarMenu(menu: str, lista_asientos: list, asientoVip: int):
    """
    Función que muestra un menú de opciones y ejecuta la opción seleccionada
    
    Args:
        menu (str): Cadena de texto con las opciones del menú
        lista_asientos (list): Matriz de asientos del avión
        asientoVip (int): Número de asiento que comienza a ser considerado como VIP
    """
    diccPasajeros = {}
    isRunning = True
    while isRunning:
        signal.signal(signal.SIGINT, signal_handler)
        print(MENU)
        choice = input("[+] Seleccione una opción: ")
        if choice == "1":
            print("""\t================\n\tVER ASIENTOS DISPONIBLES\n\t================""")
            mostrarAsientos(lista_asientos, ASIENTO_VIP)
        elif choice == "2":
            print("""\t================\n\tCOMPRAR ASIENTO\n\t================""")
            diccPasajeros, asiento, banco = solicitarInformacionPasajero(diccPasajeros)
            #print(diccPasajeros)
            precio = calcularValorAsiento(asiento, ASIENTO_VIP, VALORES_ASIENTOS)
            calcularDescuentoBanco(banco, precio)
            ocuparAsiento(asiento, lista_asientos)
        elif choice == "3":
            print("""\t================\n\tANULAR VUELO\n\t================""")
        elif choice == "4":
            print("""\t================\n\tMODIFICAR DATOS DE PASAJERO\n\t================""")
        elif choice == "5":
            print("""\t================\n\tSALIR\n\t================""")
            print("[+] Saliendo del programa...")
            isRunning = False

def ocuparAsiento(asiento: int, listaAsientos: list):
    #print(lista_asientos)
    for fila in range(len(listaAsientos)):
        for columna in range(len(listaAsientos[fila])):
            posicion = (len(listaAsientos[fila]) * fila) + columna + 1
            if posicion == asiento:
                if posicion < 10:
                    listaAsientos[fila][columna] = "X"
                else:
                    listaAsientos[fila][columna] = "X "
    #print(lista_asientos)
    

def crearAsientos(nFilas: int, nColumnas: int) -> list:
    """
    Función que crea una matriz de asientos para un avión
    
    Args:
        nFilas (int): Número de filas de asientos
        nColumnas (int): Número de columnas de asientos
    
    Returns:
        list: Matriz de asientos con números correlativos
    """
    asientos = []  # Crear una lista vacía para almacenar las filas de asientos
    asiento_numero = 1  # Iniciar el contador de asientos desde 1
    for fila in range(nFilas):
        lista_filas = []  # Crear una lista vacía para representar una fila de asientos
        for col_index in range(nColumnas):
            lista_filas.append(asiento_numero)  # Asignar el número correlativo al asiento
            asiento_numero += 1  # Incrementar el contador de asientos
        asientos.append(lista_filas)  # Agregar la fila completa a la matriz de asientos

    return asientos  # Devolver la matriz completa de asientos

def mostrarAsientos(lista: list, vip: int):
    """
    Función que muestra los asientos de un avión en formato de matriz con separaciones
    
    Args:
        lista (list): Matriz de asientos del avión
        vip (int): Número de asiento que comienza a ser considerado como VIP
    
    """
    # Configuración para la distancia del pasillo y el muro separador VIP
    TAMANO_PASILLO_CENTRAL = 5
    MURO_SEPARADOR_VIP = 2
    
    for filas in range(len(lista)):
        print("")
        for columnas in range(len(lista[filas])):
            posicion = (len(lista[filas]) * filas) + columnas + 1

            # Generar separación en el pasillo central
            if columnas == len(lista[filas]) // 2:
                print(" " * TAMANO_PASILLO_CENTRAL, end="")

            # Generar separación entre asientos VIP
            if lista[filas][columnas] == vip:
                # Definimos las partes que se repiten
                separadorVip = "\t|" + "_" * 9 + " " * (TAMANO_PASILLO_CENTRAL + 1) + "_" * 9 + "|"
                
                # Impresión de la separación (muro) entre asientos VIP
                for i in range(MURO_SEPARADOR_VIP):
                    print(separadorVip)

            # Muestra un caracter "|" al inicio de cada fila
            if posicion == 1 * len(lista[filas]) * filas + 1:
                print("\t| ", end="")

            # Imprime el número de asiento exactamente con 2 dígitos
            if posicion < 10:
                print(f"{lista[filas][columnas]} ", end=" ")
            else:
                print(lista[filas][columnas], end=" ")

            # Muestra un caracter "|" al final de cada fila
            if posicion == len(lista[filas]) * (filas + 1):
                print("|", end="")
    print("")
    
def calcularValorAsiento(asiento: int, asientoVIP: int, precios: tuple) -> int:
    """
    Función que calcula el valor de un asiento según su ubicación
    
    Args:
        asiento (int): Número de asiento a calcular
        asientoVIP (int): Número de asiento que comienza a ser considerado como VIP
        precios (tuple): Tupla con los precios de los asientos
    
    Returns:
        int: Valor del asiento
    """
    if asiento < asientoVIP:
        return precios[0]
    else:
        return precios[1]

def cantidadMaximaAsientos(filas: int, columnas: int) -> int:
    """
    Función que calcula la cantidad máxima de asientos en un avión
    
    Args:
        filas (int): Número de filas de asientos
        columnas (int): Número de columnas de asientos
    
    Returns:
        int: Cantidad máxima de asientos en el avión
    """
    return filas * columnas

def asientoDisponible(asiento: int, diccPasajeros: dict) -> bool:
    """
    Función que verifica si un asiento está disponible
    
    Args:
        asiento (int): Número de asiento a verificar
        
    Returns:
        bool: True si el asiento está disponible, False si no lo está
    """
    
    if asiento < 1 or asiento > cantidadMaximaAsientos(FILAS, COLUMNAS):
        print("[!] El asiento seleccionado no existe")
        return False
    else:
        if not comprobarAsientoOcupado(asiento, diccPasajeros):
            return True
        return False
    
def esValorNumerico(valor: str) -> bool:
    """
    Función que verifica si un valor es numérico
    
    Args:
        valor (str): Valor a verificar
        
    Returns:
        bool: True si el valor es numérico, False si no lo es
    """
    try:
        valor = int(valor)
        return True
    except ValueError:
        return False
    
def clienteComproPasajes(rut: str, diccPasajeros: dict) -> bool:
    if rut in diccPasajeros:
        return True
    return False

def ingresarRut(diccPasajeros: dict):
    while True:
        rut = input("[+] Ingrese su RUT: ").replace("-","").replace(".","").replace(" ", "").upper()
        if len(rut) == 0:
            print("[!] ERROR: El RUT no puede estar vacío")
        else:
            if clienteComproPasajes(rut, diccPasajeros):
                print("[!] Usted ya ha comprado un pasaje")
            else:
                break
    return rut
    # Fin While
    
def ingresarAsiento(diccPasajeros: dict) -> int:
    while True:
        asiento = input("[+] Ingrese el número de asiento: ")
        if esValorNumerico(asiento):
            asiento = int(asiento)
            if asientoDisponible(asiento, diccPasajeros):
                break
        else:
            print("[!] El número de asiento debe ser numérico")
    return asiento

def comprobarAsientoOcupado(asiento: int, diccPasajeros: dict) -> bool:
    for rut, datos in diccPasajeros.items():
        if datos["asiento"] == asiento:
            print(f"[!] El asiento {asiento} está ocupado, seleccione otro asiento")
            return True
    return False

def solicitarInformacionPasajero(diccPasajeros)-> tuple:
    """
    Función que solicita la información de un pasajero y la guarda en un diccionario
    
    Returns:
        tuple: Tupla con el diccionario de pasajeros actualizado, el número de asiento y el banco
    """
    
    rut = ingresarRut(diccPasajeros)
    nombre = input("[+] Ingrese su nombre: ").capitalize()
    apellido = input("[+] Ingrese su apellido: ").capitalize()
    telefono = input("[+] Ingrese su teléfono: ")
    banco = input("[+] Ingrese el nombre de su banco: ").upper()
    
    asiento = ingresarAsiento(diccPasajeros)
    
    while True:
        if asientoDisponible(asiento, diccPasajeros):
            diccPasajeros[rut] = {
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono,
                "banco": banco,
                "asiento": asiento
            }
            return (diccPasajeros, asiento, banco)
        else:
            print("[!] El asiento seleccionado no está disponible")


### DECLARACIÓN DE VARIABLES Y CONSTANTES GLOBALES

FILAS = 7
COLUMNAS = 6
ASIENTO_VIP = 31
VALORES_ASIENTOS = (78900, 240000)
CONVENIOS_BANCO = {"BANCO DEL PUEBLO": 85/100}
MENU = """
*********** VUELOS DUOC *************
    1. Ver asientos disponibles
    2. Comprar asiento
    3. Anular vuelo
    4. Modificar datos de pasajero
    5. Salir
"""

### MAIN ###
lista_asientos = []
lista_asientos = crearAsientos(FILAS, COLUMNAS)
#print(lista_asientos)
mostrarMenu(MENU, lista_asientos, ASIENTO_VIP)


