aluno = [ "Peny", "Rajesh Koothrappali", "Sheldon Cooper","Howard Wolowitz", "Leonard Hofstadter"]
notasBCC701 = [ 6.0, 8.5, 10.0, 9.0, 9.5 ]

nome = input ("Digite o nome do(a) aluno(a): ")
indice = -1
for i in range (len (aluno)):
    if (nome == aluno[i]):
        indice = i
if indice != -1:
    print ("Resultados:")
    print (f"Nome do(a) aluno(a) buscado(a): {aluno[indice]}")
    print (f"Nota: {notasBCC701[indice]}")
else:
    print ("Erro na busca, aluno(a) não encontrado(a) !")