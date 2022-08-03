def custo (v, t, r, p):
    c = ((v*t)/r)*p
    return c

print ("Custo do combustível em uma viagem")
vm = float (input ("Velocidade Média (km/h): "))
tp = float (input ("Tempo previsto (h): "))
rg = float (input ("Rendimento com gasolina (km/litro): "))
pg = float (input ("Preço do litro de gasolina (R$): "))
pa = float (input ("Preço do litro de álcool (R$): "))

custo_gasolina = custo (vm, tp, rg, pg)
print (f"Custo usando gasolina (R$): {custo_gasolina:.2f}")

ra = 0.7 * rg

custo_alcool = custo (vm, tp, ra, pa)
print (f"Custo usando alcool (R$): {custo_alcool:.2f}")