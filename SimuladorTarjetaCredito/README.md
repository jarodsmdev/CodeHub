# Descripción de la Actividad

---

El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible.

Las opciones disponibles deben estar construidas de la siguiente forma:
1. **Pago de Tarjeta de Crédito:**
    - ✔ El usuario comienza con una deuda de $100.000
    - ✔ El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito
    - ✔ Se debe verificar que el monto ingresado sea mayor o igual a cero.
    - ✔ Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
    - ✔ Al pagar el sistema debe descontar de la deuda total.
    - ✔ Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
2. **Simulación de Compras:**
    - ✔ El usuario puede simular realizar un número ilimitado de compras.
    - ✔ Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra.
    - ✔ Se verifica que el monto de la compra sea mayor o igual a cero.
    - ✔ Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
3. **Salir:**
    - ✔ Al seleccionar esta opción, el programa debe cerrarse o finalizar.

### A considerar:
1. **Manejo de Errores:**
    - ✔ Se utilizan bloques try y except para manejar posibles errores al ingresar datos, validar valores no numéricos y errores inesperados.
2. **Manejo de Errores Específico:**
    - ✔ Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas


### Requisitos para Resolver el Problema:

1. **Conocimientos de Programación en Python:**
   - Se requiere un entendimiento básico de Python para desarrollar el programa.
   - Se debe conocer cómo crear funciones, manejar estructuras de control como bucles y condicionales, y manejar errores con try-except.


2. **Manejo de Datos Numéricos:**
   - Es importante entender cómo manejar datos numéricos y realizar operaciones matemáticas para calcular pagos, saldos y montos de compras.

3. **Conocimientos de Interfaz de Usuario:**
   - Se debe tener experiencia en crear una interfaz de usuario amigable con un menú de opciones claras y mensajes de error informativos.

4. **Manejo de Excepciones:**
   - Se requiere conocimiento en manejar excepciones para capturar errores de entrada del usuario y errores inesperados durante la ejecución del programa.

5. **Lógica de Negocio:**
   - Se necesita comprender la lógica detrás de realizar pagos, sumar compras y actualizar saldos de tarjetas de crédito para diseñar esta simulación de programa de manera efectiva.

### Herramientas Recomendadas:

1. **Entorno de Desarrollo Integrado (IDE):**
   - Se recomienda utilizar un IDE como PyCharm, Visual Studio Code o Jupyter Notebook para desarrollar y probar el programa.

2. **Documentación de Python:**
   - Es útil tener acceso a la documentación oficial de Python para consultar funciones y métodos necesarios durante el desarrollo.
