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

def esMayorde15(edad: int) -> bool:
    if edad >= 15:
        return True
    else:
        print("[!] ERROR: Edad ingresada es menor a 15")
    return False

def validarNIF(nif: str) -> bool:
    numeros = "0123456789"
    abecedario = ""
    
    # CODIGO ASCII A-Z
    for c in range(65, 91):
        abecedario += chr(c)

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

def existeNIF(personas:list, nif: str) -> bool:
    for p in personas:
        if p['nif'] == nif:
            return True
        else:
            return False