#APIs prontas
# Utilizando uma API existente
import requests

resposta = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
dados = resposta.json()
print(dados)


#Interpretar documentação
# Interpretação de documentação é essencial para trabalhar com APIs
# Exemplo: https://requests.readthedocs.io/en/latest/


#Exemplos de API´s
#Cotação do dollar
#Clima Tempo
