# Descripción: Simulador de viajes

# Declaramos las variables e inicializamos las variables en None
MADRID = None
PARIS = None
LONDRES = None
ROMA = None

# Variables para guardar los costos
costoVuelo = 0
costoAlojamiento = 0
costoTours = 0

# 
destinosRecorrer = ""
cantidadDestinos = 0

# FUNCIONAMIENTO DEL PROGRAMA

# Ingreso y validación de la cantidad de destinos
esError = True
while esError:
    # Ingreso de la cantidad de destinos
    print("\n*** SELECTOR DE DESTINOS ***\n")
    print("[!] Puede seleccionar hasta 4 destinos para su viaje.")
    cantidadDestinos = input("[+] Ingrese la cantidad de destinos: ")
    try:
        cantidadDestinos = int(cantidadDestinos)
        if cantidadDestinos > 4 or cantidadDestinos < 1:
            print("[!] ERROR: Debe ingresar un número entre 1 y 4.")
        else:
            # Si la cantidad de destinos es correcta, se sale del bucle
            esError = False
    except ValueError:
        print("[!] ERROR: Debe ingresar un número entero.")

# Ingreso y validación de la cantidad de viajeros

# Seleccion de destinos (Menú Estático solo se muestra 1 vez)
print("""\n*** SELECCIÓN DE DESTINOS ***\n
      1. Madrid
      2. París
      3. Londres
      4. Roma
      """)

# Setea los destinos para el menú
for i in range(cantidadDestinos):
 
    esError = True
    while esError:
        # Selección de destino disponible
        opcion = input(f"[+] Seleccione destino {i+1}: ")
        try:
            # Cambiamos el tipo de dato de la opción
            opcion = int(opcion)
            if opcion > 4 or opcion < 1:
                print("[!] ERROR: Debe ingresar un número entre 1 y 4.")
            else:
                if opcion == 1 and MADRID == None:
                    MADRID = True
                    destinosRecorrer += "Madrid, "
                elif opcion == 2 and PARIS == None:
                    PARIS = True
                    destinosRecorrer += "París, "
                elif opcion == 3 and LONDRES == None:
                    LONDRES = True
                    destinosRecorrer += "Londres, "
                elif opcion == 4 and ROMA == None:
                    destinosRecorrer += "Roma, "
                    ROMA = True
                else:
                    # Si la opción ya fue seleccionada, se muestra un mensaje de error
                    print("[!] ERROR: Destino ya seleccionado.")
                    continue
        except ValueError:
            print("[!] ERROR: Debe ingresar valores numéricos.")
        else:
            if opcion > 4 or opcion < 1:
                print("[!] ERROR: Debe ingresar un número entre 1 y 4.")
            else:
                # Creación de la lista de destinos disponibles (Menú Dinámico)
                destinos = "\n*** DESTINOS DISPONIBLES ***\n"
                
                if MADRID == None:
                    destinos = destinos + f"1. Madrid\n"
                if PARIS == None:
                    destinos = destinos + f"2. París\n"
                if LONDRES == None:
                    destinos = destinos + f"3. Londres\n"
                if ROMA == None:
                    destinos = destinos + f"4. Roma\n"
                # Si ya se seleccionaron los 4 destinos, se muestra un mensaje
                if i == 3:
                    destinos = "[!] Ha seleccionado los 4 destinos disponibles"
                # Muestra destinos disponibles
                print(destinos)
                # Si la opción es correcta, se sale del bucle
                esError = False
                            
# Elimina los últimos 2 caracteres de la cadena de destinos (LIMPIA)
destinosRecorrer = destinosRecorrer[:-2].strip()
print(destinosRecorrer)

