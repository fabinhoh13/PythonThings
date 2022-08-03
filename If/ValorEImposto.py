valor_compra = float (input ("Informe o valor da compra: "))

valor_desconto = 0
if (valor_compra <= 150.0):
    valor_desconto = valor_compra * 0.10

if (valor_compra > 150.0):
    valor_desconto = valor_compra * 0.20
    
valor_c_desconto = valor_compra - valor_desconto

valor_imposto = valor_c_desconto * 0.08

valor_total = valor_c_desconto + valor_imposto

print (f"Valor do desconto R$ {valor_desconto}")
print (f"Valor da compra com desconto: R$ {valor_c_desconto}")
print (f"Valor do imposto: R$ {valor_imposto}")
print (f"Total a pagar: R$ {valor_total}")