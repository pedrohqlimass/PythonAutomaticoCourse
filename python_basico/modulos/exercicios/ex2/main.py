# Desafio 2 – Criando um pacote de utilidades
# Crie uma pasta chamada meu_pacote

# Dentro dela, crie:
# formatador.py → função caixa_alta(texto) → retorna o texto em letras maiúsculas
# numeros.py → função eh_par(numero) → retorna True se for par

# No main.py:
# Importe e use as funções do pacote
# Exiba o resultado formatado

from meu_pacote.formatador import caixa_alta
from meu_pacote.numeros import eh_par

texto_usuario = input("Digite um texto para ver em CAIXA ALTA: ")
print(f"Seu texto em caixa alta: {caixa_alta(texto_usuario)}")

numero = float(input("Digite um número para ver se é PAR ou IMPAR\nSe for par: True\nSe for impar: False\n"))
print(eh_par(numero))