# Exercícios — While

# 1. Implemente um programa em Python para ler do teclado a nota de um aluno. Verifique se o valor lido é uma nota válida (entre 0 e 10). Se não for, ler este valor até que a mesma seja válida;
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - NOTA VÁLIDA")
print("=" * 50)

nota = float(input("Digite a nota do aluno - a nota deve estar estar entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida. Ela deve estar estar entre 0 e 10 ")
    nota = float(input("Digite novamente: "))

print("Nota válida")

# 2. Implemente um programa em Python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1. Sendo N lido do teclado;
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - SOMÁTORIO DE N TERMOS")
print("=" * 50)

num = int(input("Digite um número inteiro maior ou igual 1: "))

while num < 1:
    print("Número inválido")
    num = int(input("Digite novamante: "))

soma = 0
cont = 1
while cont <= num:
    soma +=cont
    cont+=1

print(f"O somatório de 1 até {num} é {soma}")


# 3. Implemente um programa em Python para ler do teclado números. Caso o usuário forneça um número igual a -1, o programa deve fornecer a média dos números e encerrar;
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - MÉDIA")
print("=" * 50)

soma = 0
qnt = 0

print("INSTRUÇÕES: Digite número para obter a média dos mesmos. Para encerrar o programa, basta digitar '-1' ")

num = float(input("Digite um número: "))

while num != -1:
    num = float(input("Dgite um número: "))

    if num == -1:
        break

    soma += num
    qnt += 1

media = soma / qnt

print(f"A média dos números digitados é: {media:.2f}")

# 4. Escreva um programa que receba 10 números do teclado e exiba a quantidade de números pares e ímpares lidos.
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - QNT DE IMPAR E PAR")
print("=" * 50)

cont = 0
impar = 0
par = 0
num = float(input("Digite um número: "))

while cont <=10:
    num = float(input("Digite um número: "))

    if num % 2 == 0:
        par +=1
    else:
        impar +=1

    cont +=1

print(f"Você digitou {par} números pares e {impar} números ímpares")

# Exercícios — FOR

# 1. Faça um programa que percorra os números de 1 até 100 e mostre apenas aqueles que são múltiplos de 3 e, ao mesmo tempo, não são múltiplos de 5. Ao final, mostre também quantos números atenderam a essa condição.
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - MULTIPLOS DE 3 E NÃO DE 5")
print("=" * 50)

atenderam = 0

for i in range (101):
    if i % 3 == 0 and i % 5 != 0:
        print (i)
        atenderam +=1
print(f"A quantidade de números que atenderam esse critério é: {atenderam} números")


# 2. Peça ao usuário um número inteiro positivo n. Não permita que o programa continue caso o número não seja válido. Em seguida, calcule e exiba a soma de todos os números de 1 até n. Ao final exiba a expressão aritmética completa, incluindo o resultado.
# Exemplo: n = 5 → Output: 1 + 2 + 3 + 4 + 5 = 15
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - SOMÁTORIO")
print("=" * 50)

soma = 0
expressao = ""

while True:
    try:
        num = int(input("Digite um número inteiro positivo: "))

        if num >= 0:
            break
        else:
            print("Você digitou um número inválido.")

    except ValueError:
        print("Entrada inválida. Digite apenas um número inteiro positivo.")

for i in range (1, num + 1):
    soma +=1
    expressao += str(i)

    if i < num:
        expressao += " + "

print(f"{expressao} = {soma}")

# 3. Peça ao usuário um número inicial e um número final. Para cada número dentro desse intervalo, exiba a tabuada dele de 1 até 10.
# Exemplo: início = 3, fim = 5 → Output: tabuada do 3, tabuada do 4 e tabuada do 5.
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - TABUÁDA")
print("=" * 50)

numInical = int(input("Digite um número inicial: "))
numFinal = int(input("Digite um número final: "))

for i in range (numInical, numFinal + 1):
    #cont = 1 - opc c while
    print("\n")
    print(f"Tábuada do número {i}")

    for multiplicador in range (1,11):
        resultado = i * multiplicador
        print(f"{i} X {multiplicador} = {resultado}")

    # while cont <= 10:
    #     print(f"{i} x {cont} = {i * cont}")
    #     cont += 1


# 4. Peça ao usuário que digite um valor referente à quantidade de linhas. Em seguida, utilize for para exibir o seguinte padrão: (Exemplo para usuário que digitou 5)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - LINHAS")
print("=" * 50)

linhas = int(input("Digite a quantidade de linhas: "))

for i in range(1, linhas + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()