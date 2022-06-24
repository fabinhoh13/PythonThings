import math #inclusão da biblioteca math para o uso da constante de Euler

sair = 'n'
vD = 0
while sair != "s" and sair != "S":
    T = float(input('Informe a temperatura (em Kelvin): '))
    print('Tensão | Corrente')
    for i in range(-10, 7, 1): #for indo de -10 até 6, para isso, incluimos 6 + 1
        vD = i / 10 #o valor de vD variando de -1 até 0.6. Para isso, só fiz a divisão do valor de i por 10
        I0 = 2*(10**(-6))
        q = 1.602*(10**(-19))
        k = 1.38*(10**(-23))
        iD = I0*(math.e**((q*vD)/(k*T))-1)
        #Inclusão da constante de Euler (math.e) na fórmula
        print(f'{vD:5.1f} | {iD:5.1f}')
        
    sair = input('Deseja sair? (s/S/n/n): ')
    while sair != 's' and sair != 'S' and sair != 'n' and sair != 'N':
        print('ERRO: opção inválida !')
        sair = input('Deseja sair? (s/S/n/n): ')
print('Fim do Programa !')      
        
    