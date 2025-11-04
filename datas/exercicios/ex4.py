# Exercício 1 – Contagem regressiva para o fim do ano
# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

from datetime import datetime

hoje = datetime.now()
fim_do_ano = datetime(2025, 12, 31)
tempo_restante = fim_do_ano - hoje

print(f"Faltam {tempo_restante.days} dias até o dia {fim_do_ano.strftime("%d/%m/%Y")}")