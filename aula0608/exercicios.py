# # 1. Escreva um algoritmo em Python para calcular a idade de alguém, sabendo se seu ano de nascimento

# print("Calculadora de idade")
# print("--------------------")

# anoNascimento = int (input("Digite seu ano de nascimento: "))
# idade = 2026 - anoNascimento

# print(f"Sua idade é: {idade}")
# print("\n")

# # 2. Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por um cliente de uma locadora de carros. Sabe se que:
# # a. O valor de locação de cada carro é 100,00 reais;
# # b. O cliente pode locar um único carro por vários dias.

# print("Locadora de carro")
# print("-----------------")

# valorCarro = 100
# contDias = int(input("Quantos dias você deseja locar o carro? "))

# valorFinal = valorCarro * contDias

# print(f"O valor final da sua compra é de R$: {valorFinal}")
# print("\n")

# # 3. Leia do teclado a temperatura em Celsius e imprima o equivalente em Fahrenheit. (Fórmula: (X ºC × 9/5) + 32

# print("Conversor de temperatura")
# print("------------------------")

# tempCelsius = float(input("Digite a temperatura em Celsius: "))
# tempFahrenheit = (tempCelsius * 9/5) + 32

# print(f"A temperatura em Fahrenheit é: {tempFahrenheit}")
# print("\n")

# # 4. Escrever um algoritmo para calcular a média de 4 notas.

# print("Calculadora de média")
# print("--------------------")

# nota1 = float(input("Digite a 1ª nota: "))
# nota2 = float(input("Digite a 2ª nota: "))
# nota3 = float(input("Digite a 3ª nota: "))
# nota4 = float(input("Digite a 4ª nota: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print(f"A média final é: {media}")
# print("\n")

# # 5. Calcular sua idade em meses.

print("Conversor de anos em meses")
print("--------------------------")

idade = int(input("Digite sua idade: "))

mesNascimento = int(input("Digite seu mes de nascimento: "))

meses = 8 - mesNascimento

anoParaMeses = (idade * 12 )+ meses

print(f"{idade} anos é igual a {anoParaMeses} meses")
print("\n")

# 6. Calcular preço de venda para produto por quilo.

print("Balança digital")
print("----------------")

precoQuilo = float(input("Digito o preço do quilo do produto: "))
peso = float(input("Digito o peso do seu produto em quilos: "))

precoFinal = float(peso * precoQuilo)

print(f"O preço do seu produto é: {precoFinal:.2f}")