"""
Ejercicio 4
Haga un programa que reciba palabras hasta que se ingresa un 0 (cero). Esas palabras deben ser almacenadas en una lista, pero solo las palabras que tengan 4 o más caracteres.

La lista debe ser mostrada por pantalla.
Ejemplo:
Ingrese palabra: saber
Ingrese palabra: programar
Ingrese palabra: es
Ingrese palabra: importante
Ingrese palabra: 0
La lista es: [“saber”, “programar”, “importante”]
"""
listaPalabras = []
isRunning = True
while isRunning:
    palabra = input("Ingrese una palabra cuya longitud sea mayor a 4 \n[+] Para finalizar ingrese el número cero: ")
    
    if palabra == "0":
        isRunning = False
    else:
        if len(palabra) >= 4:
            listaPalabras.append(palabra.lower())
        else:
            print("[!] ERROR: Palabra ingresada no cumple con el requerimiento mínimo.")
            
print(listaPalabras)