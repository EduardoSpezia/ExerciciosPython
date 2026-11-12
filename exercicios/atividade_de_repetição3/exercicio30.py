qtdMulti = 0
somaPar = 0

for contador in range(0,10):
    num = int(input("Insira o número: "))
    if num % 3 == 0:
        qtdMulti += 1
    if num % 2 == 0:
        somaPar += num
print("Quantidades de números que são multiplos de 3: ",qtdMulti)
print("Soma de todos os números pares: ",somaPar)