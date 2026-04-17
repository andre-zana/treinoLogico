num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

def somar(num1, num2):
  # Se eu for reutilizar valor e/ou for uma fórmula mais complexa, é interessante criar uma variável para armazenar o resultado
  # soma = num1 + num2 
  # return soma
  # -----
  # Se for algo simples, posso retornar o resultado direto
  return num1 + num2

print(somar(num1, num2))