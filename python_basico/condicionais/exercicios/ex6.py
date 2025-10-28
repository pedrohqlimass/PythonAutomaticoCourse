# Crie um menu com 3 opções:
# 1. Pizza
# 2. Sushi
# 3. Salada
# O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválida."

opcao = int(input("Bem Vindo!\n Digite:\n1. Pizza\n2. Sushi\n3. Salada\n"))
match opcao:
    case 1:
        print("Você escolheu Pizza!")
    case 2:
        print("Você escolheu Sushi!")
    case 3:
        print("Você escolheu Salada!")
    case _:
        print("Opção inválida.")