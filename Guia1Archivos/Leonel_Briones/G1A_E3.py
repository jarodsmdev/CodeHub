"""
Ejercicio 3 
Haga un programa con la misma situación del ejercicio anterior, pero ahora debe suponer que si es posible que ingresen productos que no existen en el archivo productos.txt. Si un producto no existe, no debe sumarlo al total y al final del programa, debe mostrar por pantalla en una lista  todos los productos que no estaban. 
"""

def leerArchivoTxt(Archivo):
    diccionario = {}
    with open(Archivo, "r") as file:
        for line in file:
            producto =line.strip().split(":")
            diccionario[producto[0]] = int(producto[1])
    return diccionario
    

def existeProducto(producto, diccionario):
    if producto in diccionario:
        return True
    return False
            
data = leerArchivoTxt("productos.txt")
producto = ""
sumaTotal = 0
productosNoEstan = []

while True:

    producto = input("[+] Ingrese producto: ")
    
    if producto == "FIN":
        break
    else:
        producto = producto.title()
        if existeProducto(producto,data):
            precio = data[producto]
            print(f"[>] {producto} precio {precio}")
            sumaTotal += precio
        else:
            print(f"[!] Producto {producto} no existe")
            if not producto.lower() == "fin":
                productosNoEstan.append(producto)
print("Total compra: $",sumaTotal)
print("Productos que no tenemos: ",productosNoEstan)



