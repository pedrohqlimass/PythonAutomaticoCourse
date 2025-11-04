# Exercício 3 – Validade de produto 🥫
# Peça ao usuário para informar a data de fabricação de um produto.
# Considere que ele vence em 180 dias.
# Mostre:
# A data de validade
# Se o produto ainda está válido ou já venceu
# Quantos dias faltam ou há quanto tempo passou do prazo

from datetime import datetime, timedelta

data_fabricacao = input("Digite a data de fabricação do produto (dd/mm/aaaa): ")
data_fabricacao = datetime.strptime(data_fabricacao, "%d/%m/%Y")
hoje = datetime.now()
data_vencimento = timedelta(days=180)
data_validade = data_fabricacao + data_vencimento

print(f"Hoje é: {hoje.strftime('%d/%m/%Y')}")
print(f"Data de vencimento do produto: {data_validade.strftime('%d/%m/%Y')}")

if data_validade.date() > hoje.date():
    print("O produto ainda está válido!")
elif data_validade.date() < hoje.date():
    print("O produto está vencido!")
else:
    print("O produto vence hoje!")