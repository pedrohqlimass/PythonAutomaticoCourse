# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

nota_teste = 6
nota_usuario = float(input('Qual foi sua nota no teste? '))

if nota_usuario >= nota_teste:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado')