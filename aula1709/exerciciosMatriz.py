# 1. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida.

print("\n" + "=" * 50)
print("EXERCÍCIO 1")
print("=" * 50)

matriz = []

for i in range(5):
    linha = []

    for j in range(5):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)

    matriz.append(linha)

for linha in matriz:
    print(linha)


# 2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

print("\n" + "=" * 50)
print("EXERCÍCIO 2")
print("=" * 50)

matriz = []

for i in range(4):
    linha = []

    for j in range(4):
        numero = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(numero)

    matriz.append(linha)

print("\nA matriz digitada foi:")

for linha in matriz:
    print(linha)

maior = max(max(linha) for linha in matriz)

for i in range(4):
    for j in range(4):
        if matriz[i][j] == maior:
            print(f"O maior valor da matriz é {maior}")
            print(f"Está na linha {i} e na coluna {j}")


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

matriz = []

for i in range(5):
    linha = []

    matricula = int(input("Digite a matrícula: "))
    linha.append(matricula)

    mediaProva = int(input("Digite a média das provas: "))
    linha.append(mediaProva)

    mediaTrab = int(input("Digite a média dos trabalhos: "))
    linha.append(mediaTrab)

    notaFinal = mediaProva + mediaTrab
    linha.append(notaFinal)

    matriz.append(linha)

maior = matriz[0][3]
matriculaMaior = matriz[0][0]

for i in range(5):
    if matriz[i][3] > maior:
        maior = matriz[i][3]
        matriculaMaior = matriz[i][0]

print(f"A matrícula do aluno com a maior nota é {matriculaMaior}")