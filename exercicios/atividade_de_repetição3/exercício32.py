maiorTemp = 0
ciclo = 0
tempValida = 0
temperatura = 0
somaTemp = 0

while somaTemp < 999:
    ciclo += 1
    temperatura = int(input("Insira a temperatura: "))
    if temperatura > -50 and temperatura < 150:
        if temperatura > 20 and temperatura < 80:
            if temperatura % 5 == 0:
                if temperatura % 10 != 0:
                    tempValida += 1
                    somaTemp = somaTemp + temperatura
                    if temperatura > maiorTemp:
                        maiorTemp = temperatura
percentualValido = (tempValida / ciclo) * 100

print("Quantidade válida:", tempValida,"\nMaior temperatura válida:",maiorTemp,"\nPercentual de temperaturas válidas sobre total digitado:", percentualValido)