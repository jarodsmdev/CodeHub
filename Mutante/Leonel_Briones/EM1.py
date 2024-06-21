
import time, signal, sys

# Ctrl+C
def def_handler(sig: int, frame: object):
    print("\n[!] Saliendo...\n")
    sys.exit(1)
    
def imprimirPorcentaje(actual: int, total: int):
    porcentaje = round((actual / total) * 100, 1)
    print(f"{porcentaje}% completado")

def ordenarListaMenorAMayor(lista: list) -> list:
    print("[!] Comenzando a ordenar la lista... paciencia")
    elemento = -1 # IMC Representa el ultimo elemento de la lista
    start = time.time()
    time.sleep(1)

    for i in range(len(lista) - 1):
        imprimirPorcentaje(i, len(lista))
        for j in range(len(lista) - 1 - i):
            if lista[j][elemento] > lista[j][elemento]:
               aux = lista[j]
               lista[j] = lista[j + 1]
               lista[j + 1] = aux
    end = time.time()
    length = end - start
    print(f"[!] Ordenamiento finalizado.  Duración: {round(length)} segundos")
    return lista

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
    
    # Ordenar pacientes de menor a mayor
    filtroEstadoSalud = ordenarListaMenorAMayor(filtroEstadoSalud)
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
    
def main():
    start = time.time()
    NOMBRE_ARCHIVO = "datos.csv"
    ESTADO_SALUD = "Excellent"
    print("Cantidad de Pacientes:",promedioIMC_por_estado_de_salud(NOMBRE_ARCHIVO, ESTADO_SALUD))
    end = time.time()
    length = end - start
    print(f"[!] Programa finalizado en {round(length)} segundos")
    
### MAIN ###
signal.signal(signal.SIGINT, def_handler)
if __name__ == '__main__':
    main()
