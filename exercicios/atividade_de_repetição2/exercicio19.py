contador = 0

while contador < 150:
    contador += 1
    valorCompras = int(input("Insira o valor das compras do cliente: "))
    nomeCliente = input("Insira o nome do cliente: ")
    if valorCompras < 500000:
        valorFinal = valorCompras * 0.90
        print(nomeCliente, "parabéns! O valor final da sua compra ficou em:", valorFinal)
    else:
        valorFinal = valorCompras * 0.85
        print(nomeCliente, "parabéns! O valor final da sua compra ficou em:", valorFinal)