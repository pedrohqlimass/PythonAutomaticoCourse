# Exercício 3 – Assinatura digital do terminal
# Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:
# Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02
# A data e horário devem ser do momento atual da assinatura

from datetime import datetime


def gerar_assinatura(nome):
    agora = datetime.now()
    # print(f"Assinatura gerada por {nome} em {agora.day} de {agora.strftime("%B")} de {agora.year} às {agora.hour}:{agora.minute}")
    print(agora.strftime(f"Assinatura gerada por {nome} em %d/%m/%Y às %H:%M"))

nome_usuario = input("Digite seu nome: ")
gerar_assinatura(nome_usuario)