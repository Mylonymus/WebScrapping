#Librerías
from selenium.webdriver.common.by import By
import utils_coinmarketcap

def initCrypto():
  

  # Inicializamos el navegador
  browser = utils_coinmarketcap.create_browser()
  
  utils_coinmarketcap.prepare_table_results(browser)
  table = browser.find_elements(By.CSS_SELECTOR, '.cmc-table tbody tr')
  
  table = utils_coinmarketcap.each_rows(len(table), browser)

  for rowLoaded in table:
   utils_coinmarketcap.build_object(rowLoaded)

  utils_coinmarketcap.build_export_to_csv()
    
  

