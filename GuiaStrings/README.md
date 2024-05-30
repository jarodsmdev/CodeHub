# Guía de String
---
Nota: recuerde que las letras en negrita de los ejemplos representan datos ingresados por teclado.

## Ejercicio 1
Escriba un programa que permita ingresar una palabra y entregue la cantidad de vocales, consonantes y caracteres especiales. Cualquier otro carácter que no sea vocal ni consonante se considera carácter especial.

Ejemplo 1:
``` Python
Ingrese palabra: DuocUC
La palabra tiene 3 vocales, 3 consonantes y 0 otro carácter.
```

Ejemplo 2:
``` Python
Ingrese palabra: Saludos!!
La palabra tiene 3 vocales, 4 consonantes y 2 otro carácter
```
## Ejercicio 2

Una cadena de ADN es válida si está compuesta únicamente por las bases Adenina (A), Citosina (C), Guanina (G) o Timina (T). Escriba un programa para validar una cadena de ADN. Una cadena de ADN tiene solo 4 caracteres.

Ejemplo 1:
``` Python
Ingrese cadena: ACGG
Cadena valida
```
Ejemplo 2:
``` Python
Ingrese cadena: AXGG
Cadena invalida
```
Ejemplo 3:
``` Python
Ingrese cadena: AGT
Cadena invalida
```

## Ejercicio 3
Escriba un programa que construya un string con las letras que coinciden en dos strings ingresados como entrada. Por ejemplo, “amorosos” y “amortiza” coinciden en: “amor”; por otra parte, “conformidad” y “contorno” coinciden en “conor”. Observe que los strings pueden tener distintos largos.

Ejemplo:
``` Python
Ingrese string 1: amorosos
Ingrese string 2: amortiza
String coincidente: amor
```

## Ejercicio 4
Escriba un programa que permita ingresar una frase y entregue el número de palabras que contiene la frase.

Ejemplo 1:
``` Python
Ingrese frase: Fundamentos de programacion
La frase contiene 3 palabras
```

Ejemplo 2:
``` Python
Ingrese frase: CITT
La frase contiene 1 palabra
```	

## Ejercicio 5

Escriba un programa que encuentre la palabra de mayor longitud dentro de un texto cuyas palabras se separan por un único espacio y no hay espacio al final. Puede considerar que solo ingresan letras y espacios. Si hay dos o más palabras que tienen la mayor longitud, puede entregar cualquiera.

Ejemplo 1:
``` Python
Ingrese frase: Necesito estudiar para la prueba dos
La palabra con mayor longitud es: estudiar
```

Ejemplo 2:

``` Python
Ingrese frase: Chile
La palabra con mayor longitud es: Chile
```

## Ejercicio 6
Haga un programa que permita ingresar string que contiene un nombre y una nota separado por un dos puntos “:”. Debe permitir ingresar datos hasta que se ingrese la palabra “Terminar”. La palabra “Terminar” puede estar escrita con mayúscula o minúscula y debe funcionar de igual manera. Luego, debe entregar la cantidad de estudiantes aprobados y reprobados.

Ejemplo 1:
``` Python
Ingrese dato: Mauricio:4.3
Ingrese dato: Ana:6.7
Ingrese dato: Felipe:3.2
Ingrese dato: terminar
Hubo 2 estudiantes aprobados y 1 estudiantes reprobados.
```

Ejemplo 2:
``` Python
Ingrese dato: Alejandra:5.7
Ingrese dato: Pedro:6.1
Ingrese dato: TERMINAr
Hubo 2 estudiantes aprobados y 0 estudiantes reprobados.
```