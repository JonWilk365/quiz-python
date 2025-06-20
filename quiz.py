print("Seja bem-vindo ao Quiz de Direito Constitucional, Direito Civil e Processual civil")
receber_nome_usuario = input("Digite seu nome: ")

print(f"Vamos começar {receber_nome_usuario}")

receber_idade = input("Qual é a sua idade: ")
score = 0

if receber_idade == '18':
    print("Certa Resposta!")
    score = score + 1
else:
    print("Resposta Incorreta!")

print(f"Sua pontuação: {score}")  

print("Nova linha") 