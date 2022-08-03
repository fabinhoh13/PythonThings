# Farei a entrada de 5 valores
n = 5

#Crio uma variável com o maior valor possível
menor = 999999999999999999
#crio meu contador para contar as iterações (loops)
i = 1
#entro no meu while
while i < n:
    #Faço a entrada de n valores
    x = int (input (f"Digite o {i}o valor: "))
    #Caso esse valor for menor que o valor que está dentro da variável "menor"
    if x < menor:
        #Então esse valor recebido na linha 11 é colocado dentro da variável "menor"
        #Sendo assim, esse valor passa a ser o menor
        menor = x
        #Dessa forma, a cada entrada que obtivermos, sempre que ele for o menor
        #Ele será guardado, para que quando terminarmos todas as entradas
        #Teremos o menor valor dentre todos
    #Andamos com o iterador
    i+=1
    
#E ao final do while, printamos qual o menor valor que encontramos
print (menor)