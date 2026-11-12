paisA = int(input("Insira a população do país A: "))
paisB = int(input("Insira a população do país B: "))
anos = 0

while paisA < paisB:
    anos += 1
    paisA = paisA * 1.03
    paisB = paisB * 1.015
    if anos % 5 == 0:
        paisA = paisA * 0.93
        paisB = paisB * 0.93
print(anos,"Anos")