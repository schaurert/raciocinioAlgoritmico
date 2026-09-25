# 1. Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros. O programa deve executar os seguintes passos:
# (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
# (b) Armazene em uma variável inteira (simples) a soma entre os valores das posicões A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
# (c) Modifique o vetor na posicão 4, atribuindo a esta posicão o valor 100.
# # (d) Mostre na tela cada valor do vetor A, um em cada linha.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 1")
# print("=" * 50)
# A = [1, 0, 5, -2, -5, 7]
# soma = A[0] + A[1] + A[5]

# print(f"O valor da soma entre as posições 0, 1 e 5 do Vetor A é: {soma}")

# A[4] = 100
# print()

# print("Os valores dentro do vetor são:")
# for i in range (len(A)):
#     print(A[i])


# 2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
print("\n" + "=" * 50)
print("EXERCÍCIO 2")
print("=" * 50)
numeros = [0] * 6

for i in range(len(numeros)):
    numeros[i] = int(input("Digite um número inteiro: "))

for i in range (len(numeros)):
    print(numeros[i])


"""
numeros = []

while True:
    numero = int(input("Digite um número inteiro (0 - sair): "))

    if numero == 0:
        break

    numeros.append(numero)

print(f"Os números digitados foram: {numeros}")
"""


# # 3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir os conjuntos.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 3")
# print("=" * 50)
# numeros = []

# vetorA = []
# vetorB = []

# for i in range (10):
#     numero = float(input("Digite um número real: "))
#     vetorA.append(numero)

# for i in range(len(vetorA)):
#     quadrado = vetorA[i] ** 2
#     vetorB.append(quadrado)

# print(f"Os valores que você digitou são: {vetorA}")
# print(f"Os valores digitados ao quadrado são: {vetorB}")


# # 4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y .
# print("\n" + "=" * 50)
# print("EXERCÍCIO 4")
# print("=" * 50)
# vetor = []
# posicoes = []
# cont = 0

# for i in range (8):
#     numero = input(f"Digite um número para popular a posição {i} do seu vetor: ")

#     while not numero.isdigit():
#         print("Você deve digitar apenas número inteiro.")
#         numero = input("Digite novamente: ")

#     numero = int(numero)
#     vetor.append(numero)

# while cont < 2:
#     posicao = input("Digite uma posição do vetor (0-7): ")

#     while not posicao.isdigit():
#         print("Você deve digitar apenas número inteiro.")
#         posicao = input("Digite novamente: ")

#     posicao = int(posicao)

#     while posicao < 0 or posicao > 7:
#         print("Você deve digitar uma posição entre 0 e 7.")
#         posicao = input("Digite novamente: ")

#     posicao = int(posicao)

#     posicoes.append(posicao)
#     cont += 1

# soma = 0
# cont2 = 0

# while cont2 < (len(posicoes)):
#     soma += vetor[posicoes[cont2]]
#     cont2 += 1

# print(f"A soma dos valores nas posições escolhidas é: {soma}")


# # 5. Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 5")
# print("=" * 50)
# vetor = []
# par = 0

# for i in range (10):
#     numero = input(f"Digite um valor para a posição {i} do seu vetor: ")

#     while not numero.isdigit():
#         print("Você deve digitar apenas números inteiros")
#         numero = input(f"Digite novamente: ")

#     numero = int(numero)
#     vetor.append(numero)

#     if numero % 2 == 0:
#         par += 1

# tamanho = len(vetor)
# print(f"O vetor possui {tamanho} valores")
# print(f"O vetor possui {par} números pares")

# # 6. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 6")
# print("=" * 50)
# vetor = []

# for i in range (10):
#     numero = float(input("Digite um número: "))
#     vetor.append(numero)

# maior = vetor[0]
# menor = vetor[0]

# for i in range(1,5): #pq nao precisa verificar a posicao 0 novamente
#     if vetor[i] < menor:
#         menor = vetor[i]

#     if vetor[i] > maior:
#         maior = vetor[i]

# print(f"O maior número do seu vetor é {maior} e o menor é {menor}")


# # 7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 7")
# print("=" * 50)
# vetor = []
# for i in range (10):
#     numero = input(f"Digite um valor para a posição {i} do seu vetor: ")

#     while not numero.isdigit():
#         print("Você deve digitar apenas números inteiros")
#         numero = input(f"Digite novamente: ")

#     numero = int(numero)
#     vetor.append(numero)

# print(f"O vetor que você digitou foi: {vetor}")

# maior = vetor[0]
# posicao = 0

# for i in range(len(vetor)):

#     if vetor[i] > maior:
#         maior = vetor[i]
#         posicao = i

# print(f"O maior número do seu vetor é {maior} e está na posição {posicao}")


# # 8. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 8")
# print("=" * 50)
# notas = []
# media = 0

# for i in range (15):
#     nota = float(input("Digite uma nota: "))
#     notas.append(nota)

#     media += notas[i]

# for i in range(len(notas)):
#     media /= len(notas)

# print(f"A média geral das notas digitas é: {media}")


# # 9. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 9")
# print("=" * 50)
# numeros = []
# negativo = 0
# somaPositivo = 0

# for i in range (10):
#     numero = float(input("Digite um número real: "))
#     numeros.append(numero)

#     if numero < 0:
#         negativo += 1

#     else:
#         somaPositivo += numero

# print(f"A quantidade de números negativos que você digitou é: {negativo}")
# print(f"O valor da soma de todos os números positivos digitados é {somaPositivo}:")

    
# # 10. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 10")
# print("=" * 50)
# numeros = []

# for i in range(5):
#     numero = float(input("Digite um número: "))
#     numeros.append(numero)

# maior = max(numeros)
# menor = min(numeros)
# soma = sum(numeros)
# media = soma / len(numeros)

# print(f"Valores lidos: {numeros}")
# print(f"Maior: {maior}")
# print(f"Menor: {menor}")
# print(f"Média: {media}")


# # 11. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
# print("\n" + "=" * 50)
# print("EXERCÍCIO 10")
# print("=" * 50)
# numeros = []

# for i in range(5):
#     numero = float(input("Digite um número: "))
#     numeros.append(numero)

# maior = max(numeros)
# menor = min(numeros)
# posicaoMaior = numeros.index(maior)
# posicaoMenor = numeros.index(menor)

# print(f"O maior valor digitado foi {maior} na posição {posicaoMaior}")
# print(f"O menor valor digitado foi {menor} na posição {posicaoMenor}")





# # ------------------CORREÇÃO-----------------------------------------

