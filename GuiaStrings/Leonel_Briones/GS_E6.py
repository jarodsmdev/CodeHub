"""
Ejercicio 6
Haga un programa que permita ingresar string que contiene un nombre y una nota separado por un dos puntos “:”. Debe permitir ingresar datos hasta que se ingrese la palabra “Terminar”. La palabra “Terminar” puede estar escrita con mayúscula o minúscula y debe funcionar de igual manera.

Luego, debe entregar la cantidad de estudiantes aprobados y reprobados.
Ejemplo 1:
Ingrese dato: Mauricio:4.3
Ingrese dato: Ana:6.7
Ingrese dato: Felipe:3.2
Ingrese dato: terminar
Hubo 2 estudiantes aprobados y 1 estudiantes reprobados.

Ejemplo 2:
Ingrese dato: Alejandra:5.7
Ingrese dato: Pedro:6.1
Ingrese dato: TERMINAR
Hubo 2 estudiantes aprobados y 0 estudiantes reprobados
"""

# Declaración de variables
nombre = None
nota = None
aprobados = 0
reprobados = 0
posicion = 0

ingresarDatos = True
while ingresarDatos:
    # Ingreso de la información
    data = input("[+] Ingrese nombre y la nota en este formato (Mauricio:4.3):  ")
    
    # Detectar la salida del bucle
    if data.lower() == "terminar":
        ingresarDatos = False
        print(f"Hubo {aprobados} estudiantes aprobados y {reprobados} estudiantes reprobados")
    else:
        # Saber en qué índice está el caractér dos puntos
        indice = 0
        for i in range(len(data)):
            if ":" == data[i]:
                posicion = i

        if posicion > 0:       
            # Obtener nombre
            nombre = data[0:posicion]
            # Obtener nota
            nota = float(data[posicion+1:len(data)])

            # Validar si la nota es mayor o igual a 4
            if nota >= 4:
                aprobados += 1
            elif nota < 4:
                reprobados += 1
