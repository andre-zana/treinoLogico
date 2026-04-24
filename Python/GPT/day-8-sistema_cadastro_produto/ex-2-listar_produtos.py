listaProdutos = []

def add_produto(lista, nomeProduto, precoProduto, quantidadeProduto):
    produto = {
        "Nome": nomeProduto,
        "Preço": precoProduto,
        "Quantidade": quantidadeProduto
    }
    lista.append(produto)
    return produto

def listar_produto(lista):
    return lista

while True:
    print("")
    print("Bem-vindo ao sistema de cadastro de produtos!")
    print("")
    print("De acordo com o menu abaixo...")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")
    userInput = input("Digite o número da opção desejada: ")
    print("")

    if userInput == "1":
        nomeProduto = input("Digite o nome do produto: ")
        precoProduto = float(input("Digite o preço do produto: "))
        quantidadeProduto = int(input("Digite a quantidade do produto: "))
        add_produto(listaProdutos, nomeProduto, precoProduto, quantidadeProduto)
        print()
        print(f"O produto {nomeProduto} foi adicionado com sucesso!")
        print()
    elif userInput == "2":
        print(listar_produto(listaProdutos))
    elif userInput == "3":
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção do menu.")