import signal
import csv
import fnUtiles as fn
import fnProcesos as fnP


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


def solicitarEdad() -> int:
    while True:
        edad = input("[+] Ingrese edad: ")
        if fn.esNumero(edad):
            edad = int(edad)
            if edad >= 0:
                break
            else:
                print("[!] ERROR: Edad debe ser mayor o igual a cero")
    return edad


def ingresarNIF() -> str:
    nif = input("[+] Ingrese NIF de ciudadano: ").upper()
    return nif

def guardarPersona(personas: list) -> list:

    nif = ingresarNIF()
    while not fnP.validarNIF(nif):
        nif = ingresarNIF()
        
    if fnP.existeNIF(personas, nif):
        print("[!] NIF ya se encuentra registrado")
        guardarPersona(personas) # RECURSIVIDAD
    else:
        nombreApellido = solicitarNombreApellido()
        while not fnP.validarNombreApellido(nombreApellido):
            nombreApellido = solicitarNombreApellido()
    
        edad = solicitarEdad()
        while not fnP.esMayorde15(edad):
            edad = solicitarEdad()
            
        persona = {
            'nif': nif,
            'nombre': nombreApellido[0].capitalize(),
            'apellido': nombreApellido[1].capitalize(),
            'edad': edad
        }
        personas.append(persona)
        return personas


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
        # Ordenamiento alfabético
        for p in list_personas:
            p.append(p[0])
            p.pop(0)
        
        # Ordenar alfabéticamente
        list_personas.sort()
        
        # Retornar al formato inicial, pero con los datos ordenados
        for p in list_personas:
            p.insert(0, p[-1])
            p.pop()

    with open(nombreArchivo, "w", newline="") as file:
        writer = csv.writer(file)
        for p in list_personas:
            writer.writerow(p)
        print("[!] Archivo generado con éxito")
    

def menu(menu: str):
    personas = []
    isRunning = True
    
    while isRunning:
        print(fn.crearTitulo("Registro de Ciudadanos"))
        print(menu)
        opcion = input("\n[+] Ingrese una opción: ")
        if fn.esNumero(opcion):
            opcion = int(opcion)

            if opcion == 1:
                print(fn.crearTitulo("Guardar Persona"))
                personas = guardarPersona(personas)
                #print(personas) # TODO BORRAR
            
            elif opcion == 2:
                print(fn.crearTitulo("Buscar"))
                nif = ingresarNIF()
                while not fnP.validarNIF(nif):
                    nif = ingresarNIF()
                # END WHILE
                if fnP.existeNIF(personas, nif):
                    mostrarPersonaNIF(personas, nif)
                else:
                    print("[!] ERROR: No existen datos")

            elif opcion == 3:
                print(fn.crearTitulo("Guardar Archivos"))
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

signal.signal(signal.SIGINT, fn.def_handler)
if __name__ == "__main__":
    main()