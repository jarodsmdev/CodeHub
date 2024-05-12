"""
Ejercicio 1
Escriba un programa que permita ingresar una palabra y entregue la cantidad de vocales, consonantes y caracteres especiales. Cualquier otro carácter que no sea vocal ni consonante se considera carácter especial.

    Ejemplo 1:
    Ingrese palabra: DuocUC
    La palabra tiene 3 vocales, 3 consonantes y 0 otro carácter.

    Ejemplo 2:
    Ingrese palabra: Saludos!!
    La palabra tiene 3 vocales, 4 consonantes y 2 otro carácter
"""
vocales = "aeiouáéíóú"
consonantes = "bcdfghjklmnñpqrstvwxyz"

cantVocales = 0
cantConsonantes = 0
cantOtrosCaracteres = 0

palabra = input("Ingrese palabra: ").lower()

for c in palabra:
    if c in vocales:
        cantVocales += 1
    
    if c in consonantes:
        cantConsonantes += 1
    
    if c not in vocales + consonantes:
        cantOtrosCaracteres += 1
        
print(f"La palabra tiene {cantVocales} vocales, {cantConsonantes} consonantes y {cantOtrosCaracteres} otro carácter")



