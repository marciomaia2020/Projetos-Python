#print

"""
print("Olá mundo!")
print("Marcio Fernando Maia")
print("num1*num2")


print(f"Meu nome é {nome}.")
print("Eu gosto de programação")
print("Eu tenho 55 anos")
print("Marcio gosta de programação e tem 55 anos")


var nome = "Márcio Fernando Maia"
var gosto_de = "programação"
var idade = "55 anos"

import sys
print(sys.version)


#não pode ter espaços na parte de cima somente
if 5 > 2:
print("5 é maior que 2!")

       if 5 > 2:
print("Five is greater than two!")  


print('Ola pessoal')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa1.saudacao()
"""

"""
class Animal:
    def __init__(self, raca, cor, patas):
        self.raca = raca
        self.cor = cor
        self.patas = patas

    def informacao(self):
        print(f"Olá, a raça do cachorro é {self.raca} e sua cor é {self.cor}. Lembrando que todo cão tem {self.patas} patas!")


# Criando um objeto da classe Animal
Animal1 = Animal("Puddle", "Amarela", 4)
Animal2 = Animal("Burdogue", "Preto & Branco", 5)
Animal1.informacao()
Animal2.informacao()
"""

"""
class Animal:
    def __init__(self, raca, cor, patas):
        self.raca = raca
        self.cor = cor
        self.patas = patas

    def informacao(self):
        print(f"Olá, a raça do cachorro é {self.raca} e sua cor é {self.cor}. Lembrando que todo cão tem {self.patas} patas!")


# Capturando as informações do usuário
raca = input("Digite a raça do cachorro: ")
cor = input("Digite a cor do cachorro: ")
patas = int(input("Digite o número de patas do cachorro: "))

# Criando um objeto da classe Animal com as informações fornecidas pelo usuário
animal1 = Animal(raca, cor, patas)
animal1.informacao()
"""

class Animal:
    def __init__(self, raca, cor, patas):
        self.raca = raca
        self.cor = cor
        self.patas = patas

    def informacao(self):
        print(f"Olá, a raça do cachorro é {self.raca} e sua cor é {self.cor}. Lembrando que todo cão tem {self.patas} patas!")

# Função para capturar informações do usuário e criar um objeto Animal
def criar_animal():
    raca = input("Digite a raça do cachorro: ")
    cor = input("Digite a cor do cachorro: ")
    patas = int(input("Digite o número de patas do cachorro: "))
    return Animal(raca, cor, patas)

# Capturando as informações do usuário para o primeiro animal
print("Informações do primeiro animal:")
animal1 = criar_animal()

# Capturando as informações do usuário para o segundo animal
print("\nInformações do segundo animal:")
animal2 = criar_animal()

# Exibindo as informações dos dois animais
animal1.informacao()
animal2.informacao()