# Exercício 2 – Criar vários arquivos de exemplo
# Dentro da pasta entrada/, crie 3 arquivos vazios:
# dados1.txt
# dados2.txt
# dados3.txt
# Exercício 3 – Conferindo e filtrando arquivos .txt
# Liste todos os arquivos .txt dentro de entrada/.
# Imprima apenas o nome do arquivo (sem o caminho completo).

from pathlib import Path


def criar_arquivos():
    pasta = Path(r"gerenciamento_de_arquivos\paths\exercicio\dados\entrada")
    arquivos = ["dados1.txt", "dados2.txt", "dados3.txt"]

    for arquivo in arquivos:
        (pasta / arquivo).touch(exist_ok=True)

def listar_arquivos():
    pasta = Path(r"gerenciamento_de_arquivos\paths\exercicio\dados\entrada")
    for arquivo in pasta.glob("*txt"):
        print(arquivo)