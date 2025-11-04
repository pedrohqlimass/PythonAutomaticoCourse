# Exercício 2 – Quantos meses faltam?
# Crie um programa que exiba quantos meses faltam para o numero_meses acabar. 
# Exemplo:
# Hoje é o 4º mês do numero_meses. Ainda faltam 8 meses para terminar o numero_meses!

from datetime import datetime

# agora = datetime.now()
# mes_atual = agora.month
mes_atual = datetime.now().month
numero_meses = 12

def calcular_meses_restantes():
    meses_restantes = numero_meses - mes_atual
    if meses_restantes == 1:
        print(f"Estamos no {mes_atual}º mês do ano. Ainda falta {meses_restantes} mês para terminar o ano!")
    else:
        print(f"Estamos no {mes_atual}º mês do ano. Ainda faltam {meses_restantes} meses para terminar o ano!")

calcular_meses_restantes()