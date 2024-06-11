"""
Ejercicio 4
En la empresa SEGURITO venden tres tipos de póliza: A, B, C. Desarrolle un programa que permita recibir el sueldo y número de hijos (código main) y llame a una función calculo(sueldo, num_hijos) que recibe 2 argumentos asociados al sueldo y número de hijos y devuelva el tipo de póliza que le corresponde según los siguientes criterios:
• Póliza A: Si el sueldo es menor o igual a $250.000 y tiene a lo más un hijo.
• Póliza B: Si el sueldo es mayor a $250.000 y NO tiene hijos.
• Póliza C: Si el sueldo es mayor a $250.000 y tiene entre 1 y 5 hijos
• Póliza D: si no le corresponde ninguna de las pólizas anteriores.
Nota: Debe tener un código main, una función definida y desde el código main debe llamar a
la función solicitada
"""

def validarEsNumero(numero: str) -> str:
    esValido = False
    try:
        numero = int(numero)
        esValido = True
    except:
        print("[!] ERROR: Valor ingresado no es numérico")
    return esValido

def calculo(sueldo: int, num_hijos: int) -> str:
    sueldo = int(sueldo)
    num_hijos = int(num_hijos)
    
    if sueldo == 250000 and num_hijos <= 1:
        return "Póliza A"
    elif sueldo > 250000 and num_hijos == 0:
        return "Póliza B"
    elif sueldo > 250000 and (num_hijos >= 1 and num_hijos <= 5):
        return "Póliza C"
    else:
        return "No le corresponde ninguna Póliza"
    
    
### MAIN ###

sueldo = input("[+] Ingrese sueldo: ")
num_hijos = input("[+] Ingrese cantidad de hijos: ")

if validarEsNumero(sueldo) and validarEsNumero(num_hijos):
    print(calculo(sueldo, num_hijos))
