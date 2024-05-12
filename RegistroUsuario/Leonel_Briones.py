"""
Descripción de la Actividad:
los estudiantes deberán formar grupos de trabajos de un mínimo de 2 alumnos y un máximo de 3 alumnos.

ETAPAS:

Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
    1) iniciar sesión
    2) registrar usuario
    3) salir
    
Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña, ambas con valor inicial vacío, ejemplo:
    usuario1= None
    usuario2= None
    usuario3= None
    contrasena1= None
    contrasena2= None
    contrasena3= None

Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente menú:
    1) Realizar llamada 
    2) Enviar correo electrónico 
    3) Cerrar sesión 

Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su tamaño es de 9 dígitos (ejemplo: 985447561).

La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.

También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”

Finalmente cerrar sesión, volverá al menú principal.

El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre esto, entonces el sistema emite un error y vuelve a solicitar la opción.

Recuerde utilizar try Exception en caso de ser necesario.
"""

# Happy Coding!

# Importar librería time
import time as timer

# Declaración e Inicialización de variables
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

# Menús
MENU_INICIO_SESION = """
*** BIENVENIDO AL SISTEMA ***
\t1) Iniciar Sesión
\t2) Registrar Usuario
\t3) Salir
"""

# Menú Principal
MENU_PRINCIPAL = """
*** MENÚ PRINCIPAL ***
\t1) Realizar llamada
\t2) Enviar correo electrónico
\t3) Cerrar Sesión
"""

