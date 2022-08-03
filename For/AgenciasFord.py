print ("=== Agências Ford ===")

denovo = 's'
agencias = 1
while (denovo != 'n'):
    print (f'. Agência {agencias}:')
    vendedores = int (input (' . Quantidade de vendedores: '))
    
    maiorVenda = 0
    totalVendas = 0
    totalValorVendas = 0.0
    menorMedia = 999999999999999999999
    for contVendedores in range (1, vendedores + 1):
        print (f'  . Vendedor {contVendedores}')
        veiculos = int (input ("   . Quantidade de veículos: "))
        valorVendas = float (input ("   . Valor em vendas (R$) : "))
        if veiculos > maiorVenda:
            maiorVenda = veiculos
        totalVendas = veiculos
        totalValorVendas += valorVendas
        contVendedores += 1
    mediaVendas = totalValorVendas / totalVendas
    print (f' . Média dos valores de venda (R$) : {mediaVendas:.3f}')
    print (f' . Maior quantidade de veículos: {maiorVenda}')
    agencias += 1
    if mediaVendas < menorMedia:
        menorMedia = mediaVendas
    denovo = input ("Mais uma agência (s/n)? ")

print (f'Menor média: {menorMedia:.3f}')
    