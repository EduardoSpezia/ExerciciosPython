nome = " "
sexo = " "
homem = 0
mulher = 0

for contador in range(56):
    nome = input("Insira seu nome: ")
    sexo = input("Insira Homem ou Mulher: ")

    if sexo == "Homem":
        homem += 1
    else:
        mulher += 1

print("A quantidade de mulheres foi de:",mulher)
print("A quantidade de homens foi de:",homem)