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

def solicitarDatosCliente(sectores: list) -> dict:
    """
    Función que solicita los datos del cliente y los devuelve en un diccionario
    Se definen en una lista las keys que se van a solicitar y se recorre para solicitar los datos
    
    Returns:
        dict: Diccionario con los datos del cliente
    """
    keys = ["nombre", "apellido"]
    
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
        
    while True:
        #print("\n[+] Sectores Disponibles:", ", ".join(sectores))
        #ingreso = input(iconosInput(f"Ingrese sector cliente {cliente['nombre']}: ", "+")).title()
        ingreso = seleccionSector(sectores)
        if ingreso.title() in sectores:
            cliente["sector"] = ingreso.title()
            break
        else:
            print(iconosInput("ERROR: Sector ingresado no es válido", "!"))
        # END IF
    
    return cliente

def menuCilindros(cilindros: list) -> list:
    """
    Función que recorre la lista 'cilindros' y solicita la cantidad de cilindros de cada tipo y devuelve una lista con las cantidades seleccionadas
    
    Args:
        list: Lista con el peso de cada cilindro
    Returns:
        list: Lista con las cantidades seleccionadas de cilindros
    """
    
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
        print(iconosInput("ERROR: Debe seleccionar al menos un cilindro", "!"))
        seleccionCliente = menuCilindros(cilindros) # Recursividad
    
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
        print(iconosInput("Valor ingresado no es numérico\n", "!"))
        return False

def registrarPedido(pedidos: list, cilindros: list, sectores: list) -> list:
    """
    Función que solicita los datos del cliente y el pedido y lo agrega a la lista de pedidos
    
    Args:
        pedidos (list): Lista de pedidos
        cilindros (list): Lista de tipos de cilindros
        sectores (list): Lista de sectores diponibles para despacho
    Returns:
        list: Lista de pedidos con el nuevo pedido agregado
    """
    cliente = solicitarDatosCliente(sectores)
    pedidoCliente = menuCilindros(cilindros)
    cliente["pedido"] = pedidoCliente
    
    
    # Mostrar Resumen del pedido
    print(iconosInput("RESUMEN DE COMPRA\n", "!"))
    for k, v in cliente.items():
        
        cilindros_str = ", ".join([f"{c}kg" for c in cilindros])
        if k == "pedido":
            pedido_str = ", ".join([f"{cantidad}" for cantidad in v])
            print(f"{k.capitalize()} ({cilindros_str}): {pedido_str}")
        else:
            print(f"{k.capitalize()}: {v}")
    
    r = input(iconosInput("¿Confirma el pedido? ", "+")).lower()
    
    if r != "n":
        # Se agrega el cliente a la lista de pedidos
        pedidos.append(cliente)
        
        print(iconosInput("Pedido guardado correctamente", "!"))
        
        return pedidos
    else:
        return None

def listarPedidos(pedidos: list):
    # Lista de pedidos de ejemplo
    pedidos = [
        {'nombre': 'Juan', 'apellido': 'Pérez', 'sector': 'Colina', 'pedido': [1, 0, 1]},
        {'nombre': 'Marcelo', 'apellido': 'Rivadeneira', 'sector': 'Las Industrias', 'pedido': [10, 1, 0]}
    ]
    
    # Calcular anchos máximos de cada columna
    max_lens = {} # Diccionario utilizará para almacenar el ancho máximo de cada columna
    
    for p in pedidos: # Recorre cada diccionario en la lista
        for k, v in p.items():
            max_lens[k] = max(max_lens.get(k, len(k)), len(str(v)))
            # max() toma 2 valores y devuelve el mayor de ellos
            # .get() Retorna el valor de la clave en caso de no devuelve el segundo argumento (opcional)
            # max_lens => Por ejemplo {'nombre': 7, 'apellido': 11, 'sector': 14, 'pedido': 10}
    #print(max_lens) TODO: BORRAR

    # Línea separadora
    barraSeparadora = "-" * (sum(max_lens.values()) + 3 * len(pedidos[0].keys()) + 1)
    #print(max_lens.values(), sum(max_lens.values()))
    # Output Example: dict_values([7, 11, 14, 10] 42)

    print(barraSeparadora)
    
    # Imprimir encabezado de la tabla
    for k in pedidos[0].keys(): # Recorre el primer elemento del diccionario y lo devuelve como lista
        print(f"| {k.ljust(max_lens[k]).capitalize()} ", end="") # ljust(length, character="")
        # Asegura que la key tenga un ancho igual al valor correspondiente en max_lens[k], que es el ancho máximo calculado para esa columna.
    print("|")
    # Ejemplo => | Nombre  | Apellido    | Sector         | Pedido     |
    
    print(barraSeparadora)

    
    # Imprimir los datos de clientes en la tabla
    for p in pedidos:
        for k, v in p.items():
            print(f"| {str(v).ljust(max_lens[k])} ", end="")
        print("|")
    
    print(barraSeparadora)

