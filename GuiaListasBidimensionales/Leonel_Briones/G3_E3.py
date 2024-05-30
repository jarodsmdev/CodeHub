"""
Haga un programa que permita ingresar 3 secuencias de números de distinto largo.
Cada vez que desee terminar una secuencia, debe ingresar la palabra “fin”. Cada secuencia debe ser almacenada en una lista y estas a su vez deben ser almacenadas en una lista, quedando así una lista bidimensional. Los números de las secuencias deben ser ordenadas de mayor a menor. Guíese del ejemplo:

Secuencia 1:
Ingrese número: 4
Ingrese número: 9
Ingrese numero: 2
Ingrese numero: 1
Ingrese numero: fin
Secuencia 2:
Ingrese número: -3
Ingrese numero: 0
Ingrese numero: 2
Ingrese numero: fin
Secuencia 3:
Ingrese número: 88
Ingrese numero: 12
Ingrese numero: fin
La lista bidimensional queda como: [[9,4,2,1], [2,0,-3], [88,12]]
"""

# Declaración de variables
CANTIDAD_SECUENCIAS = 3
listaNumeros = []

# Iterar para solicitar datos de las secuencias
for i in range(3):
    # Información de secuencia
    print(f"Secuencia {i + 1}:")
    ingresoNumeros = True
    numeros = []
    # Iterar para solicitar números
    while ingresoNumeros:
        esError = True
        # Bucle while para validar que se ingresen números
        while esError:
            # Solicitar número
            numero = input("[+] Ingrese número: ")
            # Validar para salir del bucle
            if numero == "fin":
                # Salir del bucle de secuencia
                ingresoNumeros = False
                # Salir del bucle de validación de números
                esError = False
            else:
                # Validar que sea un número
                try:
                    # Convertir a entero
                    numero = int(numero)
                    # Agregar número a la lista
                    numeros.append(numero)
                    # Salir del while en caso de ser todo válido
                    esError = False
                except:
                    # En caso de error, mostrar mensaje
                    print("[!] Sólo ingreso de valores numéricos")
        # Ordenar la lista de números de menor a mayor
        numeros.sort()
        # Invertir la lista de números para que quede de mayor a menor
        numeros.reverse()
    # Agregar la lista de números a la lista bidimensional
    listaNumeros.append(numeros)    
# Mostrar lista por pantalla          
print(f"La lista bidimensional queda como: {listaNumeros}")