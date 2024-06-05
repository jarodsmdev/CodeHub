"""
Escriba 4 funciones que simule una calculadora básica, esta puede realizar operaciones de suma, resta, multiplicación y división. Cada operación debe estar encapsulada en una función que recibe 2 argumentos. Las funciones deben llamarse: resta(a,b), suma(a, b), multiplicacion(a,b) y division(a,b).

Al llamar las funciones con 2 argumentos, debe entregar el resultado de la operación.
Ejemplo:
>> print(suma(2,3))
>> 5
"""

def resta(a, b):
    return a - b

def suma(a, b):
    return a + b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("[!] ERROR: No es posible dividir por cero")
    else:
        return a / b

print(suma(2,3))
print(resta(2,3))
print(multiplicacion(2,3))
print(division(2,3))