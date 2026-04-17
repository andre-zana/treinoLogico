num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

# if num1 > num2:
#   print(f"O maior número é {num1}")
# elif num1 < num2:
#   print(f"O maior número é {num2}")
# else:
#   print("Números iguais!")

if num1 > num2:
  print(f"O maior número é {num1}")
elif num1 == num2:
  print("Números iguais!")
else:
  print(f"O maior número é {num2}")

# Desta forma, fica menos comparativo no if