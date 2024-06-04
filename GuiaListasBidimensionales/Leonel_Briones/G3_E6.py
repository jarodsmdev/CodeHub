"""
Ejercicio 6

Haga un programa que dada una lista bidimensional como:

[[“Marcela”, “Nuñez”, 17, “F”], [ ”Leonora”, “Veneca”, 23, “F”], [“Juan”, “Veloz”, 32, “M”], [“Ana”, “González”, 40, “F”], [“Pedro”, “Orellana”, 67, “M”]]

permita eliminar los datos de una persona en particular. El programa debe permitir ingresar un nombre y apellido por teclado, y si esa persona existe en la lista, sus datos deben ser eliminados de la lista y debe mostrar como queda la lista. Si no existe esa persona, el programa debe mostrar un mensaje diciendo: “esa persona no existe”.

Ejemplo 1:
Ingrese nombre: Juan
Ingrese apellido: Veloz
Persona eliminada
La lista queda asi: [[“Marcela”, “Nuñez”, 17, “F”], [ ”Leonora”, “Veneca”, 23, “F”], [“Ana”, “González”, 40, “F”], [“Pedro”, “Orellana”, 67, “M”]]

Ejemplo 2:
Ingrese nombre: Juan
Ingrese apellido: Veneca
Esa persona no existe
"""

# Declarar variables
existePersona = False

lista = [["Marcela", "Nuñez", 17, "F"],
         ["Leonora", "Veneca", 23, "F"],
         ["Ana", "González", 40, "F"],
         ["Pedro", "Orellana", 67, "M"]]

# Solicitar nombre y apellido de la persona a eliminar se convierte a minusculas
nombre = input("[+] Ingrese nombre: ").lower()
apellido = input("[+] Ingrese apellido: ").lower()


# Comprobar si existe la persona en la lista
for persona in lista:
    # Si el nombre y apellido ingresado es igual al nombre y apellido de la persona en la lista
    if nombre == persona[0].lower() and apellido == persona[1].lower():
        # Eliminar la persona de la lista
        lista.remove(persona)
        # Cambiar el valor de la variable a True
        existePersona = True
        # Informa al usuario que la persona fue eliminada
        print("[!] Persona Eliminada")

# En base a la variable existePersona mostrar mensaje
if not existePersona:
    print("[!] Esa persona no existe")
else:
    print(f"La lista queda así: {lista}")