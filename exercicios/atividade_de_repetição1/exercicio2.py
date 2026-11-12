num = int(input("Insira o número que será feita a tabuada: "))
ultiNum = int(input("Insira até qual número ira a tabuada: "))

for contador in range (1, ultiNum + 1):
    tabuada = num * contador
    print(tabuada)  