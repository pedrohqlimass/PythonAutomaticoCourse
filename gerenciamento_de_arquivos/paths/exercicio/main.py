from estruturas import *
from arquivos import *


base = Path(r"gerenciamento_de_arquivos\paths\exercicio")
dados_entrada = base / "dados" / "entrada"

while True:
        print("""
    =========== MENU ===========
    1. Criar estrutura de pastas
    2. Criar arquivos de exemplo
    3. Listar arquivos .txt
    4. Apagar pasta 'dados'
    5. Apagar pasta 'relatorios'
    6. Apagar todas as pastas
    0. Sair
    """)

        opcao = int(input(""))
        match opcao:
            case 1:
                criar_estrutura_pastas()
                print(f"As pastas 'dados' e 'relatorios' foram criadas.\n{'-'*47}")
            case 2:
                if not dados_entrada.exists():
                    print(f"A estrutura não foi criada! Selecione a OPÇÃO 1 para criar a estrutura de pastas e depois volte para criar os arquivos.\n{'-'*119}")
                    continue
                criar_arquivos()
                print(f"Os arquivos 'dados1.txt','dados2.txt' e 'dados3.txt' foram criados.\n{'-'*67}")
            case 3:
                if not (base / "dados").exists():
                    print(f"A estrutura não foi criada! Selecione a OPÇÃO 1 para criar a estrutura de pastas e depois volte para listar a lista.\n{'-'*116}")
                    continue
                print("Listagem de arquivos:")
                listar_arquivos()
                print(f"{'-'*61}")
            case 4:
                if not (base / "dados").exists():
                    print(f"A pasta 'dados' não existe! Crie a estrutura primeiro.\n{'-'*28}")
                apagar_estrutura_pastas(Path(r"gerenciamento_de_arquivos\paths\exercicio\dados"))
                print(f"A pasta 'dados' foi apagada.\n{'-'*28}")
            case 5:
                if not (base / "relatorios").exists():
                    print(f"A pasta 'relatorios' não existe! Crie a estrutura primeiro.\n{'-'*30}")
                apagar_estrutura_pastas(Path(r"gerenciamento_de_arquivos\paths\exercicio\relatorios"))
                print(f"A pasta 'relatorios' foi apagada.\n{'-'*33}")
            case 6:
                if not dados_entrada.exists():
                    print(f"As pastas 'dados' e 'relatorios' ainda não foram criadas — não é possível apagá-las.\n{'-'*84}")
                else:
                    for pasta in ["dados", "relatorios"]:
                        apagar_estrutura_pastas(base / pasta)
                    print(f"As pastas 'dados' e 'relatorios' foram apagadas.\n{'-'*48}")
            case 0:
                print(f"Saindo do programa...\n{'-'*21}")
                break
            case _:
                print(f"Opção inválida.\n{'-'*15}")