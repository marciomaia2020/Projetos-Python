import webbrowser
import time

# Lista de URLs que você deseja abrir
urls = [
    "https://www.fiec.com.br/site/procsel/listar.do",
    "https://urhsistemas.cps.sp.gov.br/dgsdad/SelecaoPublica/",
    "http://delimeira.educacao.sp.gov.br",
    "http://www.educacao.sp.gov.br/",
    "https://sed.educacao.sp.gov.br/",
    "https://lanahv.github.io/lanatcc/",
    "https://diogoapenaaas.github.io/TCCdiogo/",
    "https://melrobeth.github.io/TCCElizabeth/",
    "https://gabiasouza.github.io/gabietccc/",
    "https://gabiiduarte.github.io/gabitcc/",
    "https://giovanaliveira.github.io/Giovana-TCC/",
    "https://shinenight.netlify.app/#",
    "https://iasmin000.github.io/TCCiasmin/",
    "https://isabella9823.github.io/IsabellaTCC/",
    "https://josexdl.github.io/tccjose/",
    "https://lehhestevess.github.io/lehhestevess-newsite/index.html",
    "https://lorerds2.github.io/Lorenatcc/",
    "https://mirellasfs.github.io/tccmirella/",
    "https://tccnicholas.netlify.app/",
    "https://cainelles.github.io/tccpaulo/inicio.html",
    "https://vinicius223.github.io/TCCvinicius/",
 
]

# Função para abrir as URLs
def abrir_urls(urls, delay=5):
    for url in urls:
        webbrowser.open(url)
        #webbrowser.get('firefox').open(url) Abre uma URL em um navegador especifico.
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
