"""
Segmentación Empresa
Construir programa que permita leer el archivo listadoRutEmpresa.csv e identificar las empresas que han tenido ventas inferiores a $100.000.000, entre $100.000.001 y $200.000.000 y más de $200.000.000, a lo cual usted deberá crear un archivo llamado “segmentacionEmpresas.json” que permita hacer esta distinción,  a  los  datos  listados  más  abajo  deberá  incorporar  una  columna  adicional  llamada clasificacionEmpresa donde se indique “Pequeño Contribuyente”, “Mediano Contribuyente” y “Gran Contribuyente”.
"""
import csv, json

def leerCSV(archivo: str):
    listaEmpresas = []
    with open(archivo, "r", newline="") as file:
        datos = csv.reader(file)
        for linea in datos:
            listaEmpresas.append(linea)
    return listaEmpresas

def segmentarEmpresas(lista: list) -> list:
    for e in range(1, len(lista)):
        #print(lista[e], end=" ")
        venta = int(lista[e][2].strip())
        lista[e].insert(2, venta)
        lista[e].pop()
        if venta <= 100000000:
            lista[e].append("Pequeño Contribuyente")
        elif venta <= 200000000:
            lista[e].append("Mediano Contribuyente")
        else:
            lista[e].append("Gran Contribuyente")
    lista[0].append("clasificacionEmpresa")
    return lista

def mostrarEmpresas(lista: list):
    for e in lista:
        print(e)
        
def transformarEnDiccionario(lista: list) -> list:
    """
    Transforma una lista de listas en una lista de diccionarios
    
    Args:
        lista: list - Lista de listas
    
    Returns:
        list de diccionarios con los datos de la lista original
    """
    # Extraer las claves
    claves = lista[0]
    
    # Declarar e inicializar una lista vacía
    listaFinal = []
    
    # Iterar sobre el resto de las filas
    for empresa in lista[1:]:
        registro = {} # Declarar un diccionario temporal
        
        # Iterar sobre los índices de las claves
        for i in range(len(claves)):
            # Asignar al diccionario temporal la clave y el valor
            registro[claves[i]] = empresa[i]
        
        # Agregar el diccionario temporal a la lista final
        listaFinal.append(registro)
    
    # Retornar la lista final
    return listaFinal

def exportarJSON(empresas: list):
    try:
        FILE_NAME = "segmentacionEmpresas.json"
        with open(FILE_NAME, "w") as file:
            json.dump(empresas, file, indent = 4)
        print("[!] Fichero JSON generado con éxito")
    except Exception as error:
        print("[!] ERROR: Se ha producido un error:", error)

def main():
    listaEmpresas = leerCSV("listadoRutEmpresa.csv")
    listaFormateada = segmentarEmpresas(listaEmpresas)
    mostrarEmpresas(listaFormateada)
    diccionarioEmpresas = transformarEnDiccionario(listaFormateada)
    exportarJSON(diccionarioEmpresas)

### MAIN ###
if __name__ == "__main__":
    main()
