"""  ["Pedro", "Orellana", 67, "M"],
  
Considere una lista bidimensional como la siguiente:
[["Juan", "Veloz", 32, "M"],["Marcela", "Nuñez", 17 "F"], ["Pedro", "Orellana", 67, "M"], ["Ana", "González", 40, "F"], ["Leonora", "Veneca", 23, "F"],] 
y ordénela según edad, de menor a mayor
"""

# Datos de entrada
L = [
    ["Juan", "Veloz", 32, "M"],
    ["Marcela", "Nuñez", 17, "F"],
    ["Ana", "González", 40, "F"],
    ["Leonora", "Veneca", 23, "F"],
]

for i in range(len(L) - 1):
    for j in range(len(L)-1-i):
        if L[j][2] > L[j+1][2]:
            aux = L[j]
            L[j] = L[j+1]
            L[j+1] = aux

print(L)

