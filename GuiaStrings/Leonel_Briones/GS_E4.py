"""
Ejercicio 4
Escriba un programa que permita ingresar una frase y entregue el número de palabras que contiene la frase.

Ejemplo 1:
Ingrese frase: Fundamentos de programacion
La frase contiene 3 palabras

Ejemplo 2:
Ingrese frase: CITT
La frase contiene 1 palabra
"""
# Declaración de variables e inicialización
contador = 1

# Ingreso de una palabra
frase = input("[+] Ingrese frase: ").strip() # strip() elimina los espacios al inicio y al final

# Contar las palabras
for caracter in frase:
    if caracter == " ":
        contador += 1

# Mostrar la cantidad de palabras
if len(frase) == 0:
    print("[!] No ha ingresado ninguna frase")
else:
    print(f"[!] La frase contiene {contador} palabras")
