qtdAlunos = int (input ("Quantidade de alunos: "))
qtdDisciplinas = int (input ("Quantidade de disciplinas: "))
print ()
alunos = []
for i in range (qtdAlunos):
    print (f"Dados do aluno {i + 1}:")
    aluno = {}
    disciplinas = []
    for j in range (qtdDisciplinas):
        print (f" - Dados da disciplina {j + 1}:")
        disciplina = {}
        disciplina["nota"] = float (input ("  - Nota: "))
        disciplina["freq"] = int (input ("  - Frequência: "))
        disciplinas.append(disciplina)
    aluno["disciplinas"] = disciplinas
    alunos.append(aluno)
    print ()
    
maiores = []
for i in range (qtdAlunos):
    maior = 0
    for j in range (qtdDisciplinas):
        if alunos[i]["disciplinas"][j]["nota"] > alunos[i]["disciplinas"][maior]["nota"]:
            maior = j
    maiores.append(maior)
    
print ("Dados das disciplinas com maiores notas:")
for i in range (qtdAlunos):
    print (f" - Aluno {i + 1}: nota = {alunos[i]['disciplinas'][maiores[i]]['nota']:.1f}; frequencia = {alunos[i]['disciplinas'][maiores[i]]['freq']}")