# Exercício 1 – Primeira e Última Letra
# Peça ao usuário para digitar uma palavra. Mostre:
# A primeira letra
# A última letra

palavra = input("Digite uma palavra: ")
primeira_letra = palavra[0]
ultima_letra = palavra[-1]
print(f"Sua palavra foi {palavra}, a primeira letra é {primeira_letra} e a última é {ultima_letra}")