# Ejercicio NIF

Un NIF es un Número de Identificación Fiscal otorgado por la Unión Europea a los ciudadanos mayores de 15 años. Es equivalente o similar al Rut o número de identificación chileno.

Este NIF tiene ciertos beneficios para quien lo obtiene. La estructura del NIF en España es la siguiente:

- 99999999-RTX
- 03034567-XXY
- 12312345-CCU
- 00000001-03F

En el registro de ciudadanos pertenecientes a la Unión Europea de España, del pueblo del sur de Andalucía, se requiere desarrollar un programa con un menú que contenga las siguientes opciones:

## Opción 1: Grabar

Corresponde a guardar ciertos datos de una persona, entre ellos: NIF, nombre, apellido y edad. Debe verificar que el NIF sea correcto, que el nombre incluya al apellido en una sola entrada por teclado (un solo input() separado por espacio) y que el nombre y apellido por separado tengan un mínimo de 8 caracteres. Además, la edad debe ser mayor o igual a 15.

## Opción 2: Buscar

Corresponde a buscar a una persona por su NIF y mostrar toda su información almacenada.

## Opción 3: Guardar archivos

Corresponde a crear un archivo .csv que contenga los datos de todas las personas entre un rango de edad dado por teclado, ordenadas alfabéticamente por nombre. El archivo debe llamarse "edades_entre_a_y_b.csv", donde "a" y "b" son las edades del rango dado.

## Opción 4: Salir

Corresponde a salir del programa emitiendo un mensaje de salida. Se debe considerar el nombre y apellido del usuario, así como la versión del programa.

## Instrucciones Generales

Escribir un programa que contenga dos archivos:

1. Principal: debe contener un menú con las opciones para acceder a cada función requerida. Solo se debe considerar el ingreso de datos y el despliegue de información.
2. Funciones: debe contener todos los procesos y validaciones de los requerimientos.