#TODO: DEPENDIENDO DE CANDIDAD DE DESTINOS HACER UN FOR CON LOS INGRESOS DE DATOS
for i in range(1, cantidadDestinos):

    # Ingreso y validación de la cantidad de viajeros
    esError = True
    while esError:
        # Ingreso de la cantidad de viajeros
        cantViajeros = input("[+] Ingrese la cantidad de viajeros: ")
        try:
            # Cambiamos el tipo de dato de la cantidad de viajeros
            cantViajeros = int(cantViajeros)
            # TODO: CREAR UNA LISTA PARA GUARDAR LA CANTIDAD DE VIAJEROS
            # Si la cantidad de viajeros es correcta, se sale del bucle
            esError = False
        except ValueError:
            print("[!] ERROR: Ingrese sólo valores Numéricos")
    
    print(f"[!] Lugar de destino {i}") # MOSTRAR EL DESTINO 1 QUE ESTÁ EN LA VARIABLE
    # TODO: CREAR UNA LISTA PARA AGREGAR EL DESTINO AL OUTPUT

    # Ingreso y validación del valor del pasaje por persona
    esError = True
    while esError:
        # Ingresa el valor del pasaje por persona
        valorPasaje = input("[+] Ingrese el valor del pasaje por persona (USD): ")
        try:
            # Cambiamos el tipo de dato del valor del pasaje
            valorPasaje = float(valorPasaje)
            # TODO: CREAR LISTA PARA GUARDAR EL VALOR DEL PASAJE POR PERSONA
            # Si la cantidad de viajeros es correcta, se sale del bucle
            esError = False
        except ValueError:
            print("[!] ERROR: Ingrese sólo valores Numéricos")
            
    # Ingreso y validación de la cantidad de noches por destino
    esError = True
    while esError:
        # Ingresa el valor de las noches por destino
        cantNoches = input("[+] Ingrese la cantidad de noches por destino: ")
        try:
            # Cambiamos el tipo de dato de la cantidad de noches
            cantNoches = int(cantNoches)
            # TODO: CREAR UNA LISTA PARA GUARDAR LAS NOCHES POR DESTINO
            # Si la cantidad de viajeros es correcta, se sale del bucle
            esError = False
        except ValueError:
            print("[!] ERROR: Ingrese sólo valores Numéricos")
            
    # Ingreso y validación del valor por noche
    esError = True
    while esError:
        # Ingresa el valor por noche
        valorNoche = input("[+] Ingrese el valor por noche (USD): ")
        # Cambiamos el tipo de dato del valor por noche
        try:
            valorNoche = float(valorNoche)
            # TODO: CREAR UNA LISTA PARA GUARDAR EL VALOR POR NOCHE
            # Si la cantidad de viajeros es correcta, se sale del bucle
            esError = False
        except ValueError:
            print("[!] ERROR: Ingrese sólo valores Numéricos")
            
    # Ingreso y validación de la cantidad de tours
    esError = True
    while esError:
        # Ingresa la cantidad de tours
        cantTours = input("[+] Ingrese la cantidad de tours a realizar: ")
        # Cambiamos el tipo de dato de la cantidad de tours
        try:
            cantTours = int(cantTours)
            while cantTours > 0:
                valorTour = input(f"[+] Ingrese el valor por tour {cantTours} (USD): ")
                try:
                    valorTour = float(valorTour)
                    if valorTour < 0:
                        print("[!] ERROR: El valor del tour no puede ser negativo.")
                    else:
                        # Solo cuando se ingresa un valor correcto, se resta 1 a la cantidad de tours
                        cantTours = cantTours - 1
                        # TODO: CREAR UN ACUMULADOR PARA GUARDAR EL VALOR DE LOS TOURS
                        # Si la cantidad de viajeros es correcta, se sale del bucle
                        esError = False
                except ValueError:
                    print("[!] ERROR: Ingrese sólo valores Numéricos")
        except ValueError:
            print("[!] ERROR: Ingrese sólo valores Numéricos")
            
    # Cálculo de los costos
    output = f"""*************************************
    Los destinos que recorrerás son: {destinosRecorrer}
    El valor por conceptos de alojamiento es de: {costoAlojamiento} USD
    El valor por concepto de vuelos es de: {costoVuelo} USD
    El valor por concepto de tours es de: {costoTours} USD
    **************************************************
    """

    # Imprime en terminal resumen de costos totales
    print(output)