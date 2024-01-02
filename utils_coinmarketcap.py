from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

nombres_crypto = list()
capitalizaciones_de_mercado = list()
cantidades_maxima_tokens = list()
simbolos = list()
rankings = list()
precios = list()
volumenes = list()


def create_browser():
  #Opciones de navegacion
  options = webdriver.ChromeOptions()
  options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
  options.add_argument('--disable-gpu')
  options.add_argument('--no-sandbox') # # Bypass OS security model
  options.add_argument('start-maximized')
  options.add_argument('disable-infobars')
  options.add_argument("--disable-extensions")
  # options.add_argument('--disk-cache-dir=/Users/mylo/Documents/Cursos/Python/Selenium/cache')

  driver_path = '/Users/mylo/Documents/Cursos/Python/Selenium/webdriver/chrome-headless-shell-mac-x64/chrome-headless-shell'
  options.path = driver_path

  browser = webdriver.Chrome(options)
  browser.get('https://coinmarketcap.com')
  browser.find_elements(By.CSS_SELECTOR, '.cmc-table tbody tr')
  return browser;

def prepare_table_results(browser):
  # Botón cookies
  WebDriverWait(browser, 10)\
  .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[3]')))\
  .click()
  # Botón personalizar
  WebDriverWait(browser, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/button[2]')))\
    .click()
  # Botón acciones en circulación
  WebDriverWait(browser, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div[1]/span/div[5]/div[2]/span[1]')))\
    .click()
  #Botón acciones totales
  WebDriverWait(browser, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div[1]/span/div[5]/div[2]/span[2]')))\
    .click()
  # Acciones máximas
  WebDriverWait(browser, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div[1]/span/div[5]/div[2]/span[3]')))\
    .click()
  # Botón Guardar columnas
  WebDriverWait(browser, 20)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[3]/div/button[2]')))\
    .click()
  # Tabla de resultados
  WebDriverWait(browser, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cmc-table tbody tr')))

def each_rows(max_rows, browser):
  #Usada para recorrer toda la tabla y cargar todas las filas 
  for i in range(1, max_rows+1):
    
    rowSelected = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{}]".format(i))
    
    browser.execute_script("arguments[0].scrollIntoView();", rowSelected)
    time.sleep(0.2)
    if i % 25:
      table = browser.find_elements(By.CSS_SELECTOR, '.cmc-table tbody tr')
  return table

    
def build_object(fila):
  # Construimos el objeto y cargamos cada propiedad en su lista correspondiente
  ranking = fila.find_element(By.XPATH, './td[2]/p')
  nombre = fila.find_element(By.XPATH, './td[3]/div/a/div/div/div/p')
  precio = fila.find_element(By.XPATH, './td[4]/div/a/span')
  capitalizacion = fila.find_element(By.XPATH, './td[8]/p/span[2]')
  simbolo = fila.find_element(By.XPATH, './td[11]')
  acciones_max = fila.find_element(By.XPATH, './td[11]')
  volumen = fila.find_element(By.XPATH, './td[9]/div/a/p')
  
  rankings.append(ranking.text)
  nombres_crypto.append(nombre.text)
  precios.append(precio.text)
  capitalizaciones_de_mercado.append(capitalizacion.text)
  cantidades_maxima_tokens.append(acciones_max.text.split()) #WIP
  simbolos.append(simbolo.text.split()) #WIP
  volumenes.append(volumen.text)

def build_export_to_csv():
  df = pd.DataFrame({'Ranking': rankings, 'Simbolo': simbolos, 'Nombre': nombres_crypto, 'Cantidad Máxima de tokens': cantidades_maxima_tokens, 'Capitalización Total de Mercado': capitalizaciones_de_mercado, 'Precio': precios, 'Volumen 24h': volumenes})
  print(df)
  df.to_csv('NTokens_Crypto_CoinMarketCap.csv', index=False)