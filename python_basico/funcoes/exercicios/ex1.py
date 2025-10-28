# Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.
# Depois, use a função com um valor recebido via input() e exiba o resultado com print().

def quadrado(numero):
    operacao = numero ** 2
    return operacao
numero_usuario = float(input("Digite um número para ver o quadrado dele: "))
print(f"{numero_usuario} elevado ao quadrado é {quadrado(numero_usuario)}")