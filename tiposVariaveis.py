# Inteiro (int)
idade = 25

# Ponto Flutuante (float)
altura = 1.75

# String (str)
nome = "Ana"

# Booleano (bool)
esta_chovendo = True

# Solicitando os dados do usuário
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))
nome = input("Digite seu nome: ")
esta_chovendo = input("Está chovendo? (sim/não): ").lower() == "sim"

# Exibindo uma mensagem personalizada com os dados coletados
print(f"Olá {nome}, você tem {idade} anos, mede {altura:.2f} metros de altura.")
if esta_chovendo:
    print("E está chovendo no momento!")
else:
    print("E não está chovendo no momento.")
