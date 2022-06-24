from biblioteca import *

notas = inputVetor ('Notas:', float)

def estatNotas (notas):
    maior = 0 
    menor = 999999999999
    media = 0

    for i in range (len (notas)):
        if maior > notas[i]:
            maior = notas[i]
        if menor < notas[i]:
            menor = notas[i]
        media += notas[i]
    media = media / (len (notas))
        
        
    return round (maior, 2), round(menor, 2 ), round(media, 2)

ma, me, med = estatNotas (notas)


print (f'Maior nota: {ma :.2f}')
print (f'Menor nota: {me :.2f}')
print (f'Nota media: {med:.2f}')