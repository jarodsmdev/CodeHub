"""
EJERCICIO 2 Conjunto números primos
ACLARACIÓN: todavía no existe un mecanismo eficiente para obtener todos los números primos, este ejemplo solo es aplicado a un nivel sencillo y básico, y sirve para efectos de explicar el concepto de colecciones.
Desarrollen un programa que genere un conjunto de números primos dentro de un rango específico. Utilicen un conjunto para almacenar los números primos y una función para verificar si un número es primo.
"""

rangoInferior = int(input("[+] Ingrese el rango inferior: "))
rangoSuperior = int(input("[+] Ingrese el rango superior: "))

numeros_primos = {num for num in range(rangoInferior, rangoSuperior) if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1))}

print("Conjunto de números primos:", numeros_primos)