"""
Ejercicio 3
Escriba un programa que construya un string con las letras que coinciden en 2 String ingresados como entrada.  Por ejemplo: "amorosos" y "amortizar" coinciden en "amor"; por otra parte, "conformidad y "contorno" coinciden en "conor".  Observe que los Strings pueden tener distintos largos.

Ejemplo:
Ingrese string 1: amorosos
Ingrese string 2: amortiza
String coincidente: amor
"""

# Ingreso de 2 Strings
palabra1 = input("Ingrese String 1: ").lower()
palabra2 = input("Ingrese String 2: ").lower()

# Inicialización de variables
stringFinal = ""
i = 0

# Determinar largos de los String
if len(palabra1) <= len(palabra2):
    stringCorto1 = palabra1
    stringCorto2 = palabra2
else:
    stringCorto1 = palabra2
    stringCorto2 = palabra1

# Iterar posicion de cada caractér en ambas palabras  
for caracter in stringCorto1:
    
    if caracter == stringCorto2[i]:
        stringFinal += caracter
        
    i += 1

# Output
print("String coincidente", stringFinal)