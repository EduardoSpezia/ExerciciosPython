num = int(input("Digite um valor: "))

if num % 2 == 0:
    for contador in range (num, -1, -2):
        print(contador)
else:
    for contador in range (num - 1, -1, -2):
        print(contador)