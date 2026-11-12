nome = " "
nota = 0
notaTotal = 0
mediaGeral = 0.0
qtdAcima = 0

for contador in range(0,35):
    nome = input("Insira o nome do aluno: ")
    nota = int(input("Insira a nota do aluno: "))

    notaTotal += nota
    mediaGeral = notaTotal / 35

    if nota >= 7:
        qtdAcima += 1

print("Média geral da turma: ", mediaGeral)
print("Quantidade de alunos que tiraram acima de 7: ",qtdAcima)