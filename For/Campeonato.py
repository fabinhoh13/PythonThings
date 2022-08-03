from biblioteca import *

def calculaResultado (efetuados, recebidos):
    tam = len (efetuados)
    contadorDePontos = 0
    for i in range (tam):
        if efetuados[i] > recebidos[i]:
            contadorDePontos += 3
        elif efetuados[i] == recebidos[i]:
            contadorDePontos += 1
    return contadorDePontos


print ("=== Campeonato de Futebol ===")
n = int (input ("Defina a quantidade de N: "))

pontosCampeao = 0

for i in range (n):
    print (f"Time {i + 1}")
    golsEfetuados = inputVetor (". Defina os gols efetuados: ", int)
    golsRecebidos = inputVetor (". Defina os gols recebidos: ", int)
    pontuacaoTime = calculaResultado (golsEfetuados, golsRecebidos)
    print (f". Pontuação obtida: {pontuacaoTime}")
    if pontuacaoTime > pontosCampeao:
        pontosCampeao = pontuacaoTime
        indiceCampeao = i

print (f"Time Campeão: {indiceCampeao + 1} com {pontosCampeao} pontos!")