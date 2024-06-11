"""
## Ejercicio 2
El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

| Edad       | IMC < 22.0 | IMC ≥ 22.0 |
|------------|------------|------------|
| edad < 45  | bajo       | medio      |
| edad ≥ 45  | medio      | alto       |
"""

def IMC(peso, estatura, edad):
    
    if estatura <= 0:
        print("[!] ERROR: Peso debe ser mayor a cero")
    else:
        imc = peso/estatura ** 2
        if edad < 45:
            if imc < 22:
                return "Bajo"
            else:
                return "Medio"
        else:
            if imc >= 45:
                return "Medio"
            else:
                return "Alto"

print(IMC(70,1.8, 20))