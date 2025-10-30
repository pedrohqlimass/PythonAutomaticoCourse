# Desafio 1 – Separando funções por categoria
# Crie um arquivo matematica.py com as funções:
# dobro(numero) → retorna o dobro
# metade(numero) → retorna a metade

# Crie outro arquivo mensagens.py com a função:
# boas_vindas(nome) → imprime uma mensagem de saudação

# No arquivo principal (main.py):
# Importe as funções dos dois arquivos
# Peça ao usuário um número e mostre o dobro e a metade
# Dê boas-vindas usando o nome digitado



from matematica import dobro, metade
from mensagens import boas_vindas

nome_usuario = input("Digite o seu nome: ")
boas_vindas(nome_usuario)

n_dobro = float(input("Digite um número para ver o dobro dele: "))
print(f"O dobro de {n_dobro} é {dobro(n_dobro)}")

n_metade = float(input("Digite um número para ver a metade dele: "))
print(f"A metade de {n_metade} é {metade(n_metade)}")