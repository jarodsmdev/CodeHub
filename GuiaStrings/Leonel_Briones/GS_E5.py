"""
Ejercicio 5
Escriba un programa que encuentre la palabra de mayor longitud dentro de un texto cuyas palabras se separan por un único espacio y no hay espacio al final. Puede considerar que solo ingresan letras y espacios. Si hay dos o más palabras que tienen la mayor longitud, puede entregar cualquiera.

Ejemplo 1:
Ingrese frase: Necesito estudiar para la prueba dos
La palabra con mayor longitud es: estudiar

Ejemplo 2:
Ingrese frase: Chile
La palabra con mayor longitud es: Chile

"""
# Declaración de variables e inicialización
palabra = ""
longitudPalabraExtensa = 0

# Ingreso de una palabra
frase = input("[+] Ingrese frase: ").strip() # strip() elimina los espacios al inicio y al final

longitudPalabraExtensa = 0

# Validar si existe una frase
if len(frase) == 0:
    # Mostrar mensaje de error si no se ha ingresado una frase
    print("[!] No ha ingresado ninguna palabra")
else:
    # Recorrer cada caracter de la frase
    for i in range(len(frase)):
        # Validar si el caracter no es un espacio
        if frase[i] != " ":
            # Agregar el caracter a la palabra
            palabra += frase[i]
        else:
            # Al encontrarse un espacio, se considera que la palabra ha terminado
            # Validar si la palabra es más extensa que la anterior
            if len(palabra) > longitudPalabraExtensa:
                palabraExtensa = palabra
                longitudPalabraExtensa = len(palabra)
            palabra = ""

    # Considerar la última palabra si es la más extensa
    if len(palabra) > longitudPalabraExtensa:
        palabraExtensa = palabra
        longitudPalabraExtensa = len(palabra)

# Mostrar la palabra más larga
print("Palabra más extensa:", palabraExtensa)
