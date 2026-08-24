# EXERCÍCIO 1 
print("\n" + "=" * 50)
print("EXERCÍCIO 1 - ESCOLHA DE CAMINHO")
print("=" * 50)

direcao = input("Escolha o caminho: esquerda ou direita: ").lower()

if direcao == "esquerda":
    print("Você encontrou um rio!")
    opcao = input("Você quer atravessar ou voltar? ").lower()

    if opcao == "atravessar":
        print("Você chegou a uma vila segura!")
    else:
        print("Você ainda está perdido na floresta!")

elif direcao == "direita":
    print("Você encontrou uma montanha!")
    opcao = input("Você quer subir ou voltar? ").lower()

    if opcao == "subir":
        print("Parabéns, você encontrou o tesouro no topo da montanha!")
    else:
        print("Você ainda está perdido na floresta!")

else:
    print("Opção inválida!")


# EXERCÍCIO 2
print("\n" + "=" * 50)
print("EXERCÍCIO 2 - VERIFICAÇÃO DE INTERVALO")
print("=" * 50)

num = float(input("Digite um número: "))

if num >= 10 and num <= 50:
    print("O número está entre 10 e 50.")
elif num < 10:
    print("O número é menor que 10.")
else:
    print("O número é maior que 50.")


# EXERCÍCIO 3
print("\n" + "=" * 50)
print("EXERCÍCIO 3 - ANO BISSEXTO")
print("=" * 50)

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")


# EXERCÍCIO 4
print("\n" + "=" * 50)
print("EXERCÍCIO 4 - USUÁRIO E SENHA")
print("=" * 50)

usuario = input("Digite o usuário: ").lower()
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido!")
elif usuario == "convidado" and senha == "":
    print("Acesso restrito!")
else:
    print("Acesso bloqueado!")


# EXERCÍCIO 5
print("\n" + "=" * 50)
print("EXERCÍCIO 5 - POSIÇÃO DO PONTO NO QUADRADO")
print("=" * 50)

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x >= 0 and x <= 10 \
   and y >= 0 and y <= 10:
    if x > 0 and x < 10 and y > 0 and y < 10:
        print("Dentro do quadrado.")
    else:
        print("Na fronteira.")
else:
    print("Fora do quadrado.")


# EXERCÍCIO 6 - [DESAFIO]
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - CLASSIFICAÇÃO DO TRIÂNGULO")
print("=" * 50)

lado1 = float(input("Digite o 1º lado do triângulo: "))
lado2 = float(input("Digite o 2º lado do triângulo: "))
lado3 = float(input("Digite o 3º lado do triângulo: "))

validacao1 = lado1 + lado2 > lado3
validacao2 = lado1 + lado3 > lado2
validacao3 = lado2 + lado3 > lado1

if lado1 > 0 and lado2 > 0 and lado3 > 0 \
    and validacao1 and validacao2 and validacao3:
    if lado1 == lado2 and lado1 == lado3:
        print("Os valores formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores formam um triângulo isósceles.")
    else:
        print("Os valores formam um triângulo escaleno.")
else:
    print("Os valores informados não formam um triângulo.")


print("\n" + "=" * 50)
print("FIM DO PROGRAMA")
print("=" * 50)