num = 0
numIntervalo = 0

for contador in range(80):

    num = int(input("Escreva o número:"))
    if num >= 10 and num <= 150:
        numIntervalo += 1
print("A quantidade de números que estão entre 10 e 150 são: ",numIntervalo)    