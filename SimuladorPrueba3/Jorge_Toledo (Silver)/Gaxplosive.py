### TOP ###
pedidos = []
sectores = ["Centro", "Colina", "Industrias"]

### DEFINICIONES ###
def MenuL():
    print("""
        1. Registrar pedido
        2. Listar los todos los pedidos
        3. Imprimir hoja de ruta
        4. Salir del programa
        """)
    return ""
def registrar_pedido():
    print("=== Registrar Pedido ===")
    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    comuna = input("Comuna: ")
    c5 = int(input("Cantidad de cilindros de 5kg: "))
    c15 = int(input("Cantidad de cilindros de 15kg: "))
    c45 = int(input("Cantidad de cilindros de 45kg: "))
    if nombre.strip() == "" or apellido.strip() == "" or comuna.strip() == "":
        print("Todos los datos deben ser validos")
        return
    pedidos.append({
        "Nombre": nombre,
        "Apellido": apellido,
        "Comuna": comuna,
        "Cilindro 5kg": c5,
        "Cilindro 15kg": c15,
        "Cilindro 45kg": c45
    })
    

def listar_pedidos():
    print("=== Listar Pedidos ===")
    if not pedidos:
        print("No hay pedidos registrados.")
    else:
        print("Nombre\t\tApellido\tComuna\t\tCilindro 5kg\tCilindro 15kg\tCilindro 45kg")
        for pedido in pedidos:
            print(f"{pedido['Nombre']}\t\t{pedido['Apellido']}\t\t{pedido['Comuna']}\t\t{pedido['Cilindro 5kg']}\t\t{pedido['Cilindro 15kg']}\t\t{pedido['Cilindro 45kg']}")
    input("Presiona Enter para continuar...")

def imprimir_hoja_de_ruta():
    print("=== Imprimir Hoja de Ruta ===")
    print("Sectores disponibles para la hoja de ruta:")
    for i, sector in enumerate(sectores, start=1):
        print(f"{i}. {sector}")
    
    opcion = int(input("Seleccione un sector para generar la hoja de ruta (1, 2 o 3): "))
    
    if opcion < 1 or opcion > 3:
        print("Opción inválida.")
        return
    
    sector_elegido = sectores[opcion - 1]
    
    # Generar archivo de texto con la hoja de ruta
    nombre_archivo = f"hoja_ruta_{sector_elegido.lower()}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Nombre\t\tApellido\t\tComuna\t\tCilindro 5kg\t\tCilindro 15kg\t\tCilindro 45kg\n")
        for pedido in pedidos:
            archivo.write(f"{pedido['Nombre']}\t\t{pedido['Apellido']}\t\t{pedido['Comuna']}\t\t{pedido['Cilindro 5kg']}\t\t{pedido['Cilindro 15kg']}\t\t{pedido['Cilindro 45kg']}\n")

    print(f"Hoja de ruta para el sector '{sector_elegido}' generada en '{nombre_archivo}'.")
    

### VARIABLES ###
Menu = True
Opcion = str(0)

### CODIGO ###

while Menu == True:
    if Opcion == "1":
        registrar_pedido()
        Opcion = "0"
    elif Opcion == "2":
        listar_pedidos()
        Opcion = "0"
    elif Opcion == "3":
        imprimir_hoja_de_ruta()
        Opcion = "0"
    elif Opcion == "4":
        Menu == False
    elif Opcion == "0": 
        print(MenuL())
        Opcion = input("Elige una opcion: ")
    else:
        print("Elige una opcion valida")
        Opcion = "0"
    