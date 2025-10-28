# Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
# Depois, verifique se a idade é maior ou igual a 18:
# Se sim, imprima: "Acesso liberado para {nome}"
# Se não, imprima: "Acesso negado para {nome}"

usuario = {
    "nome": input("Digite um nome: "),
    "idade": int(input("Digite uma idade: "))
}

if usuario["idade"] >= 18:
    print(f"Acesso liberado para {usuario['nome']}")
else:
    print(f"Acesso negado para {usuario['nome']}")

print(usuario)