num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
ops = input("Digite a operação (sinal) desejada: ")
result = ""

if ops == "+":
    result = num1 + num2
elif ops == "-":
    result = num1 - num2
elif ops == "*":
    result = num1 * num2
elif ops == "/":
    if num2 == 0:
        result = "Erro: Divisão por zero não é permitida."
    else:
        result = num1 / num2

print(result)