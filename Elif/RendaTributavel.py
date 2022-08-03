capital = float (input ("Digite a renda tributável do cidadão: "))

if capital <= 6000:
    imposto = 0
elif capital <= 20000:
    imposto = (capital - 6000) * 0.17
elif capital <= 50000:
    imposto = (capital - 20000) * 0.30 + 2380
elif capital <= 60000:
    imposto = (capital - 50000) * 0.42 + 11380
else:
    imposto = (capital - 60000) * 0.47 + 15580

saude = capital * 0.015
print (f"Renda Tributável: AU$ {capital:3.2f}")
print (f"Imposto Devido: AU$ {imposto:3.2f}")
print (f"Imposto para a Saúde: AU$ {saude:3.2f}")
print (f"Imposto Total a ser pago: AU$ {imposto+saude:3.2f}")