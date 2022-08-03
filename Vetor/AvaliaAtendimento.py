from biblioteca import *

idades = inputVetor ("Defina as idades dos habitantes: ", int)

def contabilizarDemandas (idades):
    tam = len (idades)
    demandas = criarVetor (4, 0)
    
    for i in range (tam):
        if idades[i] >= 85:
            demandas[0] += 1
        elif idades[i] >= 65:
            demandas[1] += 1
        elif idades[i] >= 45:
            demandas[2] += 1
        elif idades[i] >= 18:
            demandas[3] += 1
    return demandas

demandas = contabilizarDemandas (idades)

print ("Demandas a serem atendidas por faixa etária:")
print (f". >= 85.........: {demandas[0]}")
print (f". < 85 e >= 65.: {demandas[1]}")
print (f". < 65 e >= 45.: {demandas[2]}")
print (f". >= 18.........: {demandas[3]}")

vacinas = inputVetor ("Defina as disponibilidades de vacinas: ", int)

def avaliaAtendimento (demandas, vacinas):
    tam = len (demandas)
    possibilidades = True
    
    for i in range (tam):
        if demandas[i] > vacinas[i]:
            possibilidades = False
    
    return possibilidades


temVacina = avaliaAtendimento (demandas, vacinas)

if temVacina == True:
    print ("A quantidade de vacinas é suficiente.")
else:
    print ("Infelizmente, precisaremos de mais vacinas.")