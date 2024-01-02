#Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

def initCrypto():
  #Opciones de navegacion
  options = webdriver.ChromeOptions()
  # options.add_argument('--start-maximized')
  # options.add_argument("--incognito")
  options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
  options.add_argument('--disable-gpu')
  # options.add_argument('--headless')
  options.add_argument('--no-sandbox') # # Bypass OS security model
  options.add_argument('start-maximized')
  options.add_argument('disable-infobars')
  options.add_argument("--disable-extensions")
  options.add_argument('--disk-cache-dir=/Users/mylo/Documents/Cursos/Python/Selenium/cache')

  driver_path = '/Users/mylo/Documents/Cursos/Python/Selenium/webdriver/chrome-headless-shell-mac-x64/chrome-headless-shell'
  options.path = driver_path

  driver = webdriver.Chrome(options)

  # Inicializamos el navegador

  driver.get('https://coingecko.com')
  lista_links = []
  lista_metricas = []
  nombres_crypto = list()
  capitalizaciones_de_mercado = list()
  cantidades_maxima_tokens = list()
  rankings = list()
  precios = list()
  volumenes = list()
  
  tabla = driver.find_elements(By.XPATH, '/html/body/div[2]/main/div/div[5]/table/tbody/tr')
  xpaths_nombre_cryptos = [
          '/html/body/div[3]/main/div/div/div/div/div[2]/h1/span[1]',
          '/html/body/div[3]/main/div[2]/div[1]/div/div[1]/div[2]/h1/span[1]'
      ]
  xpaths_capitalizaciones_de_mercado = [
    '/html/body/div[3]/main/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/span[2]/span',
    '/html/body/div[3]/main/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/span[2]/span'
  ]
  xpaths_cantidades_maximas_de_tokens = [
    '/html/body/div[3]/main/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[3]/span[2]',
    '/html/body/div[3]/main/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[3]/span[2]'
  ]

  xpaths_precios = [
     '/html/body/div[3]/main/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td/span/span',
     '/html/body/div[3]/main/div[4]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td/span/span'
  ]

  xpaths_volumenes = [
     '/html/body/div[3]/main/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span[2]/span',
     '/html/body/div[3]/main/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span[2]/span'
  ]

  xpaths_rankings = [
     '/html/body/div[3]/main/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[5]/td/span',
     '/html/body/div[3]/main/div[4]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[5]/td/span'
  ]
  
  for fila in tabla:
    enlace = fila.find_element(By.XPATH, './td[3]/a')
    
    # Obtener el enlace href
    enlace_url = enlace.get_attribute('href')
    lista_links.append(enlace_url)
    # Imprimir la URL del enlace
    # print("Enlace:", enlace_url)
  for link in lista_links:
    try:
      driver.get(link)
      
      for xpath in xpaths_nombre_cryptos:
        try:
            nombre_element = driver.find_element(By.XPATH, xpath)
            nombre_crypto = nombre_element.text
            break  # Detener el bucle si se encuentra el nombre de la criptomoneda
        except NoSuchElementException:
            continue  # Pasar al siguiente XPath si no se encuentra el elemento

      
      if nombre_crypto:
        nombres_crypto.append(nombre_crypto)
      else:
        print("No se encontró el nombre de la criptomoneda.")
      # print(nombre_crypto)                                   

      for xpath in xpaths_capitalizaciones_de_mercado:
        try:
            capitalizacion_de_mercado = driver.find_element(By.XPATH, xpath)
            capitalizacion_de_mercado = capitalizacion_de_mercado.text
            break  # Detener el bucle si se encuentra el nombre de la criptomoneda
        except NoSuchElementException:
            continue  # Pasar al siguiente XPath si no se encuentra el elemento
      
      if capitalizacion_de_mercado:
        capitalizaciones_de_mercado.append(capitalizacion_de_mercado)
      else:
        print("No se encontró la capitalización de mercado de la criptomoneda.")


      for xpath in xpaths_cantidades_maximas_de_tokens:
        try:
            cantidad_maxima_tokens = driver.find_element(By.XPATH, xpath)
            cantidad_maxima_tokens = cantidad_maxima_tokens.text
            break  # Detener el bucle si se encuentra el nombre de la criptomoneda
        except NoSuchElementException:
            continue  # Pasar al siguiente XPath si no se encuentra el elemento
      
      if cantidad_maxima_tokens:
        cantidades_maxima_tokens.append(cantidad_maxima_tokens)
      else:
        print("No se encontró la cantidad máxima de tokens de la criptomoneda.")


      for xpath in xpaths_rankings:
        try:
            ranking_element = driver.find_element(By.XPATH, xpath)
            ranking_crypto = ranking_element.text
            break  # Detener el bucle si se encuentra el nombre de la criptomoneda
        except NoSuchElementException:
            continue  # Pasar al siguiente XPath si no se encuentra el elemento

      
      if ranking_crypto:
        rankings.append(ranking_crypto)
      else:
        print("No se encontró el ranking de la criptomoneda.")



      for xpath in xpaths_precios:
        try:
            precio_element = driver.find_element(By.XPATH, xpath)
            precio_crypto = precio_element.text
            break  # Detener el bucle si se encuentra el nombre de la criptomoneda
        except NoSuchElementException:
            continue  # Pasar al siguiente XPath si no se encuentra el elemento

      
      if precio_crypto:
        precios.append(precio_crypto)
      else:
        print("No se encontró el precio de la criptomoneda.")


      for xpath in xpaths_volumenes:
        try:
            volumen_element = driver.find_element(By.XPATH, xpath)
            volumen_crypto = volumen_element.text
            break  # Detener el bucle si se encuentra el nombre de la criptomoneda
        except NoSuchElementException:
            continue  # Pasar al siguiente XPath si no se encuentra el elemento

      
      if volumen_crypto:
        volumenes.append(volumen_crypto)
      else:
        print("No se encontró el volumen de la criptomoneda.")

      if nombre_crypto and capitalizacion_de_mercado and cantidad_maxima_tokens:
      # print(cantidad_maxima_tokens)
        metrica = {'ranking': ranking_crypto, 'nombre': nombre_crypto, 'cantidadMaxima': cantidad_maxima_tokens, 'capitalizacionMercado': capitalizacion_de_mercado, 'precio': precio_crypto, 'volumen': volumen_crypto }
        print(metrica)
        lista_metricas.append(metrica)
      else:
         print('La criptomoneda no fué añadida al listado')
    except:
      print('Algo ha ocurrido accediendo al elemento')

   
    driver.get('https://coingecko.com')
  # print(lista_links)
  # print(lista_metricas)
  df = pd.DataFrame({'Ranking': rankings, 'Nombre': nombres_crypto, 'Cantidad Máxima de tokens': cantidades_maxima_tokens, 'Capitalización Total de Mercado': capitalizaciones_de_mercado, 'Precio': precios, 'Volumen 24h': volumenes})
  print(df)
  df.to_csv('NTokens_Crypto_Coingecko.csv', index=False)
