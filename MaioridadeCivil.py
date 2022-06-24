nome = input ("Digite o nome: ")
idade = float (input ("Digite a idade: "))
sexo = input ("Entre com o sexo (m ou f): ")

if sexo == 'f':
    if (idade >= 21):
        print (f"{nome} tem maioridade civil")
    else:
        faltam = 21 - idade
        print (f"Faltam {faltam:.1f} para {nome} atingir a maioridade civiil")
else:
    if (idade >= 18):
        print (f"{nome} tem maioridade civil")
    else:
        faltam = 21 - idade
        print (f"Faltam {faltam:.1f} para {nome} atingir a maioridade civiil")