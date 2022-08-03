from biblioteca import *

def procuraProduto (nome, produtos):
    tam = len(produtos)
    indice = -1
    
    for i in range (tam):
        if produtos[i] == nome:
            indice = i
    
    return indice

print ("=== Máquina de Vendas SkyNet ===")

produtos = inputVetor ("Defina os nomes: ", str)
precos = inputVetor ("Defina os preços: ", float)

nome = str (input ("Qual o produto? "))
indice = procuraProduto(nome, produtos)
total = 0

while indice != -1:
    total += precos[indice] 
    print (f'Preço: R$ {precos[indice]:.2f}')
    nome = str (input ("Qual o produto? "))
    indice = procuraProduto(nome, produtos)

print ("Finalizando sua compra...")
print (f'O valor total da compra é: R$ {total:.2f}')
print ("Obrigado por comprar na SkyNet!")

