"""USO DE TRY, EXCEPT, ELSE , FINALLY """
esError = True
while esError:
    numero = input("Ingresa un numero: ")
    try:
        numero = int(numero)
        print("Gracias por ingresar el numero: ", numero)
        esError = False
    except:
        print("Animal ingresa solo numeros")
    else:
        print("Se ejecuta siempre y cuando no haya error")
    finally:
        print("Siempre se va a ejecutar")