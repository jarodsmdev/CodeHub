# Venta de Pasajes de Vuelos - Aerolínea Duoc

## Descripción

Este programa permite implementar la venta de pasajes de una aerolínea con una capacidad de 42 asientos. Los asientos se gestionan mediante una matriz bidimensional (7x6) y diversas funciones para realizar las operaciones necesarias. La distribución de precios es la siguiente:

    Asientos del 1 al 30: $78,900
    Asientos del 31 al 42: $240,000 (VIP)

El programa cuenta con un menú interactivo con cinco opciones principales para gestionar la compra, cancelación y modificación de pasajes, así como la visualización de asientos y el almacenamiento de la información.
Funcionalidades
### Opción 1: Visualización de Asientos

    Permite visualizar el estado de los asientos.
    Los asientos disponibles se muestran con un número y los ocupados con una 'X'.

### Opción 2: Compra de Pasajes

    Solicita los datos del pasajero: nombre, RUT, teléfono, banco al que pertenece (Banco del Pueblo u otro).
    Solicita el número del asiento que desea comprar (un pasaje por persona).
    Valida que el asiento esté disponible.
    Si el pasajero pertenece al Banco del Pueblo, recibe un descuento del 15%.
    Muestra el valor total a pagar, aplicando el descuento si corresponde.

### Opción 3: Anulación de Pasaje

    Solicita el número del asiento (y el RUT si se desea) para comprobar si está ocupado.
    Libera el asiento y borra los datos del pasajero en caso de anulación.

### Opción 4: Modificación de Datos del Pasajero

    Solicita el número del asiento y el RUT para verificar la existencia del pasajero y su asiento correspondiente.
    Muestra los datos del pasajero.
    Ofrece la opción de modificar el RUT o el teléfono y actualiza la información.

### Opción 5: Guardado de Información

    Permite guardar la información de la venta de pasajes en un archivo de preferencia.

---

## Instrucciones de Uso

    Inicio del Programa: Ejecute el programa para acceder al menú principal.
    Seleccionar una Opción: Ingrese el número correspondiente a la opción deseada:
        1 para visualizar los asientos.
        2 para comprar un pasaje.
        3 para anular un pasaje.
        4 para modificar datos de un pasajero.
        5 para guardar la información en un archivo.
    Seguir Indicaciones: Según la opción seleccionada, siga las instrucciones proporcionadas por el programa para completar la operación.
    Finalizar: Una vez realizadas las operaciones deseadas, el programa ofrecerá la opción de finalizar.

## Requisitos del Sistema

    Python 3.6 o superior.
    Librerías estándar de Python.