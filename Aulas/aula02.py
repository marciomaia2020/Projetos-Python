"""
Escreva um programa que retorne o valor hora de um funcionário
com base no su salário mensal e hotas trabalhadas por mês
"""

def calcular_valor_hora(salario_mensal, horas_trabalhadas):
    #Tratando o erro
    if horas_trabalhadas == 0:
        return "O valor da horas trabalhadas não pode ser igual a zero"
    valor_hora = salario_mensal / horas_trabalhadas
    return valor_hora

#Caso de uso
salario_mensal = 3000.00
horas_trabalhadas = 160


#Chamando a função
valor_hora = calcular_valor_hora(salario_mensal, horas_trabalhadas)
print (f"R$: {valor_hora:.2f} é o valor hora.")
