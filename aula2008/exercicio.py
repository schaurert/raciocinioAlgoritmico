# Você está em uma floresta e precisa escolher um caminho para seguir. Você pode escolher: esquerda ou direita.
# ➔ Se escolher o caminho da esquerda você encontrará um rio. Você deverá decidir: atravessar ou voltar.
# ➔ Se escolher o caminho da direita você encontrará uma montanha. Você deverá decidir: subir ou voltar.
#RESULTADO
# Caminho da esquerda:
# ➔ Se atravessar - você chega a uma vila segura
# ➔ Se voltar - você permanece perdido na floresta
# Caminho da direita:
# ➔ Se subir - você encontra um tesouro no topo
# ➔ Se voltar - você permanece perdido na floresta

# direcao = input("Escolha o caminho: esquerda ou direita ").lower()

# if direcao == "direita":
#     print("Você encontrou um rio!")
#     opc = input("Você quer atravessar ou voltar? ").lower()

#     if opc == "atravessar":
#         print("Você chegou em uma vila segura!")
#     else:
#         print("Você ainda está perdido na floresta!")
# else:
#     print("Você encontrou uma montanha!")
#     opc = input("Você quer subir ou voltar? ").lower()

#     if opc == "subir":
#         print("Parabéns, você encontrou o tesouro no topo da montanha")
#     else:
#         print("Você ainda está perdido na floresta!")

# 2. Peça um número e verifique:
# se está entre 10 e 50 (inclusive);
# se é menor que 10;
# se é maior que 50.

# num = float(input("Digite um número: "))

# if num >=10 and num <=50:
#     print("o número está entre 10 e 50")
# elif num <10:
#     print("o número é menor que 10")
# else:
#     print("o número é maior que 50")    

# 3. Peça um ano e verifique se ele é bissexto. Um ano é bissexto se:  for divisível por 4 e não for divisível por 100 ou for divisível por 400.


# 4. Peça usuário e senha.

# Só permita acesso se usuário for "admin" e a senha for "1234".
# Caso contrário, bloqueie.
# Se o usuário for "convidado" e não digitar senha, exiba “Acesso restrito”.
# 5. Peça duas coordenadas (x, y) e verifique a posição do ponto em relação a um quadrado cujos vértices vão de (0,0) até (10, 10).

# Se o ponto estiver estritamente dentro da região, mostre “Dentro do quadrado”.
# Se estiver exatamente em uma das bordas, mostre “Na fronteira”.
# Caso contrário, mostre “Fora do quadrado”.