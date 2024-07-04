# Desarrollo de una aplicación para eSports
---

Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:

La empresa de eSports "eShirlitos" necesita desarrollar un sistema que permita registrar los puntajes obtenidos por sus competidores en Fortnite, Valorant y Fifa. El objetivo del sistema es proporcionar las siguientes funcionalidades:

1. Registrar puntajes de torneo
2. Listar todos los puntajes
3. Imprimir por tipo
4. Salir del programa

## 1. Registrar puntajes de torneo

Para registrar puntajes, se requiere la siguiente información: Identificador de Jugador, Nombre y apellido del jugador, juego y puntaje obtenido. Por ejemplo, si el jugador compite en Fortnite y Fifa, se debe permitir seleccionar una de las tres opciones e ingresar la cantidad de puntos obtenidos en esos dos juegos. Además, se debe incluir el tipo de jugador (Principiante, Avanzado, Experto). Un ejemplo de registro de puntajes del torneo se muestra a continuación:

```
Id Jugador | Nombre | VALORANT | FORTNITE | FIFA | Tipo
-----------------------------------------------------
1          | Luis   | 0        | 125000   | 3500 | Principiante
```

Se debe validar que todos los datos sean ingresados.

## 2. Listar todos los puntajes

Esta opción muestra en pantalla la lista de todos los puntajes registrados, similar al ejemplo anterior (opción 1).

## 3. Imprimir por tipo

Para imprimir por tipo, el usuario debe seleccionar uno de los tres tipos (Principiante, Avanzado, Experto). Estos tipos deben estar previamente definidos en alguna colección de Python en el código. Al seleccionar uno de los tipos, se generará un archivo de texto (.txt) con el detalle de los puntajes obtenidos por los jugadores del tipo seleccionado. El archivo de texto debe tener el mismo formato que el registro completo de las opciones anteriores.

## 4. Salir del programa

El programa debe funcionar hasta que el usuario decida salir.

Este proyecto forma parte de la evaluación 3 para estudiantes de programación en Python en el Instituto DUOC UC Viña del Mar.