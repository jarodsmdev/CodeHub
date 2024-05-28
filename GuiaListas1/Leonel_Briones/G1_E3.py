"""
Haga un programa que ingrese números enteros hasta que se ingrese la palabra "FIN". El programa debe mostrar por pantalla los números guardados en una lista ordenados de menor a mayor y luego ordenados de mayor a menor.

Ejemplo:
Ingrese número: 4
Ingrese número: 9
Ingrese número: 2
Ingrese número: 1
Ingrese número: FIN
La lista ordenada de menor a mayor es: [1, 2, 4, 9]
La lista ordenada de mayor a menor es: [9, 4, 2, 1]
"""

finalizar = True
lista = []

while finalizar:
    numero = input("Ingrese número: ")
    
    if numero == "FIN":
        finalizar = False
    else:
        try:
            numero = int(numero)
            lista.append(numero)
        except:
            print("[!] Ingrese sólo valores numéricos.")
            
# Mostrar la lista ordenada de menor a mayor
lista.sort()
print("La lista ordenada de menor a mayor es:", lista)

# Mostrar la lista ordenada de mayor a menor
lista.reverse()
print("La lista ordenada de mayor a menor es:", lista)