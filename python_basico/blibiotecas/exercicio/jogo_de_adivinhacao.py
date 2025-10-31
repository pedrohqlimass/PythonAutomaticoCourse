# Exercício – Jogo de Adivinhação 🎯
# Crie um programa que sorteia um número inteiro entre 1 e 10 usando a biblioteca random.
# O jogador tem que tentar adivinhar esse número.
# O jogo deve continuar perguntando até o jogador acertar.
# A cada tentativa, o programa deve informar:
# "Muito alto!" se o palpite for maior que o número sorteado
# "Muito baixo!" se for menor
# "Acertou!" se for igual
# Ao final, informe quantas tentativas foram necessárias para acertar.

from random import randint

tentativas = 0
numero_aleatorio = randint(1, 10)
print(f"===== Seja bem vindo ao Jogo de Adivinhação!=====\n- Será sorteado aleatoriamento um número de 1 a 10 e você terá que adivinhar!\n{'='*77}")

while True:
    try:
        numero_digitado_usuario = int(input("Digite um número de 1 a 10: "))
    except ValueError:
        print("Digite apenas número!\n")
        continue
    tentativas+=1
    if numero_digitado_usuario == 0 or numero_digitado_usuario > 10:
        print("Número inválido. Digite um número de 1 a 10.\n")
        continue
    if numero_digitado_usuario == numero_aleatorio:
        print(f"Você acertou! O número é {numero_aleatorio}")
        break
    elif numero_digitado_usuario > numero_aleatorio:
        print("o chute foi alto!")
    elif numero_digitado_usuario < numero_aleatorio:
        print("o chute foi baixo!")
print(f"Você acertou com {tentativas} tentativas!")