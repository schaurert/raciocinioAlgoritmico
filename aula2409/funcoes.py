"""
SINTAXE
def nome_funcao (parametros): -> definição
    codigo
    return algum_valor

PARAMETROS E RETURN SAO OPCIONAIS

nome_funcao(parametros) -> chamada
"""

x = 4
y = 2
soma = x + y
print(soma)

#em funcao s parametro e s retorno
def soma():
    x = 4
    y = 2
    soma = x + y
    print(soma)

soma()

#em funcao c parametro e sem retorno
def soma(x,y):
    soma = x + y
    print(soma)

soma(2,4)

#em funcao c parametro e c retorno
def soma(x,y):
    return  x + y

print(soma(4,2))
#ou
#resultado = soma (4, 2)
#print (resultado)

"""
a função nao deve ter mais coisas que a sua responsabildade para que possa ser menos engessada possivel, por isso a última opção é a mais viável para esse caso acima
nao é aconselhado pegar input dentro da função, geralmente faz na funcao main do código
"""

"""
FUNÇÃO MAIN
SINTAXE: 
def main(): -> definicao
    coddigo...
"""

def somar(a,b):
    return a+b

def main():
    a = 4
    b = 2
    

