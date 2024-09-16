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
url = "https://cmspweb.ip.tv/"
driver.get(url)

# Espera o site carregar completamente
time.sleep(5)  # Ajuste o tempo se necessário


# Clica no botão com o id "access-teacher"
button = driver.find_element(By.ID, "access-teacher")
button.click()

# Encontre o campo de entrada pelo ID e insira o dado
input_field = driver.find_element(By.ID, "rg-teacher")
input_field.send_keys("18833323x")


# Encontre o campo de entrada pelo ID e insira o dado
input_field = driver.find_element(By.ID, "password-teacher")
input_field.send_keys("965013Mfm@@")


# Clica no botão de login
login_button = driver.find_element(By.ID, "btn-login-teacher")
login_button.click()


# Clica no botão de login quando estiver clicável
#login_button = WebDriverWait(driver, 10).until(
#    EC.element_to_be_clickable((By.ID, "btn-login-teacher"))
#)
#login_button.click()


# Fecha o navegador após um tempo (opcional)
time.sleep(5000)  # Espera um pouco para que a ação ocorra
driver.quit()
