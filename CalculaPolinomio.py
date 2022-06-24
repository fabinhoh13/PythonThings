from biblioteca import *

grau = int (input ("Qual o grau do polinomio: "))

A = inputVetor ("Polinomios: ", float)

x = float (input ("Qual o valor de x? "))

Px = 0
for i in range (grau + 1):
    Px += A[i] * (x ** i)

print ("Resultados")

print (f"Valor de P({x}): {Px:.6f}")