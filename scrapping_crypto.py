#Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import pandas as pd

def initCrypto():
  #Opciones de navegacion
  options = webdriver.ChromeOptions()
  options.add_argument('--start-maximized')
  options.add_argument('--disable-extensions')
  print(options)

  driver_path = '/Users/mylo/Documents/Cursos/Python/Selenium/webdriver/chromedriver-mac-x64/chromedriver'
  options.path = driver_path

  driver = webdriver.Chrome(options)

    

  # Inicializamos el navegador

  driver.get('https://coingecko.com')