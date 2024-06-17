"""
Ejercicio 1
Haga un programa que lea el archivo quijote.txt y haga:
a) Muestre por pantalla cuántas líneas tiene el archivo.
b) Muestre por pantalla cuántas palabras tiene.
c) Muestre por pantalla cuantas letras tiene.
d) Muestre la palabra más larga.
e) Muestre en una lista todas las palabras que empiezan con una vocal.
"""

def cantidadLineas(lista: list) -> int:
    """Funcion que recibe una lista y retorna la cantidad de lineas que tiene el archivo
    
    Args:
        lista (list): lista de palabras
        
    Returns:
        int: cantidad de lineas
    """
    return len(lista)

def cantidadPalabras(lista:list) -> int:
    """
    Funcion que recibe una lista y retorna la cantidad de palabras que tiene el archivo
    
    Args:
        lista (list): lista de palabras
        
    Returns:
        int: cantidad de palabras
    """
    contadorPalabras = 0
    for l in lista:
        contadorPalabras += len(l)
    return contadorPalabras

def cantidadLetras(lista:list) -> int:
    """
    Funcion que recibe una lista y retorna la cantidad de letras que tiene el archivo
    
    Args:
        lista (list): lista de palabras
    
    Returns:
        int: cantidad de letras
    """
    contadorLetras = 0
    for l in lista:
        for e in range(len(l)):
            contadorLetras += len(l[e])
    return contadorLetras

def palabrasConVocal(lista: list) -> list:
    """
    Funcion que recibe una lista y retorna una lista con las palabras que comienzan con una vocal
    
    Args:
        lista (list): lista de palabras
        
    Returns:
        list: lista de palabras que comienzan con una vocal
    """
    vocales = "aeiouáéíóúü"
    listaPalabrasInicialesConVocal = []
    for l in lista:
        for i in range(len(l)):
            if l[i][0].lower() in vocales:
                listaPalabrasInicialesConVocal.append(l[i])
    return listaPalabrasInicialesConVocal

def leerArchivo(archivo_txt:str) -> list:
    """
    Funcion que recibe un archivo txt y retorna una lista con las palabras del archivo
    
    Args:
        archivo_txt (str): archivo txt
        
    Returns:
        list: lista de palabras
    """
    try:
        data = open(archivo_txt, 'r')
    except FileNotFoundError:
        print("[!] ERROR: El archivo no existe")
    
    listaContenedor = []
    for linea in data:
        lista = linea.strip().split()
        listaContenedor.append(lista)

    return listaContenedor

def main():
    data = leerArchivo("quijote.txt")
    if len(data) != 0:
        print("Cantidad de lineas:", cantidadLineas(data))
        print("Cantidad de palabras:", cantidadPalabras(data))
        print("Cantidad de letras:", cantidadLetras(data))
        print("Palabras que comiencen con una vocal:", palabrasConVocal(data))
        
### MAIN ###
main()