# Mostrar menú principal
enEjecucion = True
while enEjecucion:
    print(MENU_INICIO_SESION)
    opcion = input("[+] Ingrese una opción: ") # Solicitar opción al usuario
    
    # Validar si el valor ingresado es un número
    try:
        opcion = int(opcion)
        # Ejecutar según la opción seleccionada
        if opcion == 1:
            # Validar si hay usuarios registrados
            if usuario1 == None and usuario2 == None and usuario3 == None:
                print("[!] ERROR: No hay usuarios registrados") # Mostrar mensaje de error
            # Mostrar inicio de sesión
            else:
                ingresoUsuario = input("[+] Ingrese su usuario: ").lower() # Solicitar usuario
                ingresoContrasena = input("[+] Ingrese su contraseña: ") # Solicitar contraseña
                
                # Validar si el usuario y contraseña son correctos
                if (ingresoUsuario == usuario1 and ingresoContrasena == contrasena1) or (ingresoUsuario == usuario2 and ingresoContrasena == contrasena2) or (ingresoUsuario == usuario3 and ingresoContrasena == contrasena3):
                    
                    # Mostrar menú principal
                    while True:
                        print(MENU_PRINCIPAL)
                        opcion = input("[+] Ingrese una opción: ") # Solicitar opción al usuario
                        try:
                            opcion = int(opcion)
                            if opcion == 1:
                                # Ingresar número de teléfono debe tener 9 dígitos y comenzar con 9
                                numeroTelefono = input("[+] Ingrese su número de teléfono: ")
                                
                                # Validar si el número de teléfono es válido
                                if len(numeroTelefono) != 9 or numeroTelefono[0] != "9":
                                    print("[!] ERROR: Número de teléfono inválido\n[!] AVISO: Debe tener 9 dígitos y comenzar con 9")
                                else:
                                    # Realizar llamada cuando el número de teléfono es válido
                                    print("[!] Realizando llamada espere por favor...")
                                    timer.sleep(2)
                                    print(f"[!] Llamada en curso... {numeroTelefono}")
                                    
                                    # Calcula el tiempo de inicio
                                    start = timer.time()
                                    input("[+] Presione Enter para finalizar la llamada...")
                                    
                                    # Calcula el tiempo de finalización
                                    end = timer.time()
                                    length = end - start
                                    
                                    # Muestra el tiempo de la llamada y un mensaje
                                    print(f"[!] ¡Llamada finalizada! Duración: {round(length)} segundos")
                            elif opcion == 2:
                                
                                # Solicitar correo electrónico
                                correo = input("[+] Ingrese su correo electrónico: ")
                                
                                # Validar correo electrónico (con bucle while o for)
                                cantidadArroba = 0
                                for i in range(len(correo)):
                                    if correo[i] == "@":
                                        cantidadArroba += 1
                                
                                if cantidadArroba != 1:
                                    print("[!] Correo electrónico Inválido, debe contener 1 simbolo \"@\"")
                                else:
                                    # Si es correcto solicitar un mensaje
                                    mensaje = input("[+] Ingrese mensaje a enviar: ")
                                    
                                    # Visualizar mensaje y correo
                                    print("\n" + "-"*30 + " MENSAJE " + "-"*30 + "\n|")
                                    print(f"|\tCorreo: {correo}")
                                    print(f"|\tMensaje: {mensaje}")
                                    print("|\n" + "-"*70 + "\n")
                                    
                                    # preguntar si desea enviar el mensaje
                                    respuesta = input("[+] ¿Desea enviar el mensaje? (s/n): ")
                                    if respuesta.lower() == "s":
                                        print("[!] Enviando mensaje... Espere por favor...")
                                        timer.sleep(2)
                                        print("[!] ¡Mensaje enviado correctamente!")
                                    else:
                                        print("[!] ¡Mensaje no enviado!")
                                    
                            elif opcion == 3:
                                print("[!] Cerrando Sesión...")
                                break
                            else:
                                print("[!] ERROR: Seleccione una opción disponible")
                        except ValueError:
                            print("[!] ERROR: Ingresar sólo valores Numéricos")
        elif opcion == 2:
            # Registrar Usuarios
            for i in range(3):
                # respuesta = ""
                usuario = input(f"[+] Ingrese nombre de usuario {i+1}: ").lower()
                contrasena = input(f"[+] Ingrese la contraseña para el usuario {usuario}: ")
                repitaContrasena = input(f"[+] Repita la contraseña para el usuario {usuario}: ")
                
                # Validar si la contraseña y la repetición de la contraseña son iguales
                while contrasena != repitaContrasena:
                    # usuario = input(f"[+] Ingrese el usuario {i+1}: ").lower()
                    print(f"[!] ERROR: Las contraseñas para el usuario {usuario} no coinciden")
                    contrasena = input(f"[+] Ingrese la contraseña para el usuario {usuario}: ")
                    repitaContrasena = input(f"[+] Repita la contraseña para el usuario {usuario}: ")
                # Fin bloque while
                
                # Asignar usuario y contraseña según el índice
                if i == 0:
                    usuario1 = usuario
                    contrasena1 = contrasena
                    print(f"[!] ¡Usuario {usuario} Registrado Correctamente!")
                    
                    # Preguntar si desea continuar
                    respuesta = input("[+] ¿Desea continuar? (s/n): ")
                    if respuesta.lower() == "n":
                        print("[!] Volviendo al menú principal...")
                        timer.sleep(1)
                        break
                elif i == 1:
                    usuario2 = usuario
                    contrasena2 = contrasena
                    print(f"[!] ¡Usuario {usuario} Registrado Correctamente!")
                    
                    # Preguntar si desea continuar
                    respuesta = input("[+] ¿Desea continuar? (s/n): ")
                    if respuesta.lower() == "n":
                        print("[!] Volviendo al menú principal...")
                        timer.sleep(1)
                        break
                elif i == 2:
                    usuario3 = usuario
                    contrasena3 = contrasena
                    print(f"[!] ¡Usuario {usuario} Registrado Correctamente!")
                    
                    # Salir al menú principal
                    print("[!] Volviendo al menú principal...")
                    timer.sleep(1)
            
        elif opcion == 3:
            enEjecucion = False
            print("[!] Finalizando Programa...")
            timer.sleep(1)
        else:
            # En caso de que la opción no sea válida
            print("[!] ERROR: Seleccione una opción disponible")
    
    except ValueError:
        print("[!] ERROR: Ingresar sólo valores Numéricos")
