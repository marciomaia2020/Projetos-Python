import os
import pandas as pd
import numpy as np

# Obter o caminho da pasta Downloads do usuário
caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Avisar que a criação das planilhas foi iniciada
print("Iniciando o processo de criação das planilhas. Isso pode levar alguns minutos, dependendo da quantidade de jogos.")

# Solicitar ao usuário para escolher 5 dezenas fixas, digitadas separadas por vírgula
while True:
    try:
        print("\nPor favor, escolha 5 dezenas fixas entre 1 e 25. Essas dezenas aparecerão em todos os jogos gerados.")
        input_fixas = input("Digite as dezenas separadas por vírgula (ex: 3,7,12,18,25): ")
        dezenas_fixas = [int(x.strip()) for x in input_fixas.split(",")]

        # Validar se o usuário digitou exatamente 5 dezenas, todas entre 1 e 25, e sem repetição
        if len(dezenas_fixas) != 5:
            print("⚠️ Você deve digitar exatamente 5 dezenas. Tente novamente.")
        elif any(dez < 1 or dez > 25 for dez in dezenas_fixas):
            print("⚠️ As dezenas devem estar entre 1 e 25. Tente novamente.")
        elif len(set(dezenas_fixas)) != 5:
            print("⚠️ As dezenas não podem se repetir. Tente novamente.")
        else:
            print(f"✅ As dezenas fixas escolhidas foram: {dezenas_fixas}")
            break  # Sai do loop se a entrada for válida
    except ValueError:
        print("⚠️ Entrada inválida. Certifique-se de digitar números separados por vírgulas.")

# Gerar todas as combinações de 10 dezenas entre as 20 restantes (25 - 5 = 20)
dezenas_restantes = [d for d in range(1, 26) if d not in dezenas_fixas]
print("\nGerando as combinações de dezenas aleatórias. Isso pode demorar um pouco...")

# Combinar as dezenas fixas com combinações aleatórias de 10 dezenas das 20 restantes
jogos = []

# Número de jogos por planilha
num_jogos_por_planilha = 524287

# Gerar um número total de jogos desejado
while len(jogos) < 2 * num_jogos_por_planilha:
    # Selecionar 10 dezenas aleatórias das restantes
    dezenas_aleatorias = np.random.choice(dezenas_restantes, 10, replace=False)
    # Criar um jogo que combina as 5 fixas com as 10 aleatórias
    jogo_completo = sorted(dezenas_fixas + list(dezenas_aleatorias))
    jogos.append(jogo_completo)

print(f"✅ Combinações geradas com sucesso! Total de {len(jogos)} jogos criados.")

# Converter a lista de jogos em um DataFrame do Pandas
df_jogos = pd.DataFrame(jogos)

# Verificar se temos combinações suficientes para preencher as duas planilhas
if len(jogos) < 2 * num_jogos_por_planilha:
    print("⚠️ Não há combinações suficientes para gerar duas planilhas com a quantidade desejada.")
else:
    print("\nDividindo os jogos em duas planilhas e salvando os arquivos. Aguarde...")

    # Selecionar jogos para a primeira planilha
    selected_jogos1 = np.random.choice(len(jogos), num_jogos_por_planilha, replace=False)
    df_jogos1 = pd.DataFrame([jogos[i] for i in selected_jogos1])

    # Salvar a primeira planilha na pasta Downloads
    caminho_arquivo_1 = os.path.join(caminho_downloads, "jogos_lotofacil_1_5-Fixas.xlsx")
    df_jogos1.to_excel(caminho_arquivo_1, index=False, header=False)
    print(f"✅ A primeira planilha foi gerada com {num_jogos_por_planilha} jogos.")
    print(f"   Local: {caminho_arquivo_1}")

    # Selecionar jogos para a segunda planilha sem duplicação dos jogos da primeira
    jogos_restantes = list(set(range(len(jogos))) - set(selected_jogos1))
    selected_jogos2 = np.random.choice(jogos_restantes, num_jogos_por_planilha, replace=False)
    df_jogos2 = pd.DataFrame([jogos[i] for i in selected_jogos2])

    # Salvar a segunda planilha na pasta Downloads
    caminho_arquivo_2 = os.path.join(caminho_downloads, "jogos_lotofacil_2_5-Fixas.xlsx")
    df_jogos2.to_excel(caminho_arquivo_2, index=False, header=False)
    print(f"✅ A segunda planilha foi gerada com {num_jogos_por_planilha} jogos.")
    print(f"   Local: {caminho_arquivo_2}")

    # Avisar que a criação das planilhas foi concluída
    print("\n🎉 As planilhas foram geradas com sucesso na pasta Downloads!")
    print("Você pode agora acessar os arquivos gerados e utilizá-los como desejar.")
