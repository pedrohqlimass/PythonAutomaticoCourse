# Exercício 1 – Criando estrutura de pastas
# Crie a seguinte estrutura:
# ├──dados/
# │  ├── entrada/
# │  └── saida/
# ├──relatorios/
# Crie todas as pastas em uma única execução do seu código.
# criar um método para apagar a estrutura nao fazia parte do exercício, mas achei interessante essa funcionalidade para nao poluir do a pasta exercicios quando eu desse git push

from pathlib import Path


def criar_estrutura_pastas():
    base = Path(r"gerenciamento_de_arquivos\paths\exercicio")
    pastas = ["dados", "relatorios"]
    subpastas = ["entrada", "saida"]

    for pasta in pastas:
        caminho = base / pasta
        caminho.mkdir(exist_ok=True, parents=True)
        
        if pasta == "dados":
            for subpasta in subpastas:
                (caminho / subpasta).mkdir(exist_ok=True, parents=True)

def apagar_estrutura_pastas(pasta: Path):
    if pasta.exists() and pasta.is_dir():
        
        for arquivo in pasta.iterdir():
            if arquivo.is_file():
                arquivo.unlink()
            elif arquivo.is_dir():
                apagar_estrutura_pastas(arquivo)
        pasta.rmdir()