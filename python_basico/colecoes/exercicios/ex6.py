# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.
# Se o usuário e a senha estão corretos → "Login bem-sucedido"
# Senão → "Usuário ou senha incorretos"

credenciais_corretas = {
    "usuario": "pedrohq",
    "senha": "Pedr@123"
}

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

informacoes_inseridas = {
    "usuario": usuario,
    "senha": senha
}

if usuario == credenciais_corretas["usuario"] and senha == credenciais_corretas["senha"]:
    print("Login bem-sucedido!")
else:
    print("Usuário e senha incorretos.")