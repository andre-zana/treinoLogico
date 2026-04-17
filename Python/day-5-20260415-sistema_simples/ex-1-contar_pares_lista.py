numLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parCount = 0

for num in numLista:
  if num % 2 == 0: # Se o número for par (divisível por 2 sem resto)
    parCount += 1 # ou parCount = parCount + 1
print("O número de pares na lista é: ", parCount)