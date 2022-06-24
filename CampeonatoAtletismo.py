from biblioteca import *

print ('*** Campeonato de Atletismo ***')

atletas = inputMatriz ("Digite os tempos dos atletas: ", float)
lin, col = dimMatriz (atletas)
somatorioAtletas = criarVetor (lin, 0)

for i in range (col):
    indiceMenorTempo = 0
    for j in range (lin):
        if atletas[j][i] < atletas[indiceMenorTempo][i]:
            indiceMenorTempo = j
        somatorioAtletas[j] += atletas[j][i]
    print (f'Melhor atleta do percurso {i + 1}: {indiceMenorTempo + 1}')

indiceMelhorAtleta = 0
for i in range (lin):
    if somatorioAtletas[i] < somatorioAtletas[indiceMelhorAtleta]:
        indiceMelhorAtleta = i

print (f'Vencedor: atleta {indiceMelhorAtleta + 1}')
print (f'Tempo acumulado: {somatorioAtletas[indiceMelhorAtleta]:.2f} minutos')