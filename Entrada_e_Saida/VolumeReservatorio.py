import math

raio = float (input ("Digite o raio do reservatório de combustível: "))
altura = float (input ("Digite a altura do reservatório de combustível: "))

capacidade = float (input ("Digite a capacidade (m3) de armazenamento de comb. dos caminhões: "))

a = math.pi * raio ** 2

v = a * altura

quantidade = v / capacidade

print (f"O volume do reservatório é {v:.3f} m3.")
print (f"{quantidade:.0f} caminhões poderiam ser abastecidos com este reservatório.")