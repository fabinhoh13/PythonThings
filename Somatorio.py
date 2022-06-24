def fatorial (a):
    fat = 1
    i = 1
    while (i <= a):
        fat *= i
        i += 1
    return fat


n = int (input ("Digite o numero de parcelas: "))
while (n <= 0):
    n = int (input ("Valor inválivo para n. Digite novamente o numero de parcelas: "))

x = 50
y = -80
soma = 0
xa = 1
ya = 1
i = 1
sinal = -1
while (i <= n):
    soma += ((x * xa) - (sinal *(y * ya))) / fatorial (i)
    xa += 2
    ya += 6
    sinal *= -1
    
    i = i + 1
    
print (f"Valor do somatório com {n} parcelas: {soma:.2f}")