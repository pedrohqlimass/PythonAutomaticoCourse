# Crie um código onde o usuário deve inserir dois números e exiba a soma, subtração, multiplicação e divisão deles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número '))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f'A soma entre {num1} e {num2} é: {soma}')
print(f'A subtração entre {num1} e {num2} é: {subtracao}')
print(f'A multiplicação entre {num1} e {num2} é: {multiplicacao}')
print(f'A divisão entre {num1} e {num2} é: {divisao}')