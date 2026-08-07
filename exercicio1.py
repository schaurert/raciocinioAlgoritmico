# 1. Escreva um algoritmo em Python para calcular a idade de alguém, sabendo se seu ano de nascimento

# anoNascimento = int (input("Digite seu ano de nascimento: "))
# idade = 2026 - anoNascimento

# print(f"Sua idade é: {idade}")

# Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por um cliente de uma locadora de carros. Sabe se que:
# a. O valor de locação de cada carro é 100,00 reais;
# b. O cliente pode locar um único carro por vários dias.

contCarros = int(input("Quantos carros você deseja locar? "))
contDias = int(input("Quantos dias você deseja locar? "))

valorCarros = contCarros * 100
valorFinal = valorCarros * contDias

print(f"O valor final da sua compra é de R$: {valorFinal}")
