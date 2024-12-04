import pandas as pd
import numpy as np
from itertools import combinations

# Avisar que o processo foi iniciado
print("Iniciando o processo de criação das planilhas. Isso pode levar alguns minutos, dependendo do volume de combinações.")

# Gerar todas as combinações de 15 dezenas entre 25
print("\nGerando todas as combinações possíveis de 15 dezenas a partir de 25. Por favor, aguarde...")
dezenas = list(range(1, 26))  # Dezenas de 1 a 25
jogos = list(combinations(dezenas, 15))
print(f"✅ Total de combinações possíveis geradas: {len(jogos)} jogos.")

# Número de jogos por planilha
num_jogos_por_planilha = 524287

# Selecionar jogos para a primeira planilha
print("\nSelecionando jogos aleatórios para a primeira planilha...")
selected_jogos1 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
df_jogos1 = pd.DataFrame([jogos[i] for i in selected_jogos1])
print(f"✅ {num_jogos_por_planilha} jogos foram selecionados para a primeira planilha.")

# Definir os caminhos absolutos para salvar os arquivos
caminho_arquivo_1 = r'D:\MEUSSITESEPROJETOS\Projetos\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_1.xlsx'
caminho_arquivo_2 = r'D:\MEUSSITESEPROJETOS\Projetos\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_2.xlsx'

# Salvar a primeira planilha
print("\nSalvando a primeira planilha no local especificado...")
df_jogos1.to_excel(caminho_arquivo_1, index=False, header=False)
print(f"✅ A primeira planilha foi salva com sucesso em: {caminho_arquivo_1}")

# Selecionar jogos para a segunda planilha
print("\nSelecionando jogos aleatórios para a segunda planilha...")
selected_jogos2 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
df_jogos2 = pd.DataFrame([jogos[i] for i in selected_jogos2])
print(f"✅ {num_jogos_por_planilha} jogos foram selecionados para a segunda planilha.")

# Salvar a segunda planilha
print("\nSalvando a segunda planilha no local especificado...")
df_jogos2.to_excel(caminho_arquivo_2, index=False, header=False)
print(f"✅ A segunda planilha foi salva com sucesso em: {caminho_arquivo_2}")

# Avisar que o processo foi concluído
print("\n🎉 O processo de criação das planilhas foi concluído com sucesso!")
print("Você pode agora acessar os arquivos gerados nos diretórios especificados.")
