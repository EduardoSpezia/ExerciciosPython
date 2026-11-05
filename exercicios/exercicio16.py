num = 1
somaPos = 0
somaNeg = 0
somaTotal = 0
numImp = "0"
numPar = "0"

while num != 0:
    num = int(input("Digite um número"))
    if num % 2 == 0 and num != 0:
        numPar += " " + str(num)
        if num > 0:
            somaPos += num
        else:
            somaNeg += num
    else:
        numImp += " " + str(num)
        if num < 0:
            somaNeg += num
        else:
            somaPos += num
    somaTotal = somaPos + somaNeg
print("Soma total dos números:", somaTotal,"\nSoma dos positivos:", somaPos,"\nSoma dos negativos:", somaNeg,"\nTodos números pares:", numPar,"\nTodos os números impares:", numImp)