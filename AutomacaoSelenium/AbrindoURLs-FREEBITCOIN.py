from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho para o executável do Google Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Caminho para o ChromeDriver
chromedriver_path = r"D:\Python_\Selenium\chromedriver-win64\chromedriver.exe"

# Configurações para o navegador Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abre o navegador maximizado
chrome_options.binary_location = chrome_path  # Define o Chrome como navegador

# Inicia o navegador Chrome com o ChromeDriver
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre o site
url = "https://freebitco.in"
driver.get(url)

# Espera o site carregar completamente e localiza o botão de login
try:
    # Espera até que o botão esteja clicável (máximo 10 segundos)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "free_play_form_button"))
    )
    login_button.click()
    print("Botão clicado com sucesso!")
except Exception as e:
    print(f"Erro ao clicar no botão: {e}")
finally:
    #Fecha o navegador após um tempo (opcional)
    time.sleep(250)  # Espera um pouco para que a ação ocorra
    driver.quit()