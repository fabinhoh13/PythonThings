def validaEntradas (qtdMorango, qtdMaca):
    if qtdMaca >= 0 and qtdMorango >= 0:
        retorno = True
    else:
        retorno = False
    return retorno

def calculaCustos (qtdMorango, qtdMaca):
    if qtdMorango <= 5:
        valorMorango = 2.50 * qtdMorango
    else:
        valorMorango = 2.20 * qtdMorango
        
    if qtdMaca <= 5:
        valorMaca = 1.80 * qtdMaca
    else:
        valorMaca = 1.50 * qtdMaca
        
    return valorMorango, valorMaca

#Programa Principal

quantidade_morangos = float (input ("Quantidade de Morangos (em kg): "))
quantidade_macas = float (input ("Quantidade de Maçãs (em kg): "))

valido = validaEntradas (quantidade_morangos, quantidade_macas)
if valido == True:
    valor_morango, valor_maca = calculaCustos (quantidade_morangos, quantidade_macas)
    print (f"O valor pago pelos morangos é: {valor_morango:.2f}")
    print (f"O valor pago pelas maçãs é: {valor_maca:.2f}")
    print (f"O valor total da sua compra é {valor_morango + valor_maca:.2f}")
else:
    print ("Entrada inválida")

