# Descripción: Simulador de viajes

# Declaramos las variables e inicializamos las variables en None
MADRID = None
PARIS = None
LONDRES = None
ROMA = None


""" cantidadViajeros = input("[+] Ingrese la cantidad de viajeros: ")
valorPasajePersona = input("[+] Ingrese el valor del pasaje por persona (USD): ")
cantidadNochesPorDestino = input("[+] Ingrese la cantidad de noches por destino: ")
valorNoche = input("[+] Ingrese el valor por noche (USD): ")
cantidadTour = input("[+] Ingrese la cantidad de tours a realizar: ")
valorTour = input(f"[+] Ingrese el valor por tour (USD): ") """

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
                elif opcion == 2 and PARIS == None:
                    PARIS = True
                elif opcion == 3 and LONDRES == None:
                    LONDRES = True
                elif opcion == 4 and ROMA == None:
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
                    destinos = "[!] No hay destinos disponibles."
                # Muestra destinos disponibles
                print(destinos)
                # Si la opción es correcta, se sale del bucle
                esError = False

# Ingreso y validación de la cantidad de viajeros
cantViajeros = input("[+] Ingrese la cantidad de viajeros: ")