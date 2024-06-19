"""
Ejercicio 4
Haga un programa que lea el archivo alumnos.csv y escriba un archivo aprobados.csv y reprobados.csv. Cada archivo debe contener los nombres y apellidos de los alumnos que aprobaron y reprobaron considerando el promedio de sus notas. El formato de los archivos que debe escribir debe ser: nombre-apellido, y debe haber un alumno por cada fila del archivo.
"""


def leerArchivoCSV(archivo: str) -> list:
    alumnos = {}
    with open(archivo, "r") as file:
        for line in file:
            alumno = line.strip().split(":")
            notas = alumno[2:]
            notasformateadas = []

            for n in notas:
                notasformateadas.append(float(n))
                alumnos[f"{alumno[0]} - {alumno[1]}"] = notasformateadas
    return alumnos

def crearArchivos(archivo: str, listAlumnos: list):
    file = open(archivo, "w")
    for alumno in listAlumnos:
        file.write(alumno + "\n")
    file.close()
    
def calcularPromedio(nombre: str, diccAlumnos: dict) -> float:
    listaNotas = diccAlumnos[nombre]
    sumaNotas = 0
    promedio = 0
    for nota in listaNotas:
        sumaNotas += nota
    promedio = round(sumaNotas / len(listaNotas),1)
    return promedio

def calificarAlumnos(diccAlumnos: dict) -> list:
    aprobados = []
    reprobados = []
    calificados = []

    for alumno in diccAlumnos:
        if calcularPromedio(alumno, diccAlumnos) >= 4.0:
            #print(alumno, "APROBADO")
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)
            #print(alumno, "REPROBADO")
    calificados.append(aprobados)
    calificados.append(reprobados)
    #print(calificados)
    return calificados

### MAIN ###
EXPORT_FILES_NAMES = ("aprobados.csv", "reprobados.csv")
data = leerArchivoCSV("alumnos.txt")
resultadoCalificacion = calificarAlumnos(data)
for i in range(len(EXPORT_FILES_NAMES)):  
    crearArchivos(EXPORT_FILES_NAMES[i], resultadoCalificacion[i])
print("[!] Proceso Finalizado, se han creado 2 archivos")



