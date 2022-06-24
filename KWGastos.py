def calculo_kw (salario):
    retorno = (salario/7)/100
    return retorno

salario_minimo = float (input ("Informe o valor do Salário Mínimo (R$): "))
kw_gasto = float (input ("Informe a quantidade gasta de quilowatts (kW): "))

valor = calculo_kw(salario_minimo)

custo_sem_desconto = valor * kw_gasto
custo_com_desconto = custo_sem_desconto * 0.9

print (f"Valor de cada quilowatt (R$): {valor:.2f}")
print (f"Custo da energia eletrica sem o desconto (R$): {custo_sem_desconto:.2f}")
print (f"Custo da energia eletrica (desconto de 10%) (R$): {custo_com_desconto:.2f}")