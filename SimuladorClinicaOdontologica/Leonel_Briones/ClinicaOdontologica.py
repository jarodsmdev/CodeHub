import signal, sys

def handlerCtrlC(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit()
    
def crearTitulo(titulo: str) -> str:
    largo = len(titulo)
    linea = "=" * (largo + 4)
    return f"\t{linea}\n\t  {titulo}  \n\t{linea}"

def esNumero(numero: str | int) -> bool:
    try:
        numero = int(numero)
        return True
    except Exception as e:
        print("[!] ERROR: Valor ingresado no es numérico")
        return False
    
def ingresoNumeros(min: int, mensaje: str) -> int:
    while True:
        numero = input(f"[+] {mensaje}: ")
        if esNumero(numero):
            numero = int(numero)
            if numero < min:
                print(f"[!] ERROR: Número ingresado puede ser menor que {min}")
            else:
                return numero
    
def seleccionTratamiento(tratamientos: dict) -> list:
    cotizaciones = []
    
    # Mostrar menú con tratamientos
    listTratamientos = list(tratamientos.keys())
    
    while True:
        menu = "\nTratamientos: \n\n"
        for i in range(len(listTratamientos)):
            menu += f"{i + 1}. {str(listTratamientos[i]).title()}\n"
            
        print(menu,"\n0. Volver")
        opcion = ingresoNumeros(0, "Seleccione una opción ")
        
        if esNumero(opcion):
            opcion = int(opcion)
            if opcion > len(listTratamientos):
                print("[!] Opción ingresada no es válida")
            elif opcion == 0:
                break
            else:
                cotizacion = {}
                cotizacion["cantidad"] = ingresoNumeros(0, "Ingrese cantidad ")
                cotizacion["tratamiento"] = listTratamientos[opcion - 1]
                cotizacion["valor"] = tratamientos[listTratamientos[opcion - 1]]
                cotizacion["total"] = cotizacion["cantidad"] * cotizacion["valor"]
                cotizaciones.append(cotizacion)
    return cotizaciones
    # END WHILE

def seleccionTipoTrabajador(perfiles: dict) -> float:
    menu = "[+] Convenio DUOC UC: \n\n"
    
    lstPerfiles = list(perfiles.keys())
    
    for i in range(len(lstPerfiles)):
        menu += f"{i + 1}. {lstPerfiles[i].title()}\n"
    
    isRunning = True
    while isRunning:
        print(menu,"\n0. Volver")
        
        ingreso = input("[+] Seleccione un perfil de trabajador: ")

        if esNumero(ingreso):
            ingreso = int(ingreso)
            if ingreso == 0:
                descuento = 0
                isRunning = False
                return descuento
            elif ingreso < 0 or ingreso > len(lstPerfiles):
                print("[!] ERROR: Valor ingresado no es válido")
            else:
                descuento = perfiles[lstPerfiles[ingreso - 1]]
                isRunning = False
    return descuento

def menu():
    cotizaciones = []

    while True:
        print(crearTitulo("CLÍNICA DENTAL EL DIENTE DE ORO"))
        print("1. Cotización\n2. Renunciar\n3. Salir")
        
        ingreso = ingresoNumeros(0, "Ingrese una opción ")
        if esNumero(ingreso):
            ingreso = int(ingreso)
            if ingreso == 1:
                cotizacionesTemp = seleccionTratamiento(TRATAMIENTOS)
                if len(cotizacionesTemp) > 0:
                    cotizaciones = cotizacionesTemp
                if len(cotizaciones) > 0:
                    r = input("[+] ¿Tiene Descuento? s/n: ").lower()
                    
                    if r != "n":
                        descuento = seleccionTipoTrabajador(DESCUENTOS_PERFILES)
                    else:
                        descuento = 0
                    # END IF
                    
                    MAX_COL = 80
                    print("-" * MAX_COL)
                    print("COTIZACIÓN".center(MAX_COL))
                    print("-" * MAX_COL)
                    
                    subTotal = 0
                    for c in cotizaciones:
                        subTotal += c['total']
                        print(f"--> {c['cantidad']} {c['tratamiento'].title()} ${c['total']}")
                    
                    print("-" * MAX_COL)
                    
                    print(f"SubTotal ${str(subTotal)}".ljust(MAX_COL))
                    
                    valorDescuento = subTotal * descuento
                    print(f"Descuento {round(descuento * 100)}% ${round(valorDescuento)}".ljust(MAX_COL))
                    print("-" * MAX_COL)
                    print(f"Total ${round(subTotal -  descuento)}".ljust(MAX_COL))
                    print("-" * MAX_COL)
                    print(f"Son {CONVENIO_MESES} cuotas de: ${round((subTotal -  descuento)/CONVENIO_MESES)}".ljust(MAX_COL))
                    print("\nSonría Bonito!!!")
                    
            elif ingreso == 2:
                # Eliminar Cotización hecha previamente
                cotizaciones = []
                pass
            elif ingreso == 3:
                print("[!] Saliendo...")
                break

def main():
    menu()
    

### MAIN ###
signal.signal(signal.SIGINT, handlerCtrlC)
if __name__ == "__main__":
    CONVENIO_MESES = 12
    DESCUENTOS_PERFILES = {
        'trabajador auxiliar': 0.15,
        'trabajador administrativo': 0.1,
        'trabajador docente': 0.05
    }
    SERV_ADICIONALES = ["Limpieza y destartraje", "Aplicación de sellante", "Aplicación de flúor"]
    TRATAMIENTOS = {
            'tratamiento carilla porcelana': 250000,
            'tratamiento implantes dentales': 475000,
            'tratamiento ortodoncia brackets': 800000
        }
    
    main()