numLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maiorNum = numLista[0]
somaLista = 0

while True:
  print("")
  print("Bem-vindo ao sistema simples!")
  print("")
  print("De acordo com o menu abaixo...")
  print("1 - Ver lista")
  print("2 - Ver maior número")
  print("3 - Ver média")
  print("4 - Sair")
  userInput = input("Digite o número da opção desejada: ")
  print("")  

  if userInput == "1":
    print(numLista)
  elif userInput == "2":
    for num in numLista:
      if num > maiorNum:
        maiorNum = num
    print("O maior número da lista é: ", maiorNum)
  elif userInput == "3":
    for num in numLista:
      somaLista += num # ou somaLista = somaLista + num
    mediaLista = somaLista / len(numLista)
    print("A média dos números da lista é: ", mediaLista)
  elif userInput == "4":
    break
  else:
    print("Opção inválida! Por favor, escolha uma opção do menu.")