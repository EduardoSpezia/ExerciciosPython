encerrar = False
codigo = 0
valor = 0.0
valorTotal = 0.0
quantidade = 0
continuar = " "

while encerrar == False:
    codigo = int(input("Insira o código do produto: "))
    if codigo == 100:
        quantidade = int(input("Insira a quantidade de cachorro quente que você deseja: "))
        valor = quantidade * 1.20
        print("O valor dos cachorro quentes serão: R$",valor)
    if codigo == 101:
        quantidade = int(input("Insira a quantidade de bauru simples que você deseja: "))
        valor = quantidade * 1.30
        print("O valor dos bauru simples serão: R$",valor)
    if codigo == 102:
        quantidade = int(input("Insira a quantidade de bauru com ovo que você deseja: "))
        valor = quantidade * 1.50
        print("O valor dos baurus com ovo serão: R$",valor)
    if codigo == 103:
        quantidade = int(input("Insira a quantidade de hambúrguer que você deseja: "))
        valor = quantidade * 1.20
        print("O valor dos hambúrgueres serão: R$",valor)
    if codigo == 104:
        quantidade = int(input("Insira a quantidade de chesseburguer que você deseja: "))
        valor = quantidade * 1.30
        print("O valor dos chesseburguer serão: R$",valor)
    if codigo == 105:
        quantidade = int(input("Insira a quantidade de refrigerante que você deseja: "))
        valor = quantidade * 1.00
        print("O valor dos refrigerantes serão: R$",valor)
    valorTotal += valor
    print("O total geral do pedido está em:",valorTotal)
    continuar = input("Você deseja continuar o pedidio? ")
    if continuar == "Não" or continuar == "não":
        encerrar == True
print("O valor total do pedidio ficou em:",valorTotal)