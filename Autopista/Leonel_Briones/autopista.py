dicc = {}

transitos = [['BBJJ77',2], ['CCHH19',3], ['AAFF37',3], ['BBJJ77',1], 
['AAFF37',1], ['DDKK33',3], ['AAFF37',1], ['AAFF37',2]]

for p in transitos:
    portico = p[1]
    patente = p[0]
    
    if portico in dicc:
        dicc[portico].append(patente)
    else:
        dicc[portico] = (patente)


for k, v in dicc.items():
    v.sort()
    dicc[k] = list(set(v))

print(dicc)