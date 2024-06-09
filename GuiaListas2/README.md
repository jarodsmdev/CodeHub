# Guia 2 - Listas

## Descripción

Esta guía incluye una serie de ejercicios que trabajan con listas en Python. Cada ejercicio presenta un problema específico y su respectiva solución utilizando listas. A continuación se detallan los ejercicios incluidos en esta guía.

## Ejercicios

### Ejercicio 1

Haga un programa que considere la lista `[2, 8, 4, 12, 1, 19]`, y entregue la suma de todos sus valores, pero sin usar la función `sum()`.

### Ejercicio 2

Haga un programa que permita agregar 3 nombres en una lista y un nombre a buscar. El programa debe entregar las veces que aparece ese nombre en la lista. Considere que el programa debe funcionar para nombres en minúsculas y mayúsculas.

**Ejemplo 1:**

```python
Ingrese nombre: Mabel
Ingrese nombre: ANA
Ingrese nombre: pedro
Ingrese nombre a buscar: ana
El nombre aparece 1 vez
```


**Ejemplo 2:**

```python
Ingrese nombre: ana
Ingrese nombre: ANA
Ingrese nombre: pedro
Ingrese nombre a buscar: Ana
El nombre aparece 2 veces
```


### Ejercicio 3

Haga un programa que reciba palabras hasta que se ingresa un string vacío ("", de largo cero). Esas palabras deben ser almacenadas en una lista y mostrar la lista. Luego, debe mostrar la lista ordenada alfabéticamente, pero descendentemente.

**Ejemplo:**

```python
Ingrese palabra: saber
Ingrese palabra: programar
Ingrese palabra: es
Ingrese palabra: importante
Ingrese palabra:
La lista es: ["saber", "programar", "es", "importante"]
La lista ordenada es: ["saber", "programar", "importante", "es"]
```	


### Ejercicio 4

Haga un programa que reciba palabras hasta que se ingresa un 0 (cero). Esas palabras deben ser almacenadas en una lista, pero solo las palabras que tengan 4 o más caracteres. La lista debe ser mostrada por pantalla.

**Ejemplo:**

```python
Ingrese palabra: saber
Ingrese palabra: programar
Ingrese palabra: es
Ingrese palabra: importante
Ingrese palabra: 0
La lista es: ["saber", "programar", "importante"]
```


### Ejercicio 5

Haga un programa que permita ingresar un número entero positivo. Dado este número, debe generar una lista con números del 0 hasta el número ingresado usando la función `range()`. El programa debe entregar la desviación estándar de los números de la lista.

Considere que la fórmula de la desviación estándar es:

\[ \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (X_i - \bar{X})^2} \]

donde \( N \) es la cantidad de números, \( X_i \) es el número \( i \)-ésimo y \( \bar{X} \) es el promedio.

**Ejemplo 1:**

```python
Ingrese número: 5
La desviación estándar es: 1.7
```


**Ejemplo 2:**

```python
Ingrese número: 1
La desviación estándar es: 0.5
```


### Ejercicio 6

Haga un programa que reciba 3 nombres y 3 apellidos. Estos deben ser almacenados en 2 listas, una para nombres y otra para apellidos. Luego, el programa debe preguntar por un apellido y se debe mostrar por pantalla el nombre asociado a ese apellido. Si el apellido se repite una o más veces, debe mostrar todos los nombres asociados a ese apellido, sino, debe mostrar el mensaje: apellido no encontrado.

**Ejemplo 1:**

```python
Ingrese nombre: max
Ingrese apellido: diaz
Ingrese nombre: juan
Ingrese apellido: diaz
Ingrese nombre: marcela
Ingrese apellido: gonzalez
Pregunte por un apellido: diaz
Nombre encontrado: max
Nombre encontrado: juan
```

**Ejemplo 2:**

```python
Ingrese nombre: max
Ingrese apellido: diaz
Ingrese nombre: juan
Ingrese apellido: diaz
Ingrese nombre: marcela
Ingrese apellido: gonzalez
Pregunte por un apellido: soto
Apellido no encontrado
```