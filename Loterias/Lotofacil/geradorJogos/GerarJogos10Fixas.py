'''
import pandas as pd
import numpy as np

# Avisar que a criação das planilhas foi iniciada
print("As planilhas começaram a ser criadas, aguarde!")

# Solicitar ao usuário para escolher 10 dezenas fixas, digitadas separadas por vírgula
while True:
    try:
        input_fixas = input("Escolha 10 dezenas fixas entre 1 e 25, separadas por vírgula (ex: 3,7,12,18,25,1,6,9,15,20): ")
        dezenas_fixas = [int(x.strip()) for x in input_fixas.split(",")]
        
        # Validar se o usuário digitou exatamente 10 dezenas, todas entre 1 e 25, e sem repetição
        if len(dezenas_fixas) != 10:
            print("Você deve digitar exatamente 10 dezenas.")
        elif any(dez < 1 or dez > 25 for dez in dezenas_fixas):
            print("As dezenas devem estar entre 1 e 25.")
        elif len(set(dezenas_fixas)) != 10:
            print("As dezenas não podem se repetir.")
        else:
            break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números separados por vírgulas.")

print(f"As dezenas fixas escolhidas foram: {dezenas_fixas}")

# Gerar jogos aleatórios com 5 dezenas adicionais, garantindo que as 10 fixas estejam em todos os jogos
dezenas_restantes = [d for d in range(1, 26) if d not in dezenas_fixas]

# Número de jogos por planilha
num_jogos_por_planilha = 524287

# Gerar jogos aleatórios, garantindo que cada jogo contenha as 10 fixas mais 5 dezenas aleatórias das restantes
jogos = []
while len(jogos) < 2 * num_jogos_por_planilha:
    # Selecionar 5 dezenas aleatórias das restantes
    dezenas_aleatorias = np.random.choice(dezenas_restantes, 5, replace=False)
    # Criar o jogo completo com as 10 fixas e as 5 dezenas aleatórias
    jogo_completo = sorted(dezenas_fixas + list(dezenas_aleatorias))
    jogos.append(jogo_completo)

# Converter a lista de jogos em um DataFrame do Pandas
df_jogos = pd.DataFrame(jogos)

# Verificar se temos combinações suficientes para preencher as duas planilhas
if len(jogos) < 2 * num_jogos_por_planilha:
    print("Não há combinações suficientes para gerar duas planilhas com a quantidade desejada.")
else:
    # Selecionar jogos para a primeira planilha
    selected_jogos1 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
    df_jogos1 = pd.DataFrame([jogos[i] for i in selected_jogos1])

    # Definir o caminho absoluto para salvar os arquivos
    caminho_arquivo_1 = r'D:\MEUSSITESEPROJETOS\Projetos\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_1_10-Fixas.xlsx'
    #caminho_arquivo_1 = r'D:\Projetos\Celio\Marcio_Fernando_Maia\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_1_10-Fixas.xlsx'

    df_jogos1.to_excel(caminho_arquivo_1, index=False, header=False)
    print(f"A primeira planilha foi gerada com {num_jogos_por_planilha} jogos.")

    # Selecionar jogos para a segunda planilha sem duplicação dos jogos da primeira
    jogos_restantes = list(set(range(len(jogos))) - set(selected_jogos1))
    selected_jogos2 = np.random.choice(jogos_restantes, num_jogos_por_planilha, replace=False)
    df_jogos2 = pd.DataFrame([jogos[i] for i in selected_jogos2])

    caminho_arquivo_2 = r'D:\MEUSSITESEPROJETOS\Projetos\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_2_10-Fixas.xlsx'
    # caminho_arquivo_2 = r'D:\Projetos\Celio\Marcio_Fernando_Maia\Projetos-Python\Loterias\Lotofacil\geradorJogos\jogos_lotofacil_2_10-Fixas.xlsx'

    df_jogos2.to_excel(caminho_arquivo_2, index=False, header=False)
    print(f"A segunda planilha foi gerada com {num_jogos_por_planilha} jogos.")

    # Avisar que a criação das planilhas foi concluída
    print("As planilhas foram geradas com sucesso no diretório especificado!")
'''
import pandas as pd
import numpy as np
import os

