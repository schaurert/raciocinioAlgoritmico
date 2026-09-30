# 1. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida.

print("\n" + "=" * 50)
print("EXERCÍCIO 1")
print("=" * 50)

matriz = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
]

for i in range (5):
    for j in range (5):
        if i == j:
            matriz[i][j] = 1

for i in matriz:
    print(i)

# 2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

print("\n" + "=" * 50)
print("EXERCÍCIO 2")
print("=" * 50)

matriz = [
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
]

for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite o valor [{i}][{j}]: "))

print("\nA matriz digitada foi:")
for linha in matriz:
    print(linha)

maior = matriz[0][0]
linhMaior = 0
colunaMaior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linhMaior = i
            colunaMaior = j

print(f"O maior valor digitado foi {maior} e está na linha {linhMaior} e coluna {colunaMaior}")

# 3. Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes informações sobre alunos de uma disciplina, sendo todas as informações do tipo inteiro:
# a. Primeira coluna: número de matrícula (use um inteiro)
# b. Segunda coluna: media das provas
# c. Terceira coluna: media dos trabalhos
# d. Quarta coluna: nota final
# Elabore um programa que:
# a. Leia as três primeiras informações de cada aluno;
# b. Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos;
# c. Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe uma maior nota)

print("\n" + "=" * 50)
print("EXERCÍCIO 3")
print("=" * 50)

matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range (5):
    matriz[i][0] = int(input("Digite a matricula do aluno: "))
    matriz[i][1] = int(input("Digite a média das provas: "))
    matriz[i][2] = int(input("Digite a média dos trabalhos: "))
    matriz[i][3] = matriz[i][1] + matriz[i][2]

for i in range (5):
    print(matriz[i])

maiorNota = matriz[0][3]
matriculaMaior = matriz[0][0]

for i in range (5):
    if matriz[i][3] > maiorNota:
        maiorNota = matriz[i][3]
        matriculaMaior = matriz[i][0]

print(f"A matricula do aluno com a maior nota é {matriculaMaior}")