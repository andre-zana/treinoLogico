numLista = [1, 2, 3, 4, 5]
somaLista = 0

for numero in numLista:
  somaLista += numero # ou somaLista = somaLista + numero
mediaLista = somaLista / len(numLista)
print("A média dos números da lista é: ", mediaLista)