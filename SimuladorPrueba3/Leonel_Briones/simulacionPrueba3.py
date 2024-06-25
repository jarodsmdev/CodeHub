

def mostrarMenu(menu: str):
    while True:
        print(menu)
        opcion = input("[+] Ingrese una opción: ")
        if opcion == "1":
            print("REGISTRAR PEDIDO")
        elif opcion == "2":
            print("LISTAR PEDIDOS")
        elif opcion == "3":
            print("IMPRIMIR HOJA DE RUTA")
        elif opcion == "4":
            print("\n[!] Saliendo...")
            break
        else:
            print("[!] Opción Ingresada no es válida")

def main(menu):
    mostrarMenu(menu)

### MAIN ###
MENU = """\n1. Registrar Pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Salir del programa\n"""
pedidos = []

### BLOQUE PRINCIPAL ###
if '__main__' == "__main__":
    main(MENU)