"""
Haga un programa que permita ingresar N nombres por teclado, donde N es un dato que también se ingresa por teclado.  Los nombres deben ser almacenados en una lista y ordenados alfabéticamente.  Luego, el programa debe mostrar la lista de nombres por pantalla y el último y penúltimo nombre de la lista.

Ejemplo:
Indique cuántos nombres va a ingresar: 4
Agregue un nombre: Marcela
Agregue un nombre: Pedro
Agregue un nombre: Juan
Agregue un nombre: Ana
La lista ordenada es: ["Ana", "Juan", "Marcela", "Pedro"]
El último nombre es: Pedro
El penúltimo nombre es: Marcela
"""

# Declaración de variables
lista = []
esError = True

# Validación de ingreso de números
while esError:
    try:
        cantNombres = int(input("[+] Indique cuántos nombres va a ingresar: "))
        esError = False
    except:
        print("[!] Ingrese valores numéricos.")

# Solicitar al usuario cantidad de nombres definida anteriormente
for i in range(cantNombres):
    nombre = input("[+] Agregue un nombre: ")
    lista.append(nombre)
    
# Ordenar la lista
lista.sort()

# Mostrar la lista ordenada alfabéticamente
print("La lista ordenada es:", lista)

# Mostrar el último nombre de la lista
if len(lista) >= 1:
    print("El último nombre es:", lista[-1])
    
# Mostrar el penúltimo nombre de la lista
if len(lista) >= 2:
    print("El penúltimo nombre es:", lista[-2])