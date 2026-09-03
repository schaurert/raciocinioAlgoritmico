# Exercícios — While

# 1. Implemente um programa em Python para ler do teclado a nota de um aluno. Verifique se o valor lido é uma nota válida (entre 0 e 10). Se não for, ler este valor até que a mesma seja válida;

nota = float(input("Digite a nota do aluno - a nota deve estar estar entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida. Ela deve estar estar entre 0 e 10 ")
    nota = float(input("Digite novamente: "))

print("Nota válida")

# 2. Implemente um programa em Python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1. Sendo N lido do teclado;

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
