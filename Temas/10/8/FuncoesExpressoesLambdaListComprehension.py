#Funções
# Definindo uma função
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Alice"))


#Expressões Lambda
# Funções lambda
soma = lambda a, b: a + b
print(soma(3, 4))


#List Comprehension
# List comprehension
quadrados = [x ** 2 for x in range(10)]
print(quadrados)
