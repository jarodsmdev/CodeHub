import csv

def crearTitulo(titulo: str) -> str:
    longitud = len(titulo)
    linea = "=" * (longitud + 4)  # Se suman 4 para los espacios antes y después del título
    return f"\t{linea}\n\t  {titulo}  \n\t{linea}"

def esNumero(numero: int | str) -> bool:
    try:
        if numero == "":
            print("[!] ERROR: Debe ingresar un valor")
        else:
            numero = int(numero)
            return True
    except Exception as e:
        print("[!] ERROR: Valor ingresado no es numérico")
        return False

def solicitarNombreApellido() -> list:
    nombre = []
    while True:
        nombreCompleto = input("[+] Ingrese su nombre y apellido: ")
        if " " in nombreCompleto:
            nombre = nombreCompleto.split(" ")
            break
        else:
            print("[!] ERROR: Debe ingresar nombre y apellido")
    return nombre

def validarNombreApellido(nombreCompleto: list) -> bool:
    MIN_CARACTERES = 8
    esValido = False
    
    nombre = nombreCompleto[0]
    apellido = nombreCompleto[1]
    if len(nombre) < MIN_CARACTERES:
        print(f"[!] ERROR: Nombre debe tener como mínimo {MIN_CARACTERES}, ha ingresado {len(nombre)}")
        return esValido
    
    if len(apellido) < MIN_CARACTERES:
        print(f"[!] ERROR: Apellido debe tener como mínimo {MIN_CARACTERES}, ha ingresado {len(apellido)}")
        return esValido
    
    esValido = True
    return esValido

def solicitarEdad() -> int:
    while True:
        edad = input("[+] Ingrese edad: ")
        if esNumero(edad):
            edad = int(edad)
            if edad >= 0:
                break
            else:
                print("[!] ERROR: Edad debe ser mayor o igual a cero")
    return edad

def esMayorde15(edad: int) -> bool:
    if edad >= 15:
        return True
    else:
        print("[!] ERROR: Edad ingresada es menor a 15")
    return False

def ingresarNIF() -> str:
    nif = input("[+] Ingrese NIF de ciudadano: ").upper()
    return nif

def validarNIF(nif: str) -> bool:
    numeros = "0123456789"
    abecedario = ""
    
    # CODIGO ASCII A-Z
    for c in range(65, 91):
        abecedario += chr(c)

    esValido = False
    if len(nif) != 12:
        print("[!] ERROR: NIF debe contener 12 caracteres")
    else:

        for n in nif[:8]:
            if n not in numeros:
                print("[!] ERROR: NIF debe contener valores numéricos en los primeros 8 caracteres")
                return esValido
        if nif[8] != "-":
            print("[!] ERROR: Formato de NIF ingresado es incorrecto")
            return esValido

        for c in nif[-3:]:
            if c not in numeros + abecedario:
                print("[!] ERROR: Últimos 3 caracteres deben ser números o letras")
                return esValido
        
        esValido = True
    return esValido

def guardarPersona(personas: list) -> list:

    nif = ingresarNIF()
    while not validarNIF(nif):
        nif = ingresarNIF()
        
    if existeNIF(personas, nif):
        print("[!] NIF ya se encuentra registrado")
        guardarPersona(personas) # RECURSIVIDAD
    else:
        nombreApellido = solicitarNombreApellido()
        while not validarNombreApellido(nombreApellido):
            nombreApellido = solicitarNombreApellido()
    
        edad = solicitarEdad()
        while not esMayorde15(edad):
            edad = solicitarEdad()
            
        persona = {
            'nif': nif,
            'nombre': nombreApellido[0].capitalize(),
            'apellido': nombreApellido[1].capitalize(),
            'edad': edad
        }
        personas.append(persona)
        return personas

def existeNIF(personas:list, nif: str) -> bool:
    for p in personas:
        if p['nif'] == nif:
            return True
        else:
            return False

def mostrarPersonaNIF(personas:list, nif: str):
    if len(personas) > 0:
        persona = {}
        for p in personas:
            if p['nif'] == nif:
                persona = p
                break
        # END FOR
        print()
        for k, v in persona.items():
            print(f"{k.title()}: {v}")

def exportarDatos(personas: list):
    list_personas = []
    
    print("[!] Ingrese rango de Edad para el filtro: ")
    edadMin = solicitarEdad()
    edadMax = solicitarEdad()
    nombreArchivo = f"edades_entre_{edadMin}_y_{edadMax}.csv"
    
    # Realizo el filtro por edad
    for p in personas:
        if p['edad'] >= edadMin and p['edad'] <= edadMax:
            list_personas.append(list(p.values()))
            
    if len(list_personas) > 0:
        # Ordenamiento menor a mayor
        for p in list_personas:
            p.reverse() # Invierto los elementos para que edad esté al inicio
            
        list_personas.sort() # Ordeno la lista de menor a mayor edad
        
        for p in list_personas:
            p.reverse() # Vuelvo a invertir para que edad vuelva a final pero ya está ordenada

        print(list_personas)
        
    with open(nombreArchivo, "w", newline="") as file:
        writer = csv.writer(file)
        for p in list_personas:
            writer.writerow(p)
        print("[!] Archivo generado con éxito")
    

def menu(menu: str):
    personas = []
    isRunning = True
    
    while isRunning:
        print(crearTitulo("Registro de Ciudadanos"))
        print(menu)
        opcion = input("\n[+] Ingrese una opción: ")
        if esNumero(opcion):
            opcion = int(opcion)

            if opcion == 1:
                print(crearTitulo("Guardar Persona"))
                personas = guardarPersona(personas)
                print(personas) # TODO BORRAR
            
            elif opcion == 2:
                print(crearTitulo("Buscar"))
                nif = ingresarNIF()
                while not validarNIF(nif):
                    nif = ingresarNIF()
                # END WHILE
                if existeNIF(personas, nif):
                    mostrarPersonaNIF(personas, nif)
                else:
                    print("[!] ERROR: No existen datos")

            elif opcion == 3:
                print(crearTitulo("Guardar Archivos"))
                exportarDatos(personas)
            elif opcion == 4:
                isRunning = False
                salir()
            else:    
                print("[!] ERROR: Opción ingresada no es válida\n")
            
def salir():
    print("\n[!] Saliendo...\n[i] versión 1.1 Leonel Briones Palacios 2024")

def main():
    MENU = "1. Grabar\n2. Buscar\n3. Guardar archivos\n4. Salir"
    menu(MENU)
    return

if __name__ == "__main__":
    main()