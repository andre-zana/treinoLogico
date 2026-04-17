numLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ver_lista(lista):
  return lista

def ver_maior(lista):
  maiorNum = lista[0]
  for num in lista:
      if num > maiorNum:
        maiorNum = num    
  return maiorNum
  
def ver_media(lista):
  somaLista = 0
  for num in lista:
    somaLista += num # ou somaLista = somaLista + num
  return somaLista / len(lista)

def add_numero(lista, numero):
  lista.append(numero)
  return numero

def del_numero(lista, numero):
  if numero in lista:
    lista.remove(numero)  
    return True
  else:
    return False
  
def ver_menor(lista):
  menorNum = lista[0]
  for num in lista:
      if num < menorNum:
        menorNum = num    
  return menorNum

while True:
  print("")
  print("Bem-vindo ao sistema simples!")
  print("")
  print("De acordo com o menu abaixo...")
  print("1 - Ver lista")
  print("2 - Ver maior número")
  print("3 - Ver média")
  print("4 - Adicionar número")
  print("5 - Remover número")
  print("7 - Ver menor número")
  print("8 - Sair")
  userInput = input("Digite o número da opção desejada: ")
  print("")

  if userInput == "1":
    print(ver_lista(numLista))
  elif userInput == "2":
    print("O maior número da lista é: ",ver_maior(numLista))
  elif userInput == "3":
    print("A média dos números da lista é: ",ver_media(numLista))
  elif userInput == "4":
    addNum = int(input("Digite o número que deseja adicionar a lista: "))
    print(f"O número {add_numero(numLista, addNum)} foi adicionado a lista com sucesso!")
  elif userInput == "5":
    delNum = int(input("Digite o número que deseja remover da lista: "))
    deletado = del_numero(numLista, delNum)
    if deletado:
      print("")
      print(f"O número {delNum} foi removido da lista com sucesso!")
    else:
      print("")
      print(f"O número {delNum} não foi encontrado na lista!")
  elif userInput == "7":
    print("O menor número da lista é: ",ver_menor(numLista))
  elif userInput == "8":
    break
  else:
    print("Opção inválida! Por favor, escolha uma opção do menu.")