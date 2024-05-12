"""
Ejercicio 2
Una cadena de ADN es válida si está compuesta únicamente por las bases Adenina (A),
Citosina (C), Guanina (G) o Timina (T). Escriba un programa para validar una cadena de ADN. Una cadena de ADN tiene solo 4 caracteres.

Ejemplo 1:
Ingrese cadena: ACGG
Cadena valida

Ejemplo 2:
Ingrese cadena: AXGG
Cadena invalida

Ejemplo 3:
Ingrese cadena: AGT
Cadena invalida
"""

# Inicializar Variable
esValida = True

# Ingresar Cadena
cadena = input("Ingrese Cadena: ").upper()

# Validar Cadena de ADN (4 Caracteres)
if len(cadena) != 4:
    print("Cadena Inválida")
else:
    # Recorrer Cadena
    for i in range(4):
        if cadena[i] not in "ACGT":
            esValida = False
            break

# Mostrar Resultado
if esValida:
    print("Cadena Válida")
else:
    print("Cadena Inválida")