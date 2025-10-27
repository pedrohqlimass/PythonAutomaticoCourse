# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

# soma = 0
# for n in range(5):
#     numero = int(input("Digite um número: "))
#     soma += numero
# print(f"Soma dos números: {soma}")

# soma = 0
# contador = 0

# while contador < 5:
#     numero = int(input("DIgite um número: "))
#     soma += numero
#     contador+=1
# print(f"Soma total dos número digitados: {soma}")

#correção da aula
numeros = []
for n in range(1, 6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

resultado = 0
for numero in numeros:
    resultado += numero

print(f"O resultado é {resultado}")