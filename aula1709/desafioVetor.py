# [DESAFIO] Implemente um programa em Python para verificar quantos números uma aposta acertou na Mega Sena. O programa deve ler do teclado os 6 números apostados e comparar com os 6 números sorteados. Ao final, o programa deve exibir os números sorteados, númeroa jogados e quantidade de acertos. Obs: Faça essa atividade usando apenas os conceitos de vetores, sem utilizar nenhuma funcionalidade de listas.

import random

numerosApostados = [0] * 6
numerosSorteados = sorted(random.sample(range(1, 61), 6)) # Gera 6 números únicos entre 1 e 100, ordenados

for i in range (6):
    numerosApostados[i] = int(input("Digite um valor: "))

acertos = 0

for i in range (6):
    if numerosApostados[i] == numerosSorteados[i]:
        acertos += 1

print(f"Os números apostados foram: {numerosApostados}")
print(f"Os números sorteados foram: {numerosSorteados}")
print(f"Você acertou {acertos} números")