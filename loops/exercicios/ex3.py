# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
# Quando o usuário digitar 0, o programa para e mostra o total economizado.

dinheiro_guardado = 0.0
while True:
    valor = float(input("Digite um valor em reais (0 para sair do programa): "))
    if valor == 0:
        break
    dinheiro_guardado += valor
print(f"Total de dinheiro guardado: R${dinheiro_guardado:.2f}")
