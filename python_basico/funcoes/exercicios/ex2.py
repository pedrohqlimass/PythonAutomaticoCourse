# Crie uma função chamada apresentar_pessoa(nome, idade) que exibe a seguinte mensagem:
# "Nome: <nome> | Idade: <idade> anos"
# Chame a função passando valores diferentes.

def apresentar_pessoa(nome, idade):
    print(f"Nome: {nome} | Idade: {idade}")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
apresentar_pessoa(nome, idade)