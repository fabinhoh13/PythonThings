from biblioteca import *
#Inicializo um contador com o valor 0
contador = 0
#crio um vetor de 10 posições com o valor padrão de 5
vetor1 = criarVetor (10, 5)
#percorro meu vetor
for i in range (len(vetor1)):
    #imprimo na tela cada valor dentro do meu vetor
    print (vetor1[i])
    #e acumulo esse valor dentro do meu contador
    contador += vetor1[i]
#depois imprimo o valor final do contador
print ("\n", contador)


#Crio um vetor de 10 posições, onde todas as posições são inciadas com 0
vetor2 = criarVetor (10, 0)

#percorro o meu vetor
for i in range (len(vetor2)):
    #e para cada posição, eu acumulo o valor que tem em i acrescido de +1
    vetor2[i] += i + 1

#Faço a impressão do meu vetor resultante
print (vetor2)