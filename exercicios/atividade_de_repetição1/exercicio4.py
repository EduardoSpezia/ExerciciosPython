salario = 0 
salario100 = 0
mediaSalario = 0
qtdSalario = 0
numFilhos = 0
mediaFilhos = 0
qtdFilhos = 0
maiorSalario = 0
contador = 0

while salario >= 0:
    salario = float(input("Digite o sálario:"))
    if salario > 0: 
        contador += 1
        qtdSalario += salario
        mediaSalario = qtdSalario / contador 
        numFilhos = int(input("Digite a quantidade de filhos:"))
        qtdFilhos += numFilhos
        mediaFilhos = qtdFilhos / contador  
        if salario < 100:
            salario100 += 1
        elif salario > mediaSalario:
            maiorSalario = salario
perc100 = ((100 * salario100) / qtdSalario)
print("Média dos sálarios: R$",mediaSalario, "\nMaior sálario: R$",maiorSalario, "\nMédia de filhos:", mediaFilhos, "\nPercentual de sálarios abaixo de R$100:", perc100, "%")