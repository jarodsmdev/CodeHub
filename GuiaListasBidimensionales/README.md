# Guía 3 - Listas bidimensionales
---

Nota: Recuerde que en los ejemplos, las palabras en negrita son reflejo de datos ingresados por teclado.

## Ejercicio 1

Haga un programa que reciba datos de 3 personas ingresados por teclado. Los datos
deben ser: Nombre, apellido y edad.Los datos deben ser guardados en una lista bidimensional. Muestre el resultado por pantalla.

Ejemplo:

```	Python
Ingrese nombre: Juan
Ingrese apellido: Veloz
Ingrese edad: 32
Ingrese nombre: Marcela
Ingrese apellido: Núñez
Ingrese edad: 17
Ingrese nombre: Pedro
Ingrese apellido: Orellana
Ingrese edad: 67
Los datos de las personas son: [[“Juan”“Veloz”, 32], [“Marcela”, “Nuñez”, 17], [“Pedro”, “Orellana”, 67]]
```

## Ejercicio 2

Dada una lista bidimensional como:

``` python
[[“Juan”, “Veloz”, 32], [“Marcela”, “Nuñez”, 17], [“Pedro”, “Orellana”, 67], [“Ana”, “González”, 40], [ ”Leonora”, “Veneca”, 23]]
```

haga un programa que permita revisar los datos de todas las personas y entregue cuantas personas son mayores de edad (edad mayor a 17).
Su programa debe funcionar con cualquier lista bidimensional como la del ejemplo.

Ejemplo:

``` python
Existen 4 personas mayores de edad
```

### Ejercicio 3

Haga un programa que permita ingresar 3 secuencias de números de distinto largo.
Cada vez que desee terminar una secuencia, debe ingresar la palabra `“fin”`. Cada secuencia debe ser almacenada en una lista y estas a su vez deben ser almacenadas en una lista, quedando así una lista bidimensional. Los números de las secuencias deben ser ordenadas de mayor a menor. Guíese del ejemplo:

Ejemplo:
    
``` python
Secuencia 1:
Ingrese número: 4
Ingrese número: 9
Ingrese numero: 2
Ingrese numero: 1
Ingrese numero: fin
Secuencia 2:
Ingrese número: -3
Ingrese numero: 0
Ingrese numero: 2
Ingrese numero: fin
Secuencia 3:
Ingrese número: 88
Ingrese numero: 12
Ingrese numero: fin
La lista bidimensional queda como: [[9,4,2,1], [2,0,-3], [88,12]]
```

### Ejercicio 4
Dada una lista bidimensional como:

`[[“Juan”, “Veloz”, 32, “M”], [“Marcela”, “Nuñez”, 17, “F”], [“Pedro”, “Orellana”, 67, “M”], [“Ana”, “González”, 40, “F”], [ ”Leonora”, “Veneca”, 23, “F”]]`
donde los datos de cada persona son: ``nombre``, ``apellido``, ``edad`` y ``género``.
Haga un programa que lea una lista como la anteriormente mostrada y separe las personas
por género. Debe dejar a todas las personas de género masculino en una lista y las de
género femenino en otra lista. El programa debe mostrar las listas creadas.

Ejemplo:
    
``` python
La lista de mujeres es: [[“Marcela”, “Nuñez”, 17, “F”], [“Ana”, “González”, 40, “F”], [”Leonora”, “Veneca”, 23, “F”]]
La lista de hombres es: [[“Juan”, “Veloz”, 32, “M”], [“Pedro”, “Orellana”, 67, “M”]]
```

### Ejercicio 5

Considere una lista bidimensional como la del ejercicio 4 y ordénela según edad, de menor a mayor.

Ejemplo:

``` python
[[“Marcela”, “Nuñez”, 17, “F”], [ ”Leonora”, “Veneca”, 23, “F”], [“Juan”, “Veloz”, 32, “M”], [“Ana”, “González”, 40, “F”], [“Pedro”, “Orellana”, 67, “M”]]
```

### Ejercicio 6

Haga un programa que dada una lista bidimensional como:

``` Python
[[“Marcela”, “Nuñez”, 17, “F”], [ ”Leonora”, “Veneca”, 23, “F”], [“Juan”, “Veloz”, 32, “M”], [“Ana”, “González”, 40, “F”], [“Pedro”, “Orellana”, 67, “M”]]
```
permita eliminar los datos de una persona en particular. El programa debe permitir ingresar un nombre y apellido por teclado, y si esa persona existe en la lista, sus datos deben ser eliminados de la lista y debe mostrar como queda la lista. Si no existe esa persona, el programa debe mostrar un mensaje diciendo: ``“esa persona no existe”``.

Ejemplo 1:

``` Python
Ingrese nombre: Juan
Ingrese apellido: Veloz
Persona eliminada
La lista queda asi: [[“Marcela”, “Nuñez”, 17, “F”], [ ”Leonora”, “Veneca”, 23, “F”], [“Ana”, “González”, 40, “F”], [“Pedro”, “Orellana”, 67, “M”]]
```

Ejemplo 2:

``` Python
Ingrese nombre: Juan
Ingrese apellido: Veneca
Esa persona no existe
```