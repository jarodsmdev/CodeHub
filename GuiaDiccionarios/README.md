# Guía - Diccionarios y Conjuntos

## Introducción
Esta guía está diseñada para ayudar a comprender y practicar el uso de diccionarios y conjuntos en Python. A continuación, se presentan varios ejercicios que incluyen ejemplos con diccionarios y conjuntos.

## Ejercicios

### Ejercicio 1

#### Descripción
Trabajaremos con dos diccionarios que representan equipos de fútbol, donde las llaves son los números de camiseta y los valores son los nombres de los jugadores.

```python
Chile = {
    1: 'Claudio Bravo',
    4: 'Mauricio Isla',
    17: 'Gary Medel',
    18: 'Gonzalo Jaro',
    15: 'Jean Beausejour',
    8: 'Arturo Vidal',
    21: 'Marcelo Díaz',
    20: 'Charles Aranguiz',
    6: 'José Pedro Fuenzalida',
    7: 'Alexis Sánchez',
    11: 'Eduardo Vargas'
}

Argentina = {
    1: 'Sergio Romero',
    4: 'Gabriel Mercado',
    17: 'Nicolás Otamendi',
    13: 'Ramiro Funes Mori',
    16: 'Marcos Rojo',
    6: 'Lucas Biglia',
    14: 'Javier Mascherano',
    19: 'Éver Banega',
    10: 'Lionel Messi',
    9: 'Gonzalo Higuaín',
    7: 'Ángel Di María'
}
```

**A. Consultar Jugador por Número de Camiseta**

Haga un programa que permita escribir por teclado un equipo (Chile o Argentina), un número de camiseta y entregue el nombre del jugador. Considere el caso en el cual el número entregado por teclado no exista.

**B. Consultar Número de Camiseta por Nombre**

Haga un programa que permita ingresar el nombre de un jugador y un equipo, y entregue el número de camiseta de ese jugador. Si el nombre no existe, debe entregar un mensaje diciendo: “jugador no existe”.

**C. Consultar Jugadores por Número de Camiseta**

Haga un programa que permita ingresar por teclado un número de camiseta y entregue los jugadores (de ambos equipos si fuese el caso) que usan ese número.

**D. Eliminar Jugador por Nombre**

Haga un programa que permita ingresar el nombre de un jugador y elimine ese jugador del diccionario. Note que no se ingresa por teclado el equipo (debe buscar el nombre en ambos diccionarios). Si el nombre del jugador no existe, entonces debe entregar un mensaje diciendo: “jugador no existe”.

### Ejercicio 2
#### Descripción

Trabajaremos con un diccionario que tiene como llaves poderes, y como valores listas de nombres de superhéroes.

```python	
poderes = {
    "Volar": ["Superman", "Mujer maravilla", "Ironman"],
    "Rayos": ["Superman", "Ironman", "Ciclope", "Capitana marvel"],
    "Velocidad": ["Flash", "Superman"],
    "Fuerza": ["Hulk", "Mujer maravilla", "Superman"],
    "Inteligencia": ["Ironman", "Profesor-X"]
}
```
**A. Agregar Superhéroe a Poder**

Haga un programa que permita ingresar un poder y un nombre de superhéroe, y agregue ese superhéroe a la lista de ese poder. Considere que si el poder no existe en el diccionario, debe crearlo junto con la lista y el superhéroe recién ingresado por teclado. Si el poder existe y el superhéroe también, entonces no debe ingresarlo para que así no se repitan nombres.

**B. Eliminar Superhéroe**

Haga un programa que permita ingresar por teclado un superhéroe y elimine ese superhéroe de todo el diccionario.

**C. Consultar Superhéroes por Poderes**

Haga un programa que permita ingresar por teclado 2 poderes y entregue una lista con todos los superhéroes que tienen al menos uno de esos poderes. Los nombres en la lista no deben repetirse.

**D. Consultar Superhéroes por Poderes Combinados**

Haga un programa que permita ingresar por teclado 2 poderes y entregue una lista con los superhéroes que tienen ambos poderes. Si no hay superhéroe que tenga ambos poderes, debe entregar un mensaje que diga: ``“No existe superhéroe que tenga esos poderes”``.
