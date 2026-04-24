listaProdutos = []

comntinuar = True
while continuar:
  nomeProduto = input("Digite o nome do produto: ")
  precoProduto = float(input("Digite o preço do produto: "))
  quantidadeProduto = int(input("Digite a quantidade do produto: "))
  produto = {
    "nome": nomeProduto,
    "preço": precoProduto,
    "quantidade": quantidadeProduto,
  }
  listaProdutos.append(produto)
  
  print()

  while True:
    resposta = input("Deseja adicionar outro produto? (s/n): ")
    if resposta.lower() == 's':
      break
    elif resposta.lower() == 'n':
      continuar = False
      break      
    else:
      print("Resposta inválida.")

for produto in listaProdutos:
        print()
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preço']}")
        print(f"Quantidade: {produto['quantidade']}")
        print()
        print(produto)