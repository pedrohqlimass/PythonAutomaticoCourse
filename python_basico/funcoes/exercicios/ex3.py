# Crie uma função chamada verificar_par(numero) que retorna:
# "Par" se o número for par
# "Ímpar" se for ímpar
# Peça um número ao usuário com input(), chame a função e mostre o resultado.

#usando print 
# def verificar_par(numero):
#     if numero % 2 == 0:
#         print(f"{numero} é par")
#     else:
#         print(f"{numero} é impar")
# numero_usuario = float(input("Digite um número: "))
# verificar_par(numero_usuario)

#usando return
def verificar_par(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero_usuario = float(input("Digite um número: "))
resultado = verificar_par(numero_usuario)
print(f"{numero_usuario} é {resultado}")