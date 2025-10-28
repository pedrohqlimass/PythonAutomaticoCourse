# def saudacao():
#     print("Olá, Seja bem vindo")

# nome = input("Digite seu nome: ")
# def saudacao(nome):
#     print(f"Olá {nome}! Seja bem vindo")
# saudacao(nome)

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     print(f"O resultado da soma entre {numero1} e {numero2} é {resultado}")
# somar(6, 8)
# somar(2, 90)
# somar(87, 10)

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado
# print(somar(5, 5))

def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final
print(calcular_desconto(200, 10))