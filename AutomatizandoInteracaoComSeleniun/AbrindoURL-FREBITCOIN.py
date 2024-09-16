from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurações para o navegador Firefox
firefox_options = Options()
firefox_options.add_argument("--start-maximized")  # Abre o navegador maximizado

# Especificar o caminho para o Firefox manualmente
firefox_path = r"C:\\Program Files\\Firefox Developer Edition\\firefox.exe"  # Substitua pelo caminho correto do seu Firefox
firefox_options.binary_location = firefox_path

# Caminho para o geckodriver (ajuste para o seu ambiente)
geckodriver_path = r"D:\\Programas\\seleniumDrivers_\\geckodriver-v0.35.0-win32\\geckodriver.exe"  # Altere para o local onde você baixou o geckodriver

# Inicia o navegador
service = FirefoxService(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

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
    # Fecha o navegador após um tempo (opcional)
    time.sleep(5)  # Espera um pouco para que a ação ocorra
    driver.quit()
