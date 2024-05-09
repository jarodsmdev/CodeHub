"""
Descripción de la Actividad:

El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible.

Las opciones disponibles deben estar construidas de la siguiente forma:
1. Pago de Tarjeta de Crédito:
    ✔a. El usuario comienza con una deuda de $100.000
    ✔b. El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito
    ✔c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
    ✔d. Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
    ✔e. Al pagar el sistema debe descontar de la deuda total.
    ✔f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
2. Simulación de Compras:
    ✔a. El usuario puede simular realizar un número ilimitado de compras.
    ✔b. Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra.
    ✔c. Se verifica que el monto de la compra sea mayor o igual a cero.
    ✔d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
3. Salir:
    ✔a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
    
A considerar:
1. Manejo de Errores:
    ✔a. Se utilizan bloques try y except para manejar posibles errores al ingresar datos, validar valores no numéricos y errores inesperados.
2. Manejo de Errores Específico:
    ✔b. Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas
"""


# Declaración e inicialización de variables
saldoTarjetaCredito = -100000
opcion = 0

MENU_PRINCIPAL = """\n\t*** BANCO LOLAMENTO ***
    
    1. PAGO TARJETA DE CRÉDITO
    2. SIMULACIÓN DE COMPRAS
    3. SALIR
    """
    
MENU_PAGO_TARJETA = """\n*** BANCO LOLAMENTO ***
> MENU PAGO DE TARJETA DE CRÉDITO
    
    1. PAGAR TARJETA DE CRÉDITO
    2. VOLVER AL MENÚ PRINCIPAL
    """

MENU_COMPRAS = """\n*** BANCO LOLA MENTO ***
> MENU COMPRAS CON TARJETA DE CRÉDITO

    1. REALIZAR COMPRAS
    2. PAGAR CON LA TARJETA DE CRÉDITO
    3. VOLVER AL MENÚ PRINCIPAL
    """


# CICLO MENU PRINCIPAL
menuPrincipal = True
while (menuPrincipal):
    # Mostrar Menú Principal
    print(MENU_PRINCIPAL)
    
    # Controla ingreso de sólo caracteres numéricos
    try:
        opcion = int(input("[>] Ingrese una opción: "))
    except:
        print("\n[!] Error: Ingresa sólo valores Numéricos.")
        continue
    # Manejo de opciones
    if opcion == 1:
        # Pago de tarjeta
        while True:
            print(MENU_PAGO_TARJETA)
            # Controla ingreso de sólo caracteres numéricos
            try:
                opcion = int(input("[>] Ingrese una opción: "))
            except:
                print("[!] Error: Ingresa sólo valores Numéricos.")
                
            # Ejecuta opción seleccionada
            if opcion == 1:
                esNumerica = False
                while not esNumerica:
                    print("\n*** PAGO DE TARJETA DE CRÉDITO ***")
                    print(f"\n[!] Saldo Tarjeta de Crédito: ${saldoTarjetaCredito}")
                    
                    try:
                        pago = int(input("[>] Ingrese monto a Pagar: "))
                        saldoActual = saldoTarjetaCredito
                        if pago >= 0 and pago <= abs(saldoActual):
                            esNumerica = True
                        else:
                            if pago < 0:
                                print("\n[!] Error: Monto a pagar debe ser mayor o igual a cero")
                            else:
                                print("\n[!] Error: Monto a pagar no debe superar la deuda")
                    except ValueError:
                        print(f"\n[!] Error: '{pago}' No es un valor Numérico")
                        
                # Actualizar el monto
                saldoTarjetaCredito = saldoTarjetaCredito + pago
                
                # Mostrar comprobante de pago
                print("Imprimiendo comprobante...\n")
                print(f"""
                    *** COMPROBANTE DE PAGO ***
                    ---------------------------
                    \tSaldo Anterior: ${saldoActual}
                    \tMonto de pago: ${pago}
                    
                    \tNuevo Saldo: ${saldoTarjetaCredito}
                    ---------------------------
                    \tGRACIAS POR SU PAGO
                """)
            elif opcion == 2:
                print("[!] Volviendo al Menú Principal...")
                break
    elif opcion == 2:
        totalCompra = 0
        # Menu de compras
        while True:
            # Muestra el menú de compras
            print(MENU_COMPRAS)
            print(f"Total Compra: ${totalCompra}\n")
            
            # Valida que la opción ingresada sea numérica
            try:
                opcion = int(input("[>] Ingrese una opción: "))
            except:
                print("\n[!] Error: Ingresa sólo valores Numéricos.")
            
            # Verifica opción ingresada por el usuario
            if opcion == 1:
                # Ingresar a comprar
                esNumerica = False
                while not esNumerica:
                    try:
                        montoCompra = int(input("[>] Ingrese monto de la compra: "))
                        if montoCompra >= 0:
                            totalCompra += montoCompra
                            esNumerica = True
                        else:
                            print("\n[!] Error: La compra debe ser mayor o igual a cero")
                    except ValueError:
                        print("\n[!] Error: Ingrese valores Numéricos")
                        
                #
                print(f"Monto de la compra: ${totalCompra}")
            elif opcion == 2:
                # Pagar la totalidad de la compra
                print(f"""
*** SIMULADOR DE COMPRAS ***
----------------------------
[!] Saldo Actual TC :${saldoTarjetaCredito}""")
                # Calcular nuevo saldo de la tarjeta de crédito
                saldoTarjetaCredito -= totalCompra
                
                print(f"""
[!] Se han cargado ${totalCompra} a su Tarjeta de Crédito
[!] Nuevo Saldo Tarjeta de Crédito: ${saldoTarjetaCredito}
---------------------------------------------------------------
¡¡¡GRACIAS POR SU COMPRA!!!
""")
                # Reestablecer a cero la variable
                totalCompra = 0
            elif opcion == 3:
                # Volver al menú principal
                if totalCompra != 0:
                    print("\n[!] AVISO: Debe realizar el pago antes de salir")
                else:
                    print("[!] Volviendo al menú Principal...")
                    break
            else:
                print("\n[!] Error: Debe ingresar una opción disponible en el sistema")
        

    elif opcion == 3:
        print("[!] Gracias por usar Banco LolaMento\nSaliendo...")
        menuPrincipal = False
    else:
        print("\n[!] Error: Debe ingresar una opción disponible en el sistema")

