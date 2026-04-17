num = int(input("Digite um número: "))

def paridade(num):
  if num % 2 == 0:
    return "O número digitado é Par!"    
  else:
    return "O número digitado é Ímpar!"

print(paridade(num))