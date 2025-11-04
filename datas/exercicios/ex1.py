# Exercício 1 – Relógio de verificação
# Mostre a hora_atual atual no terminal, mas com a seguinte regra:
# Se a hora_atual for antes das 12h, imprima: "Bom dia!"
# Se estiver entre 12h e 18h: "Boa tarde!"
# Depois disso: "Boa noite!"

from datetime import datetime

# hora = hora_atual.hour
def verificar_horario():
    hora_atual = datetime.now().hour
    if hora_atual >= 3 and hora_atual < 12:
        print(f"Bom dia!")
    elif hora_atual >= 12 and hora_atual <= 18:
        print(f"Boa tarde!")
    else:
        print(f"Boa noite!")
    if hora_atual == 1:
        print(f"Agora é {hora_atual} hora")
    else:
        print(f"Agora são {hora_atual} horas")

verificar_horario()