def listarPedidosV2(pedidos: list, cilindrosKg: list):
    # Lista de pedidos de ejemplo
    """
    pedidos = [
        {'nombre': 'Juan', 'apellido': 'Pérez', 'sector': 'Colina', 'pedido': [1, 0, 1]},
        {'nombre': 'Marcelo', 'apellido': 'Rivadeneira', 'sector': 'Las Industrias', 'pedido': [10, 1, 0]},
        {'nombre': 'Sebastián', 'apellido': 'Galáz', 'sector': 'Centro', 'pedido': [4, 5, 1]}
    ]
    """
    
    if len(pedidos) > 0:
        # Calcular anchos máximos de cada columna
        max_lens = {}
        cilindros = []
        for c in cilindrosKg:
            descripcion = f"Cilindro {c}kg"
            cilindros.append(descripcion)
        
        for p in pedidos:
            for k, v in p.items():
                if k == 'pedido':
                    for i, cantidad in enumerate(v):
                        nombre_columna = cilindros[i]
                        max_lens[nombre_columna] = max(max_lens.get(nombre_columna, len(nombre_columna)), len(str(cantidad)))
                else:
                    max_lens[k] = max(max_lens.get(k, len(k)), len(str(v)))
                    
        # Línea separadora
        barraSeparadora = sum(max_lens.values()) + 3 * (len(pedidos[0].keys()) - 1 + len(cilindros)) + 1
        print("-" * barraSeparadora)
        
        # Imprimir encabezado de la tabla
        for k in pedidos[0].keys():
            if k != 'pedido':
                print(f"| {k.capitalize().ljust(max_lens[k])} ", end="")
        for c in cilindros:
            print(f"| {c.ljust(max_lens[c])} ", end="")
        print("|")
        
        # Línea separadora
        print("-" * barraSeparadora)
        
        # Imprimir los datos de clientes en la tabla
        for p in pedidos:
            for k, v in p.items():
                if k != 'pedido':
                    print(f"| {str(v).ljust(max_lens[k])} ", end="")
            for i, cantidad in enumerate(p['pedido']):
                nombre_columna = cilindros[i]
                print(f"| {str(cantidad).center(max_lens[nombre_columna])} ", end="")
            print("|")
            
        print("-" * barraSeparadora)
    else:
        print(iconosInput("No hay pedidos registrados.", "!"))
        
def seleccionSector(sectores: list) -> str:
    """
    Función que muestra los sectores disponibles y solicita al usuario que seleccione uno
    
    Args:
        sectores (list): Lista de sectores disponibles
        
    Returns:
        str: Sector seleccionado
    """
    despachos = iconosInput("Despachos disponibles: \n", "!")
    for i in range(len(sectores)):
        despachos += f"\t{i + 1}. {sectores[i]}\n"
    
    while True:
        print(despachos)
        opcion = input(iconosInput("Seleccione una opción: ", "+"))
        if esNumero(opcion):
            opcion = int(opcion)
            if opcion <= 0 or opcion > len(sectores):
                print(iconosInput("ERROR: Opción no válida\n", "!"))
            else:
                return sectores[opcion - 1]
            
