num = 0
numCerto = 0

while numCerto == False:

    num = int(input("Insira um número:"))

    if num > 80 or num < 25 or num == 40:
        print("Parabéns! Este era um dos número escolhidos")
        numCerto = True
    else:
        print("Tente novamente!")