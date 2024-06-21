import time, signal, sys

# Ctrl+C
def def_handler(sig: int, frame: object):
    print("\n[!] Saliendo...\n")
    sys.exit(1)
    
def imprimirPorcentaje(actual: int, total: int):
    """
    Imprime el porcentaje de completado de un proceso
    
    Args:
        actual (int): Cantidad de elementos procesados
        total (int): Cantidad total de elementos a procesar
    """
    porcentaje = round((actual / total) * 100, 1)
    print(f"{porcentaje}% completado")
    

def ordenarLista(lista:list) -> list:
    """
    Implementación de ordenamiento de lista de listas
    
    Args:
        lista (list): Lista de listas a ordenar
    
    Returns:
        list: Lista de listas ordenada
    """
    for p in lista:
        p.reverse()

    lista.sort()
    
    for p in lista:
        p.reverse()
    return lista

""" def ordenarListaMenorAMayor(lista: list) -> list:
    print("[!] Comenzando a ordenar la lista... paciencia")
    elemento = -1 # IMC Representa el ultimo elemento de la lista
    start = time.time()
    #time.sleep(1)

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
    return lista """

def calcularPromedioIMC(pacientes: list) -> float:
    """
    Calcula el promedio de IMC de una lista de pacientes
    
    Args:
        pacientes (list): Lista de pacientes
    
    Returns:
        float: Promedio de IMC
    """
    sumaIMC = 0.0
    for paciente in pacientes:
        sumaIMC += float(paciente[9])
    promedio = sumaIMC / len(pacientes)
    return round(promedio, 2)

def promedioIMC_por_estado_de_salud(nombre_archivo: str, estado_salud) -> int:
    pacientes = leerArchivoCSV(nombre_archivo)
    filtroEstadoSalud = []

    # Filtrar pacientes por estado_salud (posicion 0)
    for i in range(len(pacientes)):
        if pacientes[i][0] == estado_salud:

            imc = float(pacientes[i][9])
            pacientes[i].pop()
            pacientes[i].append(imc)

            filtroEstadoSalud.append(pacientes[i])
    
    """ print("Primeros 10 sin Ordenar")
    for p in filtroEstadoSalud[0:10]:
        print(p)
    print("-"*10) """
    
    # Ordenar pacientes de menor a mayor IMC
    listaOrdenada = ordenarLista(filtroEstadoSalud)
    
    """ print("Primeros 10 Ordenados")
    for p in listaOrdenada[0:10]:
        print(p) """
    promedio = calcularPromedioIMC(listaOrdenada)
    
    # Exportar pacientes a archivo de texto
    exportarPacientes(listaOrdenada, estado_salud, promedio)
    return len(listaOrdenada)

def leerArchivoCSV(archivo: str) -> list:
    pacientes = []
    with open(archivo, "r") as file:
        for linea in file:
            paciente = linea.strip().split(";")
            pacientes.append(paciente)
    return pacientes

def exportarPacientes(listaPacientes: list, nombreArchivo: str, promedio: float):
    file = open(nombreArchivo + "-IMC.txt", "w")
    for paciente in listaPacientes:
        file.write(f"{paciente[1]}: {paciente[9]}: {promedio}\n")
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
