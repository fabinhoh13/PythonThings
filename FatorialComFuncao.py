def Fatorial (n):
    fat = 1
    i = 1
    print (f"{i} = {fat}")
    while i <= n:
        fat = fat * i
        print (f"{i} = {fat}")
        i = i + 1
        
    return fat

#-------------------------------------------------------

n = int (input ("Informe o número que deseja calcular o Fatorial: "))

while n <= 0:
    n = int (input ("Número inválido, defina outro: "))

retorno_fatorial = Fatorial (n)

print (f"O Fatorial de 5 é: {retorno_fatorial}")