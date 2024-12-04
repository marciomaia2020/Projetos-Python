from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

# Caminho para o executável do Google Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Caminho para o ChromeDriver
chromedriver_path = r"D:\Python_\Selenium\chromedriver-win64\chromedriver.exe"

# Lista de URLs que você quer abrir
urls = [
    "https://alanatccaesthete.netlify.app/",
    "https://diogoapenaaas.github.io/TCCdiogo/",
    "https://melrobeth.github.io/TCCElizabeth/",
    "https://gabiasouza.github.io/gabietccc/",
    "https://gabiiduarte.github.io/filme-2/#",
    "https://giovanaliveira.github.io/TCCGIOVANA/",
    "https://shinenight.netlify.app/",
    "https://iasmin000.github.io/TCCiasmin/index.html",
    "https://isabella9823.github.io/IsabellaTCC/",
    "https://josexdl.github.io/tccjose/",
    "https://lehhestevess.github.io/lehhestevess-newsite/index.html",
    "https://lorerds2.github.io/Lorenatcc/",
    "https://mirellasfs.github.io/tccmirella/",
    "https://nicholastcc.netlify.app/",
    "https://cainelles.github.io/tccpaulo/",
    "https://vinicius223.github.io/TCCvinicius/"
]

# Configurações para o navegador Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abre o navegador maximizado
chrome_options.binary_location = chrome_path  # Define o Chrome como navegador

# Inicia o navegador Chrome com o ChromeDriver
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre a primeira URL
driver.get(urls[0])

# Abre as outras URLs em novas abas, esperando 5 segundos entre cada uma
for url in urls[1:]:
    driver.execute_script("window.open(arguments[0], '_blank');", url)  # Abre uma nova aba
    time.sleep(2)  # Espera 5 segundos antes de abrir o próximo site

# Mantém o navegador aberto até que o usuário o feche manualmente
input("Pressione Enter para fechar o navegador...")

