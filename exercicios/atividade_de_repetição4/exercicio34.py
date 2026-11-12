temperatura = int(input("Insira a temperatura inicial do forno industrial: "))
ciclos = 0
while temperatura < 1000:
    ciclos += 1
    if temperatura < 800:
        temperatura += 50
    elif temperatura >= 800 and temperatura < 1000:
        temperatura += 20
print("A temperatura final foi de:",temperatura)
print("O tanto de ciclos necessários foram:",ciclos)