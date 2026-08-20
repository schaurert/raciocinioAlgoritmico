# ==================================================
# Exercício 1
# Leia a idade de uma pessoa e informe True se ela
# tiver 18 anos ou mais e False caso contrário.
# ==================================================
idade = int(input("Digite sua idade: "))
print(idade >= 18)

print("\n" + "=" * 50)
# ==================================================
# Exercício 2
# Leia uma senha e informe True se a senha digitada
# for "python123" e False caso contrário.
# ==================================================
senha = input("Digite sua senha: ")
print(senha == "python123")

print("\n" + "=" * 50)
# ==================================================
# Exercício 3
# Leia um número e informe True se ele for diferente
# de 100.
# ==================================================
num = float(input("Digite um número: "))
print(num != 100)

print("\n" + "=" * 50)
# ==================================================
# Exercício 4
# Leia a idade e a altura de uma pessoa.
# Ela pode andar no brinquedo se tiver pelo menos
# 12 anos e pelo menos 1,40 m de altura.
# ==================================================
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
print(idade >= 12 and altura >= 1.40)

print("\n" + "=" * 50)
# ==================================================
# Exercício 5
# Leia a idade e pergunte se a pessoa é estudante.
# Ela recebe desconto se tiver até 12 anos ou
# for estudante.
# ==================================================
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? (sim/nao): ")
print(idade <= 12 or estudante == "sim")

print("\n" + "=" * 50)
# ==================================================
# Exercício 6
# Leia o nome de usuário e a senha.
# O acesso é válido somente se o usuário for "admin"
# e a senha for "1234".
# ==================================================
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
print(usuario == "admin" and senha == "1234")

print("\n" + "=" * 50)
# ==================================================
# Exercício 7
# Leia um número e informe se ele está entre 10 e 20,
# inclusive.
# ==================================================
num = float(input("Digite um número: "))
print(num >= 10 and num <= 20)

print("\n" + "=" * 50)
# ==================================================
# Exercício 8
# Leia a idade e se a pessoa está acompanhada.
# Ela pode entrar se tiver 18 anos ou mais ou
# estiver acompanhada.
# ==================================================
idade = int(input("Digite sua idade: "))
acompanhada = input("Está acompanhada? (sim/nao): ")
print(idade >= 18 or acompanhada == "sim")

print("\n" + "=" * 50)
# ==================================================
# Exercício 9
# Leia o valor da compra e se o cliente possui
# assinatura premium.
# Recebe frete grátis se gastar pelo menos R$ 200
# ou possuir assinatura premium.
# ==================================================
valor = float(input("Digite o valor da compra: "))
assinatura = input("Você tem assinatura premium? (sim/nao): ")
print(valor >= 200 or assinatura == "sim")

print("\n" + "=" * 50)
# ==================================================
# Exercício 10
# Leia a idade, se possui ingresso e se está
# acompanhada por um responsável.
# ==================================================
idade = int(input("Digite sua idade: "))
ingresso = input("Você possui ingresso? (sim/nao): ")
acompanhada = input("Esta acompanhada por um responsável? (sim/nao): ")

print(ingresso == "sim" and (idade >= 18 or acompanhada == "sim"))