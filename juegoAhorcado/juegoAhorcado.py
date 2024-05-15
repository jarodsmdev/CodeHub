intentos = int(input("[+] Ingrese cantidad de intentos: "))
# frase = input("[+] Ingrese la palabra: ")

frase = "sacoweso" # frase incila
# fraseFormateada = "h _  _ a" # mosstrarr al usuario
fraseInterna = "" # manejo interno

fraseFormateada = ""
# cambiar formato a la palabra
inicial = frase[0]
final = frase[-1]
centro = (len(frase)-2) * " _ "

# Completa la frase
fraseFormateada = inicial + centro + final

# Separa con un espacio la palabra que manejará el sistema
for i in range(len(frase)):
    fraseInterna = fraseInterna + frase[i] + " "
    
print("Frase Formateada", fraseFormateada)
print("Frase Interna",fraseInterna)

palabra = ""
for i in range(intentos):
    letra = input(f"[+] Ingresa una letra: ({i+1})")
    
    for i in range(len(fraseInterna)):
        
        if letra == fraseInterna[i]:
            palabra = palabra + letra
        else:
            palabra += fraseFormateada[i]
        
    fraseFormateada = palabra
        
    print(fraseFormateada.replace("_", ""))
    palabra = ""
        