numLista = [1, 2, 3, 4, 5]
maiorNum = numLista[0]
for numero in numLista: # Se não precisa de posição, não usa range(len(numLista))
  if numero > maiorNum:
    maiorNum = numero
print("O maior número da lista é: ", maiorNum)