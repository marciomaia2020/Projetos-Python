import pandas as pd
import numpy as np
from itertools import combinations

# Gerar todas as combinações de 15 dezenas entre 25
dezenas = list(range(1, 26))  # Dezenas de 1 a 25
jogos = list(combinations(dezenas, 15))

# Número de jogos por planilha
num_jogos_por_planilha = 524288

# Selecionar jogos para a primeira planilha
selected_jogos1 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
df_jogos1 = pd.DataFrame([jogos[i] for i in selected_jogos1])

# Salvar a primeira planilha
df_jogos1.to_excel('jogos_lotofacil_1.xlsx', index=False, header=False)

# Selecionar jogos para a segunda planilha
selected_jogos2 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
df_jogos2 = pd.DataFrame([jogos[i] for i in selected_jogos2])

# Salvar a segunda planilha
df_jogos2.to_excel('jogos_lotofacil_2.xlsx', index=False, header=False)
