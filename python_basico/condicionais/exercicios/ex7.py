# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:
# "carro" → "Transporte terrestre"
# "bicicleta" → "Transporte sustentável"
# "avião" ou "helicóptero" → "Transporte aéreo"
# Qualquer outro → "Transporte desconhecido"

opcao = input("Digite o meio de transporte: ")
match opcao:
    case "carro":
        print("Veículo terrestre")
    case "bicicleta":
        print("Veículo sustentável")
    case "avião" | "helicóptero":
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")