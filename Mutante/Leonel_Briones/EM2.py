
def estado_de_salud(nombre_archivo: str):
    """
    Función que recibe un archivo CSV con información de pacientes y genera un archivo de texto por cada estado de salud, invoca a otras funciones para realizar el procesamiento de los datos.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV con la información de los pacientes
    """
    pacientes = leerArchivoCSV(nombre_archivo)
    diccPacientes = transformarEnDiccionario(pacientes)
    listaGruposEstadosSalud = agruparEstadosSalud(diccPacientes)
    exportarPacientesPorEstadoSalud(diccPacientes, listaGruposEstadosSalud)
    return len(listaGruposEstadosSalud)

def exportarPacientesPorEstadoSalud(pacientes: dict, estadosSalud: list):
    """
    Función que recibe un diccionario con los pacientes y una lista con los estados de salud, genera un archivo de texto por cada estado de salud con la cantidad de pacientes activos y sedentarios.
    """
    for estado in estadosSalud:
        # Trae una lista de pacientes solo con su condicion de salud sea igual al de la iteración
        pacientesPorEstadoSalud = filtrarPacientesPorEstadoSalud(pacientes, estado) # OK
        
        # Trae un diccionario con su clave Yes/No con el conteo de pacientes activos o sedentarios
        agrupacionporActividadFisica = contarPacientesEjercitados(pacientesPorEstadoSalud)
        
        # Escribir cada uno de los ficheros con sus pacientes
        fileName = "estado_de_salud_" + estado + ".txt"
        
        with open(fileName, "w") as file:
            cantActivos = agrupacionporActividadFisica["Yes"]
            cantSedentarios = agrupacionporActividadFisica["No"]
            texto = f"Exercise: {cantActivos}\nNo Exercise: {cantSedentarios}"
            file.write(texto)
    print("[!] Generación Correcta")

def contarPacientesEjercitados(pacientes: list) -> dict:
    """
    Función que recibe una lista de pacientes y retorna un diccionario con la cantidad de pacientes activos y sedentarios.
    
    Args:
        pacientes (list): Lista de pacientes con su estado de salud
        
    Returns:
        dict: Diccionario con la cantidad de pacientes activos
    """
    pacientesActSedentarios = {}
    
    for i in range(len(pacientes[0])):
        haceEjercicio = pacientes[0][i][2]
        #paciente = pacientes[0][i]
        if haceEjercicio in pacientesActSedentarios:
            pacientesActSedentarios[haceEjercicio] += 1
        else:
            pacientesActSedentarios[haceEjercicio] = 1
    
    return pacientesActSedentarios

def agruparEstadosSalud(pacientes: dict) -> list:
    """
    Función que recibe un diccionario con los pacientes y retorna una lista con los estados de salud.
    
    Args:
        pacientes (dict): Diccionario con los pacientes
        
    Returns:
        list: Lista con los estados de salud
    """
    lista = []
    for k in pacientes:
        lista.append(k)
    return lista
        
def filtrarPacientesPorEstadoSalud(dicc: dict, estadoSalud: str) -> list:
    """
    Función que recibe un diccionario con los pacientes y un estado de salud, retorna una lista con los pacientes que tengan el estado de salud igual al recibido.
    
    Args:
        dicc (dict): Diccionario con los pacientes
        estadoSalud (str): Estado de salud a filtrar
    
    Returns:
        list: Lista con los pacientes que tengan el estado de salud igual al recibido
    """
    listaCondicionSalud = []
    for k in dicc:
        if k == estadoSalud:
            listaCondicionSalud.append(dicc[k])
    return listaCondicionSalud

def transformarEnDiccionario(lista: list) -> dict:
    """
    Función que recibe una lista con los pacientes y retorna un diccionario con los pacientes agrupados por estado de salud.
    
    Args:
        lista (list): Lista con los pacientes
    
    Returns:
        dict: Diccionario con los pacientes agrupados por estado de salud
    """
    pacientes = {}
    for p in lista:
        estadoSalud = p[0]
        if estadoSalud in pacientes:
            pacientes[estadoSalud].append(p)
        else:
            pacientes[estadoSalud] = [p]

    return pacientes

def leerArchivoCSV(nombreArchivo: str) -> list:
    """
    Función que recibe el nombre de un archivo CSV y retorna una lista con los pacientes.
    
    Args:
        nombreArchivo (str): Nombre del archivo CSV con los pacientes

    Returns:
        list: Lista con los pacientes
    """
    pacientes = []
    with open(nombreArchivo, "r") as file:
        for fila in file:
            pacientes.append(fila.strip().split(";"))
    return pacientes

def main():
    """
    Función principal que invoca a la función estado_de_salud.
    """
    print("[+] Inicio de la aplicación")
    cantidadArchivos = estado_de_salud("datos.csv")
    print(f"Cantidad de archivos Generados: {cantidadArchivos}")

### MAIN ###
if __name__ == "__main__":
    main()