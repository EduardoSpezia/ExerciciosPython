import random
vencedor = False
pontosP1 = 0
pontosP2 = 0

while vencedor == False:
    ponto = int(input("Insira o jogador que marcou o ponto: "))
    if ponto == 1:
        pontosP1 += 1
        print("Jogador 1 marcou 1 ponto \nTotal de pontos do jogador 1:", pontosP1)
        if pontosP1 >= 21 and pontosP1 - pontosP2 >= 2:
            vencedor = True
            print("Jogador 1 é o vencedor \nPontos jogador 1:", pontosP1, "\nPontos jogador 2:", pontosP2)
    else:
        pontosP2 += 1
        print("Jogador 2 marcou 1 ponto \nTotal de pontos do jogador 2:", pontosP2)
        if pontosP2 >= 21 and pontosP2 - pontosP1 >= 2:
            
            vencedor = True
            print("Jogador 2 é o vencedor \nPontos jogador 2:", pontosP2, "\nPontos jogador 1:", pontosP1)
    
    