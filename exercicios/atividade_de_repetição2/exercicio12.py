codigo = 1
alimentoNaopere = 0
alimentoPere = 0
vestuario = 0
higienePessoal = 0
limpezaUten = 0

while codigo != 0:
    codigo = int(input("Digite o código do produto:"))
    match codigo:
        case 1:
            alimentoNaopere += 1
        case 2 | 3 | 4:
            alimentoPere += 1
        case 5 | 6:
            vestuario += 1
        case 7:
            higienePessoal += 1
        case 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
            limpezaUten += 1
        case _:
            print("ERRO!")
print("Quantidade de alimentos não perecíveis: ", alimentoNaopere, "\nQuantidade de alimentos perecíveis: ", alimentoPere, "\nQuantidade de vestuário: ", vestuario, "\nQuantidade de higiene pessoal: ", higienePessoal, "\nQuantidade de limpeza e utensílios domésticos: ", limpezaUten)