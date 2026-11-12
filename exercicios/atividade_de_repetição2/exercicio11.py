numeroVeiculos = 0
numeroAcidentes = 0
somaTodasCidades = 0
menorAcidente = float('inf')
maiorAcidente = 0
contador = 0
cidadeMaior = 0
cidadeMenor = 0
somaSCVeiculos = 0
qtdSC = 0
somaSCAcidentes = 0
somaPRAcidentes = 0
somaPRVeiculos = 0
somaRSAcidentes = 0
somaRSVeiculos = 0
qtdPR = 0
qtdRS = 0

for contador in range (1,12):
    codigo = int(input("Digite o código da cidade: "))
    numeroVeiculos = int(input("Digite o número de veículos: "))
    numeroAcidentes = int(input("Digite o número de acidentes: "))

    if numeroAcidentes > maiorAcidente:
        maiorAcidente = numeroAcidentes
        cidadeMaior = codigo
    if numeroAcidentes < menorAcidente:
        menorAcidente = numeroAcidentes
        cidadeMenor = codigo

    somaTodasCidades += numeroVeiculos

    if codigo >= 11 and codigo <= 14:
        somaSCVeiculos += numeroVeiculos
        somaSCAcidentes += numeroAcidentes
        qtdSC += 1

    elif codigo >= 21 and codigo <=  24:
        somaRSVeiculos += numeroVeiculos
        somaRSAcidentes += numeroAcidentes
        qtdRS += 1
    
    elif codigo >= 31 and codigo <= 34:
        somaPRVeiculos += numeroVeiculos
        somaPRAcidentes += numeroAcidentes
        qtdPR += 1


print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
print("A média de veículos em SC é: ", (somaSCVeiculos / qtdSC))
print("A média de acidentes em SC é: ", (somaSCAcidentes / qtdSC))
print("A média de veículos em RS é: ", (somaRSVeiculos / qtdRS))
print("A média de acidentes em RS é: ", (somaRSAcidentes / qtdRS))