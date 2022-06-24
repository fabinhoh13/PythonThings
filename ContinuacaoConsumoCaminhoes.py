from biblioteca import *

def calculaConsumos (C, Q):
    retorno = []
    for i in range (len(Q)):
        retorno.append([])
        for j in range (len (Q[i])):
            kmpl = Q[i][j]/C[j]
            retorno[i].append(round (kmpl, 2))
            
    return retorno
    
def calculaMedias (Consumos):
    lins, cols = dimMatriz(Consumos)
    medias = criarVetor (cols, 0)
    for i in range (lins):
        for j in range (cols):
            medias[j] += Consumos[i][j]
    for i in range (cols):
        medias[i] = round (medias[i]/lins, 2)
    
    return medias

print ("Teste de consumo")
print ("Capacidade dos tanques:")
capacidades = inputVetor (">>> ", float)

if (len(capacidades) != 0):
    erro = False
    print ("Quilometragens dos condutores:")
    quilometragens = inputMatriz (">>> ", float)
    for i in range (len(quilometragens)):
        if (len(quilometragens[i]) != len (capacidades)):
            erro = True
    if (len(quilometragens) == 0): 
        print("Deve haver pelo menos um condutor")
    elif (erro == True):
        print ("Quantidade de automóveis incompatível")
    else:
        kmpl = calculaConsumos(capacidades, quilometragens)
        print ("Consumos km/l:")
        print (kmpl)
        print ("Medias dos consumos por automóvel:")
        medias = calculaMedias (kmpl)
        print (medias)
else:
    print ("É necessário pelo menos um automóvel")
