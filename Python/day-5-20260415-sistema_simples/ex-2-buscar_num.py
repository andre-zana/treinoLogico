numLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numBusca = int(input("Digite um número para buscar na lista: "))

if numBusca in numLista:
  print("O número", numBusca, "está presente na lista!")
else:
  print("O número", numBusca, "não está presente na lista!")