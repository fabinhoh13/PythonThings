print ("1 - Celsius para Fahreinheit\n2 - Fahreinheit para Celsius")
opcao = int (input("Informe a opção: "))

if opcao == 1:
    tc = float (input ("Informe a temperatura em Celsius: "))
    tf = (9 * ( tc/5)) + 32
    print (f"A temperatura em Fahreinheit é: {tf:.2f}")
elif opcao == 2:
    tf = float (input ("Informe a temperatura em Fahreinheit: "))
    tc = ((tf - 32) / 9) * 5
    print (f"A temperatura em Celsius é : {tc:.2f}")
else:
    print ("Opção Inválida")