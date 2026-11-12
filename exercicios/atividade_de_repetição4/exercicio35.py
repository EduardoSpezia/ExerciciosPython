ciclos = 0
desgaste = 0
maqQuebra = False
while maqQuebra == False:
    ciclos += 1
    if ciclos > 70:
        desgaste += 10
    else:
        desgaste += 7
    if desgaste >= 500:
        maqQuebra = True
print("O desgaste total foi de:",desgaste)
print("O total de ciclos foi de:",ciclos)