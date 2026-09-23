numbers = [10, 7, 2, 15] #nome do vetor precisa ser plural

#acessar índice (indicies começam em 0)
#nome_varialvel[indice]
#ex.: soma 10 e 7
numbers[0]+numbers[2]

#exemplo01:
numeros = [5, 7, 12, 2, 9, 21] #tamanho = quantidade que tem dentro do vetor | indice = tamanho -1
print(len(numeros))
print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])

#substituir algum valor do vetor

numeros[1] = 17
numeros[3] = 22
print(numeros)

numeros[2] = 1
numeros[4] = 29
print(numeros)

#Na mesma atividade realizada na Prática 2, some os valores 21 e 29, subtraia os valores 22 e 17, multiplique os valores dos índices 0 e 5 e divida os valores dos índices 3 e 2. Faça isso criando uma variável para cada operação. Imprima cada uma das operações na tela.

soma = (numeros[5] + numeros[4])
print(soma)

sub = (numeros[3] - numeros[1])
print(sub)

mult = (numeros[0] * numeros[5])
print(mult)

div = (numeros[3]/numeros[2])
print(div)


#Na mesma atividade realizada na Prática 3, percorra o vetor utilizando while e imprima cada um dos valores do vetor multiplicados por 2. Faça a mesma coisa com for(i) e for(each)
numeros = [5, 17, 1, 22, 29, 21]
indice = 0

while indice < len(numeros):
    print(numeros[indice]*2)
    indice +=1

print()

for i in range (len(numeros)):
    print(numeros[i] * 2)

print()

for numero in numeros:
    print(numero * 2)

#Implemente um programa em Python para verificar quantos números uma aposta acertou na Mega Sena. O programa deve ler do teclado os 6 números apostados e comparar com os 6 números sorteados. Ao final, o programa deve exibir os números sorteados, númeroa jogados e quantidade de acertos.

