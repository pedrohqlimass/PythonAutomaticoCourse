# Crie pizza sistema de votação onde o usuário escolhe entre:
# 1."Pizza"
# 2."Hambúrguer"
# 3."Sair"
# Enquanto ele não digitar "3", continue perguntando
# No final, mostre quantos votos cada item recebeu

pizza = 0
hamburguer = 0

while True:
    opcao = int(input("Digite uma opção: \n 1. Pizza \n 2. Hambúrguer \n 3. Sair \n"))
    match opcao:
        case 1:
            print("+1 voto para Pizza")
            pizza+=1
        case 2:
            print("+1 voto para Hambúrguer")
            hamburguer+=1
        case 3:
            break
        case _:
            print("Opção inválida.")
soma_votos = pizza + hamburguer
print(f"Total de votos: {soma_votos}\n{pizza} votos para Pizza\n{hamburguer} votos para Hambúrguer")