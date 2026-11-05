numIni = int(input("Insira o número em que irá começar: "))
intervalo = int(input("Insira o intervalo: "))

for contador in range (numIni, -1, -intervalo):
    print(contador)
    