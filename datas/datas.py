from datetime import datetime

# agora = datetime.now()
# # print(f"Hoje é dia {agora.day} do mês {agora.month} de {agora.year}")
# print(agora.strftime("Hoje é dia %d do mês %m de %Y"))
# print(agora.strftime("Agora são %H horas e %M minutos"))

# print(agora.day)
# print(agora.month)
# print(agora.year)
# print(agora.hour)
# print(agora.minute)
# print(agora.second)
# print(agora.microsecond)

# aniversario = datetime(2006, 8, 21)
# print(aniversario.day)

data_str = "20/04/2025"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
print(data_convertida)