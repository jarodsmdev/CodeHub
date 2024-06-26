import signal, sys

def handler(sig, frame):
    # Ctrl + c
    print("\n\n[!] Interrupción del programa por parte del usuario...")
    sys.exit(1)

def iconosInput(mensaje, icono: str) -> str:
    """
    Función que recibe un mensaje y un ícono y devuelve el mensaje con el ícono al inicio
    
    Args:
        mensaje (str): Mensaje a mostrar
        icono (str): Ícono a mostrar
        
    Returns:
        str: Mensaje con ícono al inicio    
    """
    return f"[{icono}] {mensaje}"

def crearTitulo(titulo: str) -> str:
    """
    Función que recibe un título y lo devuelve con un formato de título
    con un borde de igualdad a los costados y centrado
    
    Args:
        titulo (str): Título a formatear
    
    Returns:
        str: Título formateado
    """
    
    longitud = len(titulo)
    linea = "=" * (longitud + 4)  # Se suman 4 para los espacios antes y después del título
    return f"\n\t{linea}\n\t  {titulo}  \n\t{linea}\n"

def solicitarDatosCliente() -> dict:
    """
    Función que solicita los datos del cliente y los devuelve en un diccionario
    Se definen en una lista las keys que se van a solicitar y se recorre para solicitar los datos
    
    Returns:
        dict: Diccionario con los datos del cliente
    """
    keys = ["nombre", "apellido", "comuna", "rut"]
    cliente = {}
    
    for k in keys:
        while True:
            ingreso = input(iconosInput(f"Ingrese {k} cliente: ", "+"))
            if len(ingreso.strip()) > 0:
                cliente[k] = ingreso.title()
                break
            else:
                print(iconosInput(f"ERROR: {k.capitalize()} no debe estar vacío", "!"))
            # END IF
        # END WHILE
    cliente["rut"] = cliente["rut"].upper()
    
    return cliente

def menuCilindros() -> list:
    """
    Función que recorre la lista 'cilindros' y solicita la cantidad de cilindros de cada tipo y devuelve una lista con las cantidades seleccionadas
    
    Returns:
        list: Lista con las cantidades seleccionadas de cilindros
    """
    cilindros = [5, 15, 45]
    seleccionCliente = []

    for c in cilindros:
        isRunning = True
        while isRunning:
            opcion = input(iconosInput(f"¿Cuántas unidades de cilindro de {c}kg?: ", "+"))
            if esNumero(opcion):
                opcion = int(opcion)
                if opcion < 0:
                    print(iconosInput("ERROR: Valor ingresado no debe ser negativo","!"))
                else:
                    seleccionCliente.append(opcion)
                    isRunning = False
                # END IF
            # END IF
        # END WHILE
    # END FOR
    
    # Si la suma de la lista es 0, se vuelve a llamar a la función
    if sum(seleccionCliente) <= 0:
        seleccionCliente = menuCilindros() # Recursividad
    
    return seleccionCliente

def esNumero(numero: str) -> bool:
    """
    Función que recibe un número y verifica si es numérico o no, retorna True si es numérico y False si no lo es, además imprime un mensaje de error
    
    Args:
        numero (str): Número a verificar
        
    Returns:
        bool: True si es numérico, False si no lo es
    """
    try:
        numero = int(numero)
        return True
    except Exception:
        print(iconosInput("Valor ingresado no es numérico", "!"))
        return False

def registrarPedido(pedidos: list) -> list:
    cliente = solicitarDatosCliente()
    pedidoCliente = menuCilindros()
    cliente["pedido"] = pedidoCliente
    
    # Se agrega el cliente a la lista de pedidos
    pedidos.append(cliente)
    return pedidos


def mostrarMenu(menu: str, pedidos: list):
    """
    Función que muestra el menu definido en una constante, recibe la opción del usuario y ejecuta la acción correspondiente
    
    Args:
        menu (str): Menú a mostrar
        pedidos (list): Lista de pedidos
    """
    while True:
        print(menu)
        opcion = input("[+] Ingrese una opción: ")
        if opcion == "1":
            print(crearTitulo("REGISTRAR PEDIDO"))
            pedidos = registrarPedido(pedidos)
            print(pedidos) # TODO: Borrar
        elif opcion == "2":
            print(crearTitulo("LISTAR PEDIDOS"))
        elif opcion == "3":
            print(crearTitulo("IMPRIMIR HOJA DE RUTA"))
        elif opcion == "4":
            print("\n[!] Saliendo...")
            break
        else:
            print("[!] Opción Ingresada no es válida")

def main(menu, pedidos):
    mostrarMenu(menu, pedidos)

### DECLARACIÓN DE VARIABLES ###
MENU = """\n1. Registrar Pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Salir del programa\n"""
pedidos = []

### MAIN ###
signal.signal(signal.SIGINT, handler)
if '__main__' == "__main__":
    main(MENU, pedidos)