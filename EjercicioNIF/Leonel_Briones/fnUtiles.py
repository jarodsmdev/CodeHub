import sys

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)

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