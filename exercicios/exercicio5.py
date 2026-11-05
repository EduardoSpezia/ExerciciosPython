num = int(input("Digite o número: "))
mediaPar = 0
numPar = 0
contador = 0

while num > 0:
    if num % 2 == 0:
        contador += 1
        numPar += num
        mediaPar = numPar / contador
        num = int(input("Digite um número: "))
    elif num % 2 != 0:
        num = int(input("Digite um número: "))
print("A média dos números pares é:", mediaPar)