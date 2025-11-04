# Exercício 2 – Verificador de evento
# Peça ao usuário que digite uma data de um evento
# Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

from datetime import datetime

evento_data = input("Digite a data do evento (dd/mm/aaaa): ")
evento_data = datetime.strptime(evento_data, "%d/%m/%Y")
hoje = datetime.now()

evento_aconteceu = (hoje - evento_data).days
evento_acontecendo = hoje.date() == evento_data.date()
dias_faltando = (evento_data - hoje).days

if evento_aconteceu > 0:
    print(f"O evento já aconteceu há {evento_aconteceu} dias!")
elif evento_acontecendo:
    print(f"O evento está acontecendo hoje dia {hoje.strftime('%d/%m/%Y')}!")
elif dias_faltando > 0:
    print(f"O evento ainda vai acontecer, e faltam {dias_faltando} dias para ser iniciado!")