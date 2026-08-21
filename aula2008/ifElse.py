#IF/ELSE

# temp = float(input("Digite a temperatura,: "))

# if temp > 25:
#     print("Está quente")
# else:
#     print("está frio")

# print("-----------------------------")

# num = int(input("Digite um número: "))

# if num % 2 == 0:
#     print("O número é par")
# else: 
#     print("o número é ímpar")

#ELIF

temp = float(input("Digite a temperatura: "))

if temp >= 25: 
    print("temperatura está quente")

elif temp >= 18 and temp < 25:
    print("temperatura está amena")

else:
    print("temperatura está fria")

