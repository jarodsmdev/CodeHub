
---

## Descripción de la Actividad

Esta actividad consiste en la creación de un programa de inicio de sesión con funcionalidades adicionales, diseñado para grupos de trabajo de un mínimo de 2 alumnos y un máximo de 3 alumnos.

## Etapas

### 1. Creación del Menú de Inicio de Sesión

Se debe implementar un menú de inicio de sesión con las siguientes opciones:

1. **Iniciar Sesión**
2. **Registrar Usuario**
3. **Salir**

#### Variables de Usuario y Contraseña

Se deben crear 3 variables de usuario y 3 variables de contraseña, inicializadas con un valor vacío, por ejemplo:

- `usuario1 = None`
- `usuario2 = None`
- `usuario3 = None`
- `contrasena1 = None`
- `contrasena2 = None`
- `contrasena3 = None`

### 2. Iniciar Sesión

Si se selecciona la opción 1 y no hay usuarios registrados, el sistema indicará que es necesario registrar un usuario antes de iniciar sesión y volverá al menú principal.

Si se ingresan el usuario y la contraseña correctamente, el sistema mostrará el siguiente menú:

1. **Realizar Llamada**
2. **Enviar Correo Electrónico**
3. **Cerrar Sesión**

### 3. Realizar Llamada

Esta opción solicita un número de celular que debe comenzar con 9 y tener 9 dígitos (ejemplo: 985447561).

### 4. Enviar Correo Electrónico

Esta opción solicita un correo electrónico válido (con al menos un carácter "@"), utilizando validación con `for` y `while`. Además, se pide el mensaje a enviar, guardado en una variable llamada "mensaje".

### 5. Cerrar Sesión

Vuelve al menú principal.

### Consideraciones Adicionales

- El sistema no acepta opciones distintas a 1, 2 y 3 en ambos menús. Si se ingresa una opción incorrecta, emite un error y vuelve a solicitar la opción.
- Se recomienda utilizar `try` y `Exception` cuando sea necesario para manejar errores.

---
