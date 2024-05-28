"""
Haga un programa que cree la lista [3, 9, 12, 34, 90] y permita ingresar un valor por teclado.  Si el valor ingresado está en la lista, este debe ser eliminado y mostrar la lista, sino, debe mostrar un mensaje que el valor no existe en la lista.

Ejemplo 1:
Ingrese un número: 3
La lista es: [9, 12, 34, 90]

Ejemplo 2:
Ingrese un número: 5
El valor no existe
"""

lista = [3, 9, 12, 34, 90]

esError = True
isInList = False

while esError:
    try:
        numero = int(input("[+] Ingrese un número: "))
        esError = False
    except:
        print("[!] Debe ingresar sólo números")
        
# Recorrer la lista
for i in lista:
    
    # Verificar si el número está en la lista
    if i == numero:
        # Quitar el número de la lista
        lista.remove(i)
        isInList = True

# Mostrar la lista
if isInList:
    print("La lista es:", lista)
else:
    print("El valor no existe")