def exportarHojaRuta(sector: str, pedidos: list, cilindros: list):
    """
    Función que exporta un archivo de texto con los pedidos del sector seleccionado
    
    Args:
        sector (str): Sector seleccionado
        pedidos (list): Lista de pedidos
        cilindros (list): Lista con el detalle de los cilindros
    """
    headerClaves = list(pedidos[0].keys())
    headerCilindros = []
    detallePedido = ""
    
    # Crear texto encabezado de cilindros en forma de lista
    for c in cilindros:
        headerCilindros.append(f"{c}Kg")
    
    despachos = []
    
    # Filtrar pedidos por sector
    for p in pedidos:
        if p["sector"] == sector:
            despachos.append(list(p.values()))
    
    # Crear encabezado
    salida = " ".join(headerClaves) + "\n"
    
    # Prepara la salida de los pedidos, de manera que sea comprendida por el usuario
    for i in range(len(despachos)):
        detallePedido = "Pedido: "
        for j in range(len(headerCilindros)):
            detallePedido += str(despachos[i][-1][j]) + " Und. de " + headerCilindros[j] + "  | "
        despachos[i][-1] = detallePedido

    # Crear texto de salida
    try:
        with open(sector + ".txt", "w") as file:
            file.write(salida)
            for fila in despachos:
                file.write(str(fila).replace("[", "").replace("'","").replace(",","").replace("]","") + "\n") # Se eliminan los caracteres innecesarios
        
        print(iconosInput("Archivo Generado con éxito", "!"))
    except Exception as e:
        print(iconosInput("Error al generar archivo", "!"))
        print(e)

def mostrarMenu(menu: str, pedidos: list, cilindros, sectores: list):
    """
    Función que muestra el menu definido en una constante, recibe la opción del usuario y ejecuta la acción correspondiente
    
    Args:
        menu (str): Menú a mostrar
        pedidos (list): Lista de pedidos
        cilindros (list): Lista con el detalle del peso de cada cilindro
        sectores (list): Lista con los sectores de despacho
    """
    while True:
        print(crearTitulo("GAXPLOSIVE"))
        print(menu)
        opcion = input("[+] Ingrese una opción: ")
        if opcion == "1":
            print(crearTitulo("REGISTRAR PEDIDO"))
            pedidoTemporal = registrarPedido(pedidos, cilindros, sectores) # Puede retornar None
            # Sólo en caso de que exista realmente un pedido se actualizará la variable pedidos
            if pedidoTemporal != None:
                pedidos = pedidoTemporal
        elif opcion == "2":
            print(crearTitulo("LISTAR PEDIDOS"))
            listarPedidosV2(pedidos, cilindros)
            input(iconosInput("Presione una tecla para continuar...", "+"))
        elif opcion == "3":
            print(crearTitulo("IMPRIMIR HOJA DE RUTA"))
            if len(pedidos) > 0:
                sector = seleccionSector(sectores)
                exportarHojaRuta(sector, pedidos, cilindros)
            else:
                print(iconosInput("No hay pedidos registrados.", "!"))
            input(iconosInput("Presione una tecla para continuar...", "+"))
        elif opcion == "4":
            print("\n[!] Saliendo...")
            break
        else:
            print("[!] Opción Ingresada no es válida")

def main(menu, pedidos, cilindros, sectores):
    mostrarMenu(menu, pedidos, cilindros, sectores)

### DECLARACIÓN DE VARIABLES ###
MENU = """\n1. Registrar Pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Salir del programa\n"""
pedidos = []
""" # DATOS DE PRUEBA
pedidos = [
        {'nombre': 'Juan', 'apellido': 'Pérez', 'sector': 'Las Industrias', 'pedido': [1, 0, 1]},
        {'nombre': 'Marcelo', 'apellido': 'Rivadeneira', 'sector': 'Centro', 'pedido': [10, 1, 0]},
        {'nombre': 'Sebastián', 'apellido': 'Galáz', 'sector': 'Colina', 'pedido': [4, 5, 1]}
    ]
"""
# CONFIGURACIÓN DE LA APLICACIÓN 
# PUEDE AGREGAR MÁS TIPOS DE CILINDROS O SECTORES COMO SE REQUERA
cilindros = [5, 15, 45] #<- 
sectores = ["Colina", "Las Industrias", "Centro"] #<-

### MAIN ###

signal.signal(signal.SIGINT, handler)
if '__main__' == "__main__":
    main(MENU, pedidos, cilindros, sectores)
