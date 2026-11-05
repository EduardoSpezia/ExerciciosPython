import random

numero = random.randint(1,50)
print(numero)
for contador in range (5):
    num = int(input("Digite um valor: "))
    if num == numero:
        print("Acertou")
        break
    elif num > numero:
        print("O número é menor, TENTE NOVAMENTE!")
    elif num < numero:
        print("O número é maior, TENTE NOVAMENTE!")
print("O número era:", numero)a