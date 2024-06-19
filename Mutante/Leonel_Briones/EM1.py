# FALTA CONSIDERAR EL ORDENAMIENTO DE MENOR A MAYOR POR PROMEDIO IMC

def promedioIMC_por_estado_de_salud(nombre_archivo: str, estado_salud) -> int:
    pacientes = leerArchivoCSV(nombre_archivo)
    filtroEstadoSalud = []
    sumaIMC = 0.0
    # Filtrar pacientes por estado_salud (posicion 0)
    for p in pacientes:
        if p[0] == estado_salud:
            filtroEstadoSalud.append(p)
            sumaIMC += float(p[9])
    
    # Calcular Promedio IMC
    cantPacientes = len(filtroEstadoSalud)
    if cantPacientes == 0:
        promedio = 0
    else:
        promedio = round(sumaIMC / cantPacientes, 2)
    
    exportarPacientes(filtroEstadoSalud, estado_salud)
    return cantPacientes

def leerArchivoCSV(archivo: str) -> int:
    pacientes = []
    with open(archivo, "r") as file:
        for linea in file:
            paciente = linea.strip().split(";")
            pacientes.append(paciente)
    return pacientes

def exportarPacientes(listaPacientes: list, nombreArchivo: str):
    file = open(nombreArchivo + ".txt", "w")
    for paciente in listaPacientes:
        file.write(f"{paciente[1]}: {paciente[9]}\n")
    file.close()
    
### MAIN ###
NOMBRE_ARCHIVO = "datos.csv"
ESTADO_SALUD = "Excellent"
print("Cantidad de Pacientes:",promedioIMC_por_estado_de_salud(NOMBRE_ARCHIVO, ESTADO_SALUD))
