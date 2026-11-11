idade = 0
opniao = 0
quantidadeRegular = 0
quantidadeBom = 0
porcentagemBom = 0
somaIdade = 0

for contador in range(15):
    idade = int(input("Insira a sua idade: "))
    opniao = int(input("1 = regular 2 = bom 3 = ótimo \nInsira qual a sua opnião do filme: "))
    if opniao == 3:
        somaIdade += idade
    elif opniao == 2:
        quantidadeRegular += 1
    else:
        quantidadeBom += 1
        porcentagemBom = (quantidadeBom / 15) * 100

print("A soma da idade das pessoas que responderam ótimo são:",somaIdade)
print("A quantidade de pessoas que responderam regular são:",quantidadeRegular)
print("A porcentagem de pessoas que responderam bom são:",porcentagemBom)