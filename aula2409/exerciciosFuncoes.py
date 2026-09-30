# 1. Crie uma função chamada soma_elementos que receba um a lista de números como parâmetro e retorne a soma de todos os elementos dessa lista.
print("\n" + "=" * 50)
print("EXERCÍCIO 1")
print("=" * 50)

def soma_elementos (lista):
    soma = 0

    for numero in lista:
        soma += numero  

    return soma

"""
def soma_elementos (lista):
    return sum(lista)
"""

lista = [10, 20, 30, 40]
resultado = soma_elementos(lista)
print(resultado)

# 2. Crie uma função chamada e_palindromo que receba uma string como parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás para frente for igual à original) e False caso contrário.
print("\n" + "=" * 50)
print("EXERCÍCIO 2")
print("=" * 50)

def e_palindromo (palavra):
    if palavra == palavra[::-1]:
       return True
    else:
      return False

palavra = "ovo"
print(palavra)
print(e_palindromo(palavra))

palavra = "faca"
print(palavra)
print(e_palindromo(palavra))

# 3. Crie uma função chamada maior_elemento que receba uma lista de números como parâmetro e retorne o maior elemento dessa lista.
print("\n" + "=" * 50)
print("EXERCÍCIO 3")
print("=" * 50)

def maior_elemento(lista):
   maior = lista[0]
   
   for i in range (len(lista)):
      if lista[i] > maior:
         maior = lista[i]

   return maior

lista = [1, 10, 28, 876, 2, 85]
print(maior_elemento(lista))

# 4. Crie uma função chamada contar_caracteres que receba uma string e um caractere como parâmetros e retorne o número de vezes que o caractere aparece na string.
print("\n" + "=" * 50)
print("EXERCÍCIO 4")
print("=" * 50)

def contar_caracteres(texto, x):
    cont = 0

    for letra in texto:
        if letra == x:
            cont +=1

    return cont

"""
def contar_caracteres(texto, x):
    return texto.count(x)
"""

texto = "calculadora"
x = "a"

print(contar_caracteres(texto, x))

# 5. Implemente uma calculadora simples em Python utilizando funções.
# A calculadora deve ser capaz de realizar as seguintes operações matemáticas básicas:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão
#
# Requisitos:
# • Crie uma função para cada operação matemática (soma, subtração,
#   multiplicação e divisão). As funções devem receber dois valores e
#   retornar o resultado da operação.
#
# • Implemente uma função para exibir o menu de opções para o usuário.
#
# • O programa deve repetir o menu após cada operação, até que o usuário
#   escolha a opção de sair.
print("\n" + "=" * 50)
print("EXERCÍCIO 5")
print("=" * 50)

def exibir_menu():
    print("===== CALCULADORA =====")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


while True:
    exibir_menu()

    opc = int(input("\nDigite uma opção: "))

    if opc == 5:
        print("Programa encerrado")
        break

    elif opc == 1 or opc == 2 or opc == 3 or opc == 4:

        x = float(input("Digite o primeiro valor: "))
        y = float(input("Digite o segundo valor: "))

        if opc == 1:
            print(soma(x, y))

        elif opc == 2:
            print(subtracao(x, y))

        elif opc == 3:
            print(multiplicacao(x, y))

        elif opc == 4:
            print(divisao(x, y))

    else:
        print("\nOpção inválida\n")