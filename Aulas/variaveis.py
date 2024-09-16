#print

#Criando variável simples. (NOTAR QUE AQUI IRÁ SER IMPRESSO O VALOR ATRIBUIDO A LETRA Z)
x = 5
y = 10
z = x + y
print(z)

#Criando variável simples. (NOTAR QUE AQUI IRÁ SER IMPRESSO A LETRA Z)
x = 5
y = 10
z = x + y
print("z")

#O valor x assume o ultimo valor a ele atribuido
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Posso especificar o tipo de dados de uma variável
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#Posso obter o tipo de dados de uma variável
x = 5
y = "Márcio"
print(type(x))
print(type(y))

#Aspas Simples ou Dupla?
x = "John"
# is the same as
x = 'John'


"""
Um nome de variável deve começar com uma letra ou o caractere sublinhado
Um nome de variável não pode começar com um número
Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9 e _)
Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (idade, Idade e IDADE são três variáveis ​​diferentes)
Um nome de variável não pode ser nenhuma das palavras-chave do Python .
"""

#Variáveis legais
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Variáveis ilegais
#   2myvar = "John"
#   my-var = "John"
#   my var = "John"


#Camel Case (Cada palavra, exceto a primeira, começa com letra maiúscula:)
myVariableName = "John"

#Pascal Case (Cada palavra começa com uma letra maiúscula:)
MyVariableName = "John"

#Snake Case (Cada palavra é separada por um caractere sublinhado:)
my_variable_name = "John"


#Letra Maiúscula ou minuúscula (Isso criará duas variáveis:)
a = 4
A = "Sally"  #A will not overwrite a


#Python permite que você atribua valores a várias variáveis ​​em uma linha:
x, y, z = "Orange", "Banana", "Cherry"
#print(x)
#print(y)
#print(z)

#Pode se atribuir o mesmo valor a várias variáveis ​​em uma linha:
x = y = z = "Orange"


#Descompacte uma coleção (Se você tem uma coleção de valores em uma lista, tupla etc. Python permite que você extraia os valores em variáveis.)
#Isso é chamado de unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
#print(x)
#print(y)
#print(z)


pecas = ["roda", "aro","pneu","camara"]
a, b, c, d = pecas
#print(a)
#print(b)
#print(c)
#print(d)




#Variáveis ​​de saída (A função Python print()é frequentemente usada para gerar variáveis.)
x = "Python é incrível"
print(x)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Na print()função, você gera diversas variáveis, separadas por uma vírgula:
x = "Python"
y = "é"
z = "incrível"
print(x, y, z)#É a mesma coisa do código abaixo

#Você também pode usar o +operador para gerar múltiplas variáveis:
x = "Python "
y = "é "
z = "incrível"
print(x + y + z)#É a mesma coisa do código acima, note os espaço no fim de cada palavra
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#Para números, o + caractere funciona como um operador matemático:
x = 5
y = 10
print(x + y)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Na print() função, quando você tenta combinar uma string e um número com o + operador, o Python apresentará um erro:
#x = "João é "
#y = 10
#print(x + y)

#Para isso atribua o valor numerico como string
x = "João e "
y = "10"
print(x + y)

#A melhor maneira de gerar múltiplas variáveis ​​na print()função é separá-las com vírgulas, o que suporta até mesmo diferentes tipos de dados:
#x = "João é "
#y = 10
#print(x , y)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Variáveis ​​globais (Crie uma variável fora de uma função e use-a dentro da função)

x = "incrível"

def myfunc():
  print("Python é " + x)

myfunc()


#Palavra-chave correta (global) para fazer com que a variável x pertença ao escopo global.
def myfunc():
    global x
    x = "fantastic"
    