avaliacao = 0
idade = 0
qtdBom = 0
qtdExcelente = 0
qtdPessimo = 0
somaIdade = 0
mediaExcelente = 0
porcentagemBom = 0

for contador in range(0,4):
    avaliacao = int(input("1 = péssimo 2 = regular 3 = bom 4 = excelente \nInsira a sua avaliação: "))
    idade = int(input("Insira a sua idade: "))

    if avaliacao == 1:
        qtdPessimo += 1
    elif avaliacao == 3:
        qtdBom += 1
        porcentagemBom = qtdBom / 40
    elif avaliacao == 4:
        qtdExcelente += 1
        somaIdade += idade
        mediaExcelente = somaIdade / qtdExcelente
print("Quantidade de pessoas que avaliaram como péssimo: ",qtdPessimo)
print("Porcentagem de pessoas que avaliaram como bom: ",porcentagemBom)
print("Média da idade de pessoas que avaliaram como excelente: ",mediaExcelente)