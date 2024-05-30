"""
Haga un programa que reciba datos de 3 personas ingresados por teclado. Los datos
deben ser: Nombre, apellido y edad.Los datos deben ser guardados en una lista bidimensional. Muestre el resultado por pantalla.
"""
# Declaración de variables
CANT_MAX_PERSONAS = 3
listaPersonas = []

# Iterar para solicitar datos de las personas
for i in range(3):
    # Solicitar datos de la persona
    print(f"[!] Persona {i + 1}/{CANT_MAX_PERSONAS}")
    nombre = input(f"[+] Ingrese nombre: ")
    apellido = input(f"[+] Ingrese apellido: ")
    
    # Validar edad ingresada sea un número positivo
    esError = True
    while esError:
        # Solicitar edad
        edad = input("[+] Ingrese edad: ")
        # Validar que sea un número
        try:
            # Convertir a entero
            edad = int(edad)
            # Validar que sea positivo
            if edad < 0:
                print("[!] ERROR: Ingrese valores positivos")
            else:
                # Salir del while en caso de ser todo válido
                esError = False
        except:
            # En caso de error, mostrar mensaje
            print("[!] ERROR: Ingrese valores numéricos.")

    # Crear lista de persona vacía
    persona = []
    # Agregar datos a la lista de persona
    persona.append(nombre)
    persona.append(apellido)
    persona.append(edad)
    
    # Agregar persona a la lista principal
    listaPersonas.append(persona)
    
# Mostrar lista de personas
print(f"Los datos de las personas son: {listaPersonas}")