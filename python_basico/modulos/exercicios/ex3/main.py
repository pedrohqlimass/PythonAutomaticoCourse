# Desafio 3 – Mini sistema de perfil de usuário
# Estrutura esperada:
# perfil/
# ├── usuario.py
# ├── validacao.py
# main.py

# usuario.py → função criar_perfil(nome, idade) → retorna dicionário com os dados
# validacao.py → função idade_valida(idade) → retorna True se idade >= 18

# main.py →
# Recebe os dados do usuário
# Valida a idade
# Se for válida, cria e exibe o perfil
# Senão, exibe uma mensagem de acesso negado

from perfil.usuario import criar_perfil
from perfil.validacao import idade_valida

nome_usuario = input("Digite o seu nome: ")
idade_usuario = int(input("Digite sua idade: "))

if idade_valida(idade_usuario):
    perfil = criar_perfil(nome_usuario, idade_usuario)
    print(f"Acesso liberado para {nome_usuario}")
else:
    print("Acesso negado! você tem menos de 18 anos.")