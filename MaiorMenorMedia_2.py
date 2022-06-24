from biblioteca import *

def estatNotas (notas):
    tam = len (notas)
    
    # 2, 4, 1, 5, 6
    maior = 0
    menor = 11
    media = 0
    
    for i in range (tam):
        if notas[i] > maior:
            maior = notas[i]
        if notas[i] < menor:
            menor = notas[i]
            
        media += notas[i]
    media /= tam
    
    maior = round (maior, 1)
    menor = round (menor, 1)
    media = round (media, 1)
    
    return maior, menor, media

notas = inputVetor ("Notas: ", float)

ma, me, med = estatNotas (notas)

print (f"Maior nota: {ma}")
print (f"Menor nota: {me}")
print (f"Nota média: {med}")
