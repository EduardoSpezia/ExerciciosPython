salarioTotal = 0
salarioAdmin = 0
salarioOpe = 0
qtdAdmin = 0 
qtdOpe = 0 
mediaAdmin = 0
mediaOpe = 0
codigo = 0

for contador in range(0,5):
    codigo = int(input("Insira o código do seu setor: "))
    salario = int(input("Insira o seu sálario: "))
    salarioTotal += salario

    if codigo == 1:
        qtdAdmin += 1
        salarioAdmin += salario
        mediaAdmin = salario / qtdAdmin

    else:
        qtdOpe += 1
        salarioOpe += salario
        mediaOpe = salario / qtdOpe

print(" _______________________________________")
print("|          Setor Administrativo         |")
print("|_______________________________________|")

print("Quantidade de pessoas: ",qtdAdmin)
print("Média salarial:",mediaAdmin)

print(" _______________________________________")
print("|           Setor Operacional           |")
print("|_______________________________________|")

print("Quantidade de pessoas: ",qtdOpe)
print("Média salarial:",mediaOpe)

print(" _______________________________________")
print("|               Empresa                 |")
print("|_______________________________________|")


print("Total de sálarios pagos na empresa:",salarioTotal)