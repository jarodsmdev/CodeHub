"""
al recibir un correo electronico debe validar lo siguiente:

1. El correo debe tener un solo @
2. Si tiene dominio ".cl"
3. Entregar nombre de usuario y dominio por separado

Ejemplo:
s.campos@profesor.duoc.cl
Nombre de usuario: s.campos
Dominio: duoc.cl
El correo tiene dominio .cl
"""

correoElectronico = input("[+] Ingrese su correo electrónico: ")

# Validar si el correo tiene un solo @
arroba = 0
posicion = 0
for i in range(len(correoElectronico)):
    if "@" == correoElectronico[i]:
        arroba += 1
        posicion = i
        break

if arroba == 1:
    print("[+] nombre de usuario: ", correoElectronico[0:posicion])
    print("[+] dominio: ", correoElectronico[posicion+1:len(correoElectronico)])
    if correoElectronico[len(correoElectronico)-1:].lower() == ".cl":
        print("[!] Cumple con la terminación .cl")
    else:
        print("[!] No cumple con la terminación .cl")
else:
    print("[!] ERROR: El correo no es válido")

