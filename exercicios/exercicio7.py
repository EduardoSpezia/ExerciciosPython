num = int(input("Digite um valor: "))
mediaNum = 0
contador = 0
numTotal = 0

while num > 0:
    if num > 0:
        contador += 1
        numTotal += num
        mediaNum = numTotal / contador
        num = int(input("Digite um valor: "))
print(mediaNum)