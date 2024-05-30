"""
Dada una lista bidimensional como:
[[“Juan”, “Veloz”, 32], [“Marcela”, “Nuñez”, 17], [“Pedro”, “Orellana”, 67], [“Ana”, “González”, 40], [ ”Leonora”, “Veneca”, 23]]
haga un programa que permita revisar los datos de todas las personas y entregue cuantas personas son mayores de edad (edad mayor a 17).
Su programa debe funcionar con cualquier lista bidimensional como la del ejemplo.

Existen 2 personas mayores de edad
"""

# Declaración de variables
contadorMayorEdad = 0

# Lista de personas
personas = [
    ["Juan", "Veloz", 32],
    ["Marcela", "Nuñez", 17],
    ["Pedro", "Orellana", 67],
    ["Ana", "González", 40],
    ["Leonora", "Veneca", 23]
]

# Iterar sobre las personas
for persona in personas:
    # Validar si la persona es mayor de edad
    if persona[2] > 17:
        contadorMayorEdad += 1
        
# Mostrar cantidad de personas mayores de edad
print(f"Existen {contadorMayorEdad} personas mayores de edad")
