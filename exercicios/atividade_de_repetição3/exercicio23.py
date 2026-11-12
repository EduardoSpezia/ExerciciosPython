formaPag = 0
totalPrazo = 0
totalVista = 0
valorTotal = 0
primeiroPrazo = 0
valor = 0

for contador in range(15):
    formaPag = int(input("Insira 1 para pagamento à vista \nInsira 2 para pagamento a prazo \nInsira a forma de pagamento:"))
    valor = int(input("Insira o valor da compra: "))
    if formaPag == 1:
        totalVista += valor
    if formaPag == 2:
        totalPrazo += valor
        primeiroPrazo = valor / 3
        print("O valor da primeira prestação será de:",primeiroPrazo)
    valorTotal = totalPrazo + totalVista

print("O valor total de pagamento à vista foi de:",totalVista)
print("O valor total de pagamento a prazo foi de:",totalPrazo)
print("O valor total de pagamento foi de:",valorTotal)
