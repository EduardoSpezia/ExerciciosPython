canal = 1
pessoas = 0
soma12 = 0
soma4 = 0
soma5 = 0
soma7 = 0
somaTotal = 0
porcen12 = 0
porcen4 = 0
porcen5 = 0
porcen7 = 0

while canal != 0:
    canal = int(input("Insira o canal em que estava sendo assistido: "))
    match canal:
        case 4:
            pessoas = int(input("Insira a quantidade de pessoas que estavam assistindo: "))
            soma4 += pessoas
        case 5:
            pessoas = int(input("Insira a quantidade de pessoas que estavam assistindo: "))
            soma5 += pessoas
        case 7:
            pessoas = int(input("Insira a quantidade de pessoas que estavam assistindo: "))
            soma7 += pessoas
        case 12:
            pessoas = int(input("Insira a quantidade de pessoas que estavam assistindo: "))
            soma12 += pessoas

somaTotal = soma4 + soma12 + soma5 + soma7
porcen4 = (soma4 / somaTotal) * 100
porcen5 = (soma5 / somaTotal) * 100
porcen7 = (soma7 / somaTotal) * 100
porcen12 = (soma12 / somaTotal) * 100
    print("Porcentagem de pessoas que estavam assistindo o canal 4:", porcen4,"\nPorcentagem de pessoas que estavam assistindo o canal 5:", porcen5,"Porcentagem de pessoas que estavam assistindo o canal 7:", porcen7,"Porcentagem de pessoas que estavam assistindo o canal 12:", porcen12)