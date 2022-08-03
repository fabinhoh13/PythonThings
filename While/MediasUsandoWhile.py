import math

n = int (input ("Quantidade de números: "))
while (n <= 0):
    n = int (input ("ERRO! Quantidade de números: "))

i = 1
aritmetica = 0
geometrica = 1
while i <= n:
    print (f"Iteração {i}")
    x = float (input ("Digite um número real: "))
    while x <= 0:
        x = float (input ("ERRO! Digite um número real: "))
    aritmetica += x
    geometrica *= x
    
    i += 1

aritmetica /= n
geometrica = geometrica ** (1/n)

print ("Impressão dos Resultados:")
print (f"Média Aritmética: {aritmetica:.2f}")
print (f"Média Geométrica: {geometrica:.2f}")