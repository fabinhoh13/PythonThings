from biblioteca import *

produtos = inputMatriz ("Matriz de estoque: ", int)

atualizacoes = int (input ("Numero de atualizações: "))

for i in range (atualizacoes):
    loja = int (input ("Indice da loja: "))
    produto = int (input ("Indice do produto: "))
    novo = int (input ("Novo estoque: "))
    produtos[loja][produto] = novo
    print (produtos)