import webbrowser
import time

# Lista de URLs que você deseja abrir
urls = [
    "https://portifoliodomaia.netlify.app/docs/python/html/apostilas_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/cronograma_estudo_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/problemas_resolvidos_em_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/mapa_do_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/sites_para_deployment_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/funcoes_especiais_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/resumo_web_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/integra%C3%A7%C3%A3o_de_APIs_e_Servi%C3%A7os_Externos.html",
    "https://portifoliodomaia.netlify.app/docs/python/html/ambientes_virtuais_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/flask_extensions",
    "https://portifoliodomaia.netlify.app/docs/python/html/resumo_web_python_explicacao",
    "https://portifoliodomaia.netlify.app/docs/python/html/resumo_web_python_codigos",
    "https://portifoliodomaia.netlify.app/docs/python/html/tutorial_manipulacao_python",
    "https://portifoliodomaia.netlify.app/docs/python/html/dependencias_python",
]

# Função para abrir as URLs
def abrir_urls(urls, delay=5):
    for url in urls:
        webbrowser.open(url)
        #webbrowser.get('firefox').open(url) # Abre uma URL em um navegador especifico.
        print(f"Abrindo: {url}")
        time.sleep(delay)  # Espera um pouco antes de abrir a próxima URL

# Chamada da função
abrir_urls(urls, delay=3)  # 3 segundos de delay entre cada URL


"""
Explicação
Importação dos Módulos:

webbrowser: Para abrir as URLs no navegador.
time: Para adicionar um delay entre as aberturas das URLs.
Lista de URLs:

urls: Uma lista contendo todas as URLs que você deseja abrir.
Função abrir_urls:

Recebe uma lista de URLs e um parâmetro opcional delay que especifica o tempo de espera (em segundos) entre a abertura de cada URL.
Itera sobre cada URL na lista, abre-a no navegador padrão e imprime uma mensagem indicando qual URL está sendo aberta.
Usa time.sleep(delay) para esperar o tempo especificado antes de abrir a próxima URL.
Rodando o Script
Para executar o script:

Salve o código em um arquivo, por exemplo, abrir_urls.py.
Abra um terminal ou prompt de comando.
Navegue até o diretório onde o arquivo foi salvo.
Execute o script com o comando:


Este script abrirá cada URL na lista no navegador padrão, com um delay de 3 segundos entre cada abertura. Você pode ajustar o tempo de delay conforme necessário.

Considerações
Certifique-se de que o navegador padrão esteja configurado corretamente no seu sistema.
Se desejar abrir as URLs em um navegador específico, pode usar webbrowser.get('chrome').open(url) ou webbrowser.get('firefox').open(url) em vez de webbrowser.open(url).
Tenha cuidado ao abrir muitas URLs automaticamente, pois isso pode sobrecarregar o navegador ou a rede.



# URL da página que você deseja abrir
url = "http://www.exemplo.com"

# Abre a URL no navegador padrão
webbrowser.open(url)

# Abre a URL no Google Chrome
webbrowser.get('chrome').open(url)

# Abre a URL no Mozilla Firefox
webbrowser.get('firefox').open(url)

# Abre a URL em uma nova aba no navegador padrão
webbrowser.open_new_tab(url)

# Abre a URL em uma nova janela no navegador padrão
webbrowser.open_new(url)


"""
