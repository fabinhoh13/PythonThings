x = 30.0 # Definimos o valor de X como 30
expo = 3 # Esse valor será o expoente presente no dividendo e o numero a ser fatorado no divisor 
res = x # é aqui onde será guardado o resultado do somatório, já iniciado com o primeiro valor, que é x

# fazemos um for para ir de 1 até 100, sendo as 100 primeiras parcelas do somatório
for i in range (1, 100):
    # Primeiro, resolvemos o dividendo, tirando a potenciação de x por um numero impar iniciado por 3
    pot = x ** expo

    # Agora faremos o divisor, que é um fatorial
    # Para isso, vamos fazer um while que tira o fatorial do número definido
    fat = 1.0
    j = 2
    while j <= expo:
        fat = fat*j
        j += 1

    # Com o dividendo e o divisor prontos, agora temos que fazer o somatório propriamente dito
    # Faremos subtração, pois como já colocamos o primeiro elemento do somatório no inicio do programa, agora 
    # temos que subtrair
    res -= pot / fat
    # E para que possamos trocar o sinal, multiplicamos o resultado por -1
    res *= -1
    # Para que o expoente sempre seja um numero impar, somamos 2 a cada iteração
    expo += 2
    
# No final, printamos o resultado na tela
print (f"Sen(30) = {res}")