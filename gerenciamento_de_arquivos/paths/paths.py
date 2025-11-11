from pathlib import Path

# caminho = Path("arquivinho.txt")
# caminho_absoluto = caminho.absolute()

# print(caminho)
# print(caminho_absoluto)

# caminho = Path(r"gerenciamento_de_arquivos\arquivinho.txt")
# if caminho.exists():
#     print("Existe")
# else:
#     print("Não existe")

# caminho = Path(r"gerenciamento_de_arquivos\pastinha")
# if caminho.is_file():
#     print("É um arquivo")
# elif caminho.is_dir():
#     print("É uma pasta")

# nova_pasta = Path(r"gerenciamento_de_arquivos\NovaPasta\outraPasta\maisUmaPasta")
# nova_pasta.mkdir(exist_ok=True, parents=True)

# arquivinho = Path(r"gerenciamento_de_arquivos\arquivinho.txt")
# novapasta = Path(r"gerenciamento_de_arquivos\NovaPasta")
# # arquivinho.unlink()
# novapasta.rmdir()

# arquivinho = Path(r"gerenciamento_de_arquivos\arquivinho.txt")
# # texto = arquivinho.read_text()
# # print(texto)
# arquivinho.write_text("Olá fefe", encoding='utf-8')

# pasta = Path(r"gerenciamento_de_arquivos\minha_pasta")
# for arquivo in pasta.glob("*txt"):
#     print(arquivo)

# caminho = Path("gerenciamento_de_arquivos\minha_pasta/dados.xlsx")
# print(caminho)
# print(caminho.name)
# print(caminho.stem)
# print(caminho.suffix)


arquivo = Path("gerenciamento_de_arquivos\meu_arquivo.txt")
# arquivo.touch()
arquivo.unlink()