def inputVetor(mensagem, conversao):
    valores = input(mensagem)
    resultado = [ ]
    if valores == "":
        return resultado
    valores = valores.split(',')
    for i in range(len(valores)):
        valor = conversao(valores[i].strip())
        resultado.append(valor)
    return resultado

maior = 0
menor = 99999999999999999999999999
v = inputVetor("Digite: ", int)


for i in range (len(v)):
    if v[i] > maior:
        maior = v[i]
    
    if v[i] < menor:
        menor = v[i]
    print (f"{v[i]}", end=" ")
print ("\nResultado: ")
print (len(v))
print (maior)
print (menor)