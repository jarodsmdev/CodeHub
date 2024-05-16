correo = input("Ingrese su correo").lower()
# correo = "correo@duoc.cl"

posicionArroba = 0
cantidadArroba = 0
for i in range(len(correo)):
    if correo[i] == "@":
        posicionArroba = i
        cantidadArroba = cantidadArroba + 1

if cantidadArroba == 1:
    print("El correo es valido")
else:
    print("El correo no es valido")

puntoCl = correo[-3] + correo[-2] + correo[-1]

nombre = correo[0:posicionArroba]
dominio = correo[posicionArroba+1:]

print("Correo:", correo)
print("Nombre:", nombre)
print("Domino:", dominio)

if puntoCl == ".cl":
    print("El correo tiene dominio .cl")