# Avisar que a criação das planilhas foi iniciada
print("As planilhas começaram a ser criadas, aguarde!")

# Solicitar ao usuário para escolher 10 dezenas fixas, digitadas separadas por vírgula
while True:
    try:
        input_fixas = input("Escolha 10 dezenas fixas entre 1 e 25, separadas por vírgula (ex: 3,7,12,18,25,1,6,9,15,20): ")
        dezenas_fixas = [int(x.strip()) for x in input_fixas.split(",")]
        
        # Validar se o usuário digitou exatamente 10 dezenas, todas entre 1 e 25, e sem repetição
        if len(dezenas_fixas) != 10:
            print("Você deve digitar exatamente 10 dezenas.")
        elif any(dez < 1 or dez > 25 for dez in dezenas_fixas):
            print("As dezenas devem estar entre 1 e 25.")
        elif len(set(dezenas_fixas)) != 10:
            print("As dezenas não podem se repetir.")
        else:
            break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números separados por vírgulas.")

print(f"As dezenas fixas escolhidas foram: {dezenas_fixas}")

# Gerar jogos aleatórios com 5 dezenas adicionais, garantindo que as 10 fixas estejam em todos os jogos
dezenas_restantes = [d for d in range(1, 26) if d not in dezenas_fixas]

# Número de jogos por planilha
num_jogos_por_planilha = 524287

# Gerar jogos aleatórios, garantindo que cada jogo contenha as 10 fixas mais 5 dezenas aleatórias das restantes
jogos = []
while len(jogos) < 2 * num_jogos_por_planilha:
    # Selecionar 5 dezenas aleatórias das restantes
    dezenas_aleatorias = np.random.choice(dezenas_restantes, 5, replace=False)
    # Criar o jogo completo com as 10 fixas e as 5 dezenas aleatórias
    jogo_completo = sorted(dezenas_fixas + list(dezenas_aleatorias))
    jogos.append(jogo_completo)

# Converter a lista de jogos em um DataFrame do Pandas
df_jogos = pd.DataFrame(jogos)

# Localizar a pasta Downloads do sistema
caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Verificar se temos combinações suficientes para preencher as duas planilhas
if len(jogos) < 2 * num_jogos_por_planilha:
    print("Não há combinações suficientes para gerar duas planilhas com a quantidade desejada.")
else:
    # Selecionar jogos para a primeira planilha
    selected_jogos1 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
    df_jogos1 = pd.DataFrame([jogos[i] for i in selected_jogos1])

    # Definir o caminho para salvar o primeiro arquivo
    caminho_arquivo_1 = os.path.join(caminho_downloads, "jogos_lotofacil_1_10-Fixas.xlsx")
    df_jogos1.to_excel(caminho_arquivo_1, index=False, header=False)
    print(f"A primeira planilha foi gerada com {num_jogos_por_planilha} jogos e salva em {caminho_arquivo_1}.")

    # Selecionar jogos para a segunda planilha sem duplicação dos jogos da primeira
    jogos_restantes = list(set(range(len(jogos))) - set(selected_jogos1))
    selected_jogos2 = np.random.choice(jogos_restantes, num_jogos_por_planilha, replace=False)
    df_jogos2 = pd.DataFrame([jogos[i] for i in selected_jogos2])

    # Definir o caminho para salvar o segundo arquivo
    caminho_arquivo_2 = os.path.join(caminho_downloads, "jogos_lotofacil_2_10-Fixas.xlsx")
    df_jogos2.to_excel(caminho_arquivo_2, index=False, header=False)
    print(f"A segunda planilha foi gerada com {num_jogos_por_planilha} jogos e salva em {caminho_arquivo_2}.")

    # Avisar que a criação das planilhas foi concluída
    print("As planilhas foram geradas com sucesso na pasta Downloads!")
