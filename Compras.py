vct = float (input ("Qual o valor da compra? "))
if (vct > 0 and vct <= 300):
    valor_total = vct * 0.98
    print (f"Valor do Pagamento: R$ {valor_total}")
    
if (vct > 300 and vct <= 600):
    valor_total = vct * 0.96
    print (f"Valor do Pagamento: R$ {valor_total}")
    
if (vct > 600 and vct <= 900):
    valor_total = vct * 0.94
    print (f"Valor do Pagamento: R$ {valor_total}")
    
if (vct > 900):
    valor_total = vct * 0.92
    print (f"Valor do Pagamento: R$ {valor_total}")
    
else:
    print ("ERRO: Valor de compra invalida!")