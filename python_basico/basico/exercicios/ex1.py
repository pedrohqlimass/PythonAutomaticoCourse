# Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.

ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
resultado = ano_atual - ano_nascimento

print(f'Você tem {resultado} anos de idade')