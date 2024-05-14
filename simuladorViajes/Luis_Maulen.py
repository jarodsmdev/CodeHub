print("********************************\nPLANIFICADOR DE VIAJES FALABELLA\n********************************")

lugares = ""

valortnoches = 0
valorTtours = 0
valorTvuelos = 0

cantidad_destinos = int(input("INGRESE CANTIDAD DE DESTINOS: "))
viajeros = int(input("CANTIDAD DE VIAJEROS: "))

for i in range(1,cantidad_destinos+1):
    lugar_destino = input(f"LUGAR DE DESTINO {i}: ")
    lugares += "'" + lugar_destino + "'" + ", "

    if lugar_destino.upper() == "MADRID":
        valorxpersonaM = 150
        M = valorxpersonaM * viajeros
        valorTvuelos += M
        print("VALOR PASAJE (por persona USD): ",valorxpersonaM)

    elif lugar_destino.upper() == "PARIS":
        valorxpersonaP = 350
        P = valorxpersonaP * viajeros
        valorTvuelos += P
        print("VALOR PASAJE (por persona USD): ",valorxpersonaP)

    elif lugar_destino.upper() == "LONDRES":
        valorxpersonaL = 200
        L = valorxpersonaL * viajeros
        valorTvuelos += L
        print("VALOR PASAJE (por persona USD): ",valorxpersonaL)

    elif lugar_destino.upper() == "ROMA":
        valorxpersonaR = 320
        R = valorxpersonaR * viajeros
        valorTvuelos += R
        print("VALOR PASAJE (por persona USD): ",valorxpersonaR)

    cantidadnoches = int(input("CANTIDAD DE NOCHES ALOJAMIENTO: "))
    valorxnoche = 80
    print("VALOR POR NOCHE USD:",valorxnoche)

    s = valorxnoche * cantidadnoches
    valortnoches = valortnoches + s

    cantidadTour = int(input("CANTIDAD DE TOUR A REALIZAR: "))
    for i in range (1,cantidadTour+1):
        valorxTour = 35
        print(f"VALOR DEL TOUR {i} A REALIZAR USD:",valorxTour)
        t = valorxTour * cantidadTour
        valorTtours += t

    print("***************************************************************")

print("Los destinos que recorreras en esta aventura son: ","["+lugares.upper() + "]")
print("El valor por conceptos de alojamiento es: $",valortnoches, "USD")
print("El valor por conceptos de vuelos es: $",valorTvuelos, "USD")
print("El valor por conceptos de tours es: $",valorTtours, "USD")
print("***************************************************************")