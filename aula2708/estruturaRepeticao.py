# #exemplo 1
# cont = 0
# while cont <= 3:
#     print("Olá")
#     cont = cont +1

# # exemplo 2
# cont = 3
# while cont > 0:
#     print("Olá")
#     cont -=1

#colinha A4 frente impressa ou manuscrita

#teste de mesa faz até a condição ficar F
#teste de mesa
#tabela verdade


#pratica
# 1. imprimir numero de 1 a 10
# cont = 1
# while cont <= 10:
#     print(cont)
#     cont +=1

# # 1. imprimir numero de 10 a 1
# cont = 10
# while cont >= 1:
#     print(cont)
#     cont -=1

#37

# num = int(input("digite um numero: "))
# cont = 0

# while cont <=10:
#     print(num*cont)
#     cont +=1

#.isDigit() verifica se é numerico - V p numero e F p str

palavra = input("Digite uma palavra. Ela deve conter entre 3 e 10 caracteres: ")
qnt = len(palavra)

while qnt < 3 or qnt > 10:
    print("A palavra deve conter entre 3 e 10 caracteres.")
    palavra = input ("Digite novamente: ")
    qnt = len(palavra)

print(f"A palavra que você digitou é {palavra} e tem {qnt} caracteres")