"""
Ejercicio 2 
Haga un programa que ingrese nombres de productos hasta que ingrese “FIN” y calcule el valor total y lo muestre en pantalla. Los productos y sus precios están en el archivo productos.txt y puede suponer que los productos que se ingresen siempre están en el archivo.
"""

def leerProductosTXT(archivoTxt: str) -> dict:
    productos = {}
    with open(archivoTxt, "r") as file:
        for line in file:
            listaProducto = line.strip().split(":")
            productos[listaProducto[0]] = int(listaProducto[1])
    return productos

def obtenerPrecio(producto: str, productos: dict) -> int:
    if producto in productos:
        precio = productos.get(producto)
        return precio
    return 0

### MAIN ###

productos = leerProductosTXT("productos.txt")
print(productos)
totalCompra = 0

while True:
    producto = input("[+] Ingrese producto: ").title()
    
    if producto.upper() == "FIN":
        break
    else:
        precio = obtenerPrecio(producto, productos)
        if precio != 0:
            print(f"[>] {producto} : {precio}")
            totalCompra += precio
print(f"Total de la compra: ${totalCompra}").M