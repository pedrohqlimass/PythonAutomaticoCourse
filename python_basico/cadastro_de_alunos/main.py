alunos = []

def adicionar_aluno():
    nome = input("Insira o nome do aluno: ")
    idade = int(input("Insira a idade do aluno: "))
    while True:
        nota = float(input("Insira a nota do aluno: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("Nota inválida. A nota precisa ser de 0 a 10\n")
    dados = {
        "nome":nome,
        "idade":idade,
        "nota":nota
    }
    alunos.append(dados)

def listar_alunos():
        if not alunos:
            print("Não há nenhum aluno cadastrado.\n")
            return
        for aluno in alunos:
                print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}\n{'='*30}")

def procurar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print(f"Não há nenhum aluno cadastrado.\n")
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}\n")
            break
    else:
        print("Aluno não encontrado.\n")

def deletar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print("Não há nenhum aluno cadastrado.\n")
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} foi deletado com sucesso!\n")
            break
    else:
        print("Aluno não encontrado.\n")

def media_de_notas():
    if len(alunos) == 0:
        print("Não há nenhum aluno cadastrado.\n")
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f"A média das notas dos alunos é {media:.2f}")

print("---Bem Vindo ao Sistema de Cadastro de Alunos---\n")
while True:
    opcao = int(input("O que deseja fazer?\nn1. Adicionar aluno\n2. Listar alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair\n"))
    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            nome_aluno = input("Qual aluno deseja buscar? ")
            procurar_aluno(nome_aluno)
        case 4:
            nome_aluno = input("Qual aluno deseja remover? ")
            deletar_aluno(nome_aluno)
        case 5:
            media_de_notas()
        case 6:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida! Tente novamente.")