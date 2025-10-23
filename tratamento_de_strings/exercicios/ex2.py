# Exercício 2 – Pegando um trecho da frase
# Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

frase = input("Digite sua frase ou palavra: ")
inicio = int(input("Digite o índice de início: "))
fim = int(input("Digite o índice do fim: "))
fatiamento = frase[inicio:fim]
print(fatiamento)