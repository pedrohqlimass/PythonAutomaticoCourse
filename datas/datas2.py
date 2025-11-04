from datetime import datetime, timedelta

# hoje = datetime.now()
# um_dia = timedelta(days=1)
# amanha = hoje + um_dia
# ontem = hoje - um_dia
# print(ontem)

# prazo = datetime(2025, 11, 4)
# hoje = datetime.now()
# if hoje > prazo:
#     print("Prazo vencido!")
# else:
#     print("Ainda está no prazo!")

# agora = datetime.now()
# futuro = datetime(2025, 11, 23)
# dias_restantes = futuro - agora
# print(dias_restantes.days)

aniversario = datetime(2025, 11, 3)
hoje = datetime.now()

if aniversario.day == hoje.day and aniversario.month == hoje.month:
    print("O aniversário é hoje!")
elif aniversario > hoje:
    print("O aniversário ainda vai acontecer!")
elif aniversario < hoje:
    print("O aniversário já passou!")
