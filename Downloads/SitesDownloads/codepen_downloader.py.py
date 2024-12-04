from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Mensagem inicial
print("Iniciando o download do conteúdo do site...")

# Configurações das opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em modo sem interface (opcional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Configura o WebDriver com as opções e serviço
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acesse o CodePen desejado
#url = 'https://codepen.io/bcarvalho/pen/gWPvJB'
url ='https://www.ilovepdf.com/pt'
driver.get(url)

# Mens agem informativa
print("Aguarde enquanto o conteúdo do site carrega...")

# Aguarde até que o elemento do conteúdo esteja presente (ajuste conforme necessário)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'result'))  # Mude a classe conforme necessário
    )
except Exception as e:
    print("Erro ao esperar pelo carregamento do conteúdo:", e)

# Captura o HTML da página completa, incluindo o cabeçalho
html_content = driver.page_source

# Caminho para salvar o arquivo
# save_path = r'D:\Projetos\Celio\Marcio_Fernando_Maia\Projetos-Python\Downloads\SitesDownloads\ilovepdf.html'


# Definir o diretório de destino
save_path = r'C:\Users\Marcio Fernando Maia\Downloads\SitesDownloads\ilovepdf.html'



# Salva o conteúdo em um arquivo HTML
with open(save_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

# Fecha o navegador
driver.quit()

# Mensagem de finalização
print(f"Conteúdo do site copiado e salvo com sucesso como '{save_path}'.")
