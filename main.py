import scrapping_crypto
import scrapping_crypto_coinmarketcap

def run():
  options = ('coingecko', 'coinmarketcap')
  user_option = input('coingecko o coinmarketcap => ')
  user_option = user_option.lower()

  if user_option == 'coingecko':
    scrapping_crypto.initCrypto()
  if user_option == 'coinmarketcap':
    scrapping_crypto_coinmarketcap.initCrypto()
  if user_option != 'coingecko' and user_option != 'coinmarketcap':
    print('la opción seleccionada no está soportada')

if __name__ == '__main__':
  run()