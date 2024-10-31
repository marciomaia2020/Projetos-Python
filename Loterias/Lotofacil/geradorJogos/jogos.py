
import pandas as pd
import numpy as np
from itertools import combinations


# Avisar que a criação das planilhas foi iniciada
print("As planilhas começaram a ser criadas aguarde!")

# Gerar todas as combinações de 15 dezenas entre 25
dezenas = list(range(1, 26))  # Dezenas de 1 a 25
jogos = list(combinations(dezenas, 15))

# Número de jogos por planilha
num_jogos_por_planilha = 524287

# Selecionar jogos para a primeira planilha
selected_jogos1 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
df_jogos1 = pd.DataFrame([jogos[i] for i in selected_jogos1])

# Definir o caminho absoluto para salvar os arquivos
caminho_arquivo_1 = r'D:\MEUSSITESEPROJETOS\Projetos\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_1.xlsx'
caminho_arquivo_2 = r'D:\MEUSSITESEPROJETOS\Projetos\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_2.xlsx'

# Salvar a primeira planilha
df_jogos1.to_excel(caminho_arquivo_1, index=False, header=False)

# Selecionar jogos para a segunda planilha
selected_jogos2 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
df_jogos2 = pd.DataFrame([jogos[i] for i in selected_jogos2])

# Salvar a segunda planilha
df_jogos2.to_excel(caminho_arquivo_2, index=False, header=False)

# Avisar que a criação das planilhas foi concluída
print("As planilhas foram geradas com sucesso no diretório especificado!")
