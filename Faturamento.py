from biblioteca import *

print ("=== Programa de metas das Lojas Americanas ===")
faturamentos = inputMatriz ("Defina os faturamentos: ", float)
metas = inputVetor ("Defina as metas: ", float)

lin, col = dimMatriz(faturamentos)
faturamentoFiliais = criarVetor (lin, 0)

for i in range (lin):
    for j in range (col):
        faturamentoFiliais[i] += faturamentos[i][j]

for i in range (lin):
    print (f"=== Filial {i + 1} ===")
    print (f"Faturamento: R$ {faturamentoFiliais[i]:.2f}")
    print (f"Meta: R$ {metas[i]:.2f}")
    
    if (faturamentoFiliais[i] > metas[i]):
        folga = faturamentoFiliais[i] - metas[i]
        print (f"Meta atingida com FOLGA de R$ {folga:.2f}")
    elif (faturamentoFiliais[i] < metas[i]):
        aumento = metas[i] - faturamentoFiliais[i]
        print (f"Meta ***NÃO ATINGIDA***, aumentar faturamento em R$ {aumento:.2f}")
    else:
        print (f"Meta atingida SEM QUALQUER FOLGA.")
    