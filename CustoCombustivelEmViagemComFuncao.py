def Custo (v, t, r, p):
    c = ((v*t)/r)*p
    return c

velocidade_media = float (input("Velocidade Media (km/h): "))
tempo = float (input("Tempo Previsto(h): "))

rendimento_gasolina = float (input("Rendimento com gasolina\t(km/litro: "))
preco_gasolina = float (input("Preço do litro de gasolina\t(R$): "))
preco_alcool = float (input("Preço do litro de alcool\t(R$): "))

rendimento_alcool = rendimento_gasolina * 0.7

custo_gasolina = Custo (velocidade_media, tempo, rendimento_gasolina, preco_gasolina)
custo_alcool = Custo (velocidade_media, tempo, rendimento_alcool, preco_alcool)

print (f"\nCusto usando gasolina (R$): {custo_gasolina:.2f}")
print (f"Custo usando alcool (R$): {custo_alcool:.2f}")

