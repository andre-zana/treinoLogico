nome = input("Digite o seu nome: ")
hora = int(input("Digite a hora atual (0-23): "))

if hora < 0 or hora > 23:
    print("Hora inválida. Por favor, insira um valor entre 0 e 23.")
elif hora <= 11:
    print(f"Bom dia, {nome}")
elif hora <= 17:
    print(f"Boa tarde, {nome}")
elif hora <= 23:
    print(f"Boa noite, {nome}")
