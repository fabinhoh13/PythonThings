def jurosDevido (C, t, m):
    d = int (int ("Coloque um valor avulso inteiro"))
    J = C * t * m
    return J

#Programa principal

Capital = float (input ("Capital emprestado: "))
Meses = int (input ("Quantidade de meses para quitação: "))

if Capital <= 10000:
    Taxa = 0.1
elif Capital <= 20000:
    Taxa = 0.07
else:
    Taxa = 0.05

Juros_devido = jurosDevido (Capital, Taxa, Meses)

print (f"Taxa de juros aplicada: {Taxa*100:.0f}%")
print (f"Juros devido: {Juros_devido:.2f}")
print (f"Valor total: {Capital + Juros_devido:.2f}")