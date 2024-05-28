""" Cree una lista vacía, luego reciba 3 valores numéricos ingresado por teclado y guardelos según fueron dados.  Muestre el resultado por pantalla

Ejemplo:
Ingrese un número: 3
Ingrese un número: -1
Ingrese un número: 88
La lista con los números es: [3, -1, 88]
"""

# Definir cantidad de ingresos
CANT_INGRESOS = 3

# Crear lista vacía
lista = []

# Recorrer la cantidad de ingresos
for i in range(CANT_INGRESOS):
    try:
        captura = int(input("Ingrese un número: "))
    except:
        pass
    # Agregar a la lista
    lista.append(captura)

# Mostrar lista
print(lista)