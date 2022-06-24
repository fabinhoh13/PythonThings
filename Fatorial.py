import math

def fatorial (x):
    fat = 1
    i = 1
    while i <= x:
        fat = fat * i
        i = i + 1
    return fat

n = int (input ("Informe o número de parcelas: "))
while n <= 0:
    n = int (input ("Valor inválido. Informe o número de parcelas: "))

x = 50
y = -80

i = 1
xi = 1
yi = 1
sinal = 1
total = 0

while i <= n:
    total += ((xi * x) - (yi * y)*sinal) / fatorial (i)
    sinal = sinal * -1
    xi = xi + 2
    yi = yi + 6
    i += 1
    #i += 1
    
print (f"Valor do somatório com {n} parcelas: {total:.2f}")

    
    