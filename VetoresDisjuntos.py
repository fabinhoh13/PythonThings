from biblioteca import *

def vetoresDisjuntos (vetor1, vetor2):
    tam1 = len (vetor1)
    tam2 = len (vetor2)
    
    for i in range (tam1):
        for j in range (tam2):
            if vetor1[i] == vetor2[j]:
                return False
    return True

vetor1 = inputVetor ("Entre com o primeiro conjunto: ", str)
vetor2 = inputVetor ("Entre com o segundo conjunto: ", str)

if (vetoresDisjuntos (vetor1, vetor2) == True):
    print ('Os conjuntos são disjuntos!')
else:
    print ('Os conjuntos não são disjuntos!')
