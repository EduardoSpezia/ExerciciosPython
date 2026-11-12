divida = int(input("Insira o valor da dívida: "))
parcelas = int(input("Insira a quantidade de parcelas: "))

if parcelas == 1:
    print(divida, "0", parcelas, divida)
elif parcelas == 3:
    juros = divida * 0.10
    dividaFinal = divida + juros
    valorParcela = dividaFinal / 3
    print(divida, juros, parcelas, valorParcela)
elif parcelas == 6:
    juros = divida * 0.15
    dividaFinal = divida + juros
    valorParcela = dividaFinal / 6
    print(divida, juros, parcelas, valorParcela)
elif parcelas == 9:
    juros = divida * 0.20
    dividaFinal = divida + juros
    valorParcela = dividaFinal / 9
    print(divida, juros, parcelas, valorParcela)
elif parcelas == 12:
    juros = divida * 0.25
    dividaFinal = divida + juros
    valorParcela = dividaFinal / 12
    print(divida, juros, parcelas, valorParcela)