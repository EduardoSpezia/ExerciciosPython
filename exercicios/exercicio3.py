num = int(input("Digite um número: "))
numNeg = 0

while num != 0:
    if num < 0:
        numNeg += 1
    num = int(input("Digite um número: "))
print("Você digitou", numNeg, "número negativos")