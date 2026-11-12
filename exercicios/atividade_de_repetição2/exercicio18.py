pagamento = input("Insira a forma de pagamento:")
preco = int(input("Insira o valor do carro: "))

if pagamento == "à vista" or pagamento == "À vista":
    precoFinal = preco * 0.8
    print("O preço final é: ",precoFinal)
elif pagamento == "parcelado" or pagamento == "Parcelado":
    parcelas = int(input("Insira a quantidade de parcelas: "))
    precoFinal = preco * (1 + (parcelas / 200))
    valorParcela = precoFinal / parcelas
    print("O preço final é:", precoFinal, "\nA quantidade de parcelas:", parcelas, "\nO valor de cada parcela é: ",valorParcela)