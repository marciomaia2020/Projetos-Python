#Ciência de Dados


#9. Pandas, NumPy e Bibliotecas de Gráficos
# Análise de dados com Pandas e NumPy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = np.random.rand(10, 3)
df = pd.DataFrame(dados, columns=['A', 'B', 'C'])
df.plot(kind='bar')
plt.show()


#10. Obtenção e Tratamento de Dados
# Obtenção e tratamento de dados
import pandas as pd

df = pd.read_csv('dados.csv')
df.fillna(0, inplace=True)
print(df)


#Desenvolvimento Web


#9. Orientação a Objetos
# Fundamentos de orientação a objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

pessoa = Pessoa("Alice", 30)
print(pessoa.saudacao())


#10. Integração Backend Frontend
# Uso de Flask para desenvolvimento web
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo!"

if __name__ == '__main__':
    app.run(debug=True)


#Automaçãos, Tabelas

# Manipulação de arquivos
import os

caminho = 'caminho/para/arquivo.txt'
with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#10. Ferramentas de Automação

# Web Scraping com BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, 'html.parser')
print(soup.title.text)
