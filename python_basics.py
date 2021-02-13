from keys import ameritrade
import requests

url = 'https://api.tdameritrade.com/v1/instruments'

payload = {'apikey': ameritrade,
           'symbol': 'GOOG',
           'projection': 'fundamental'}

results = requests.get(url,params=payload)

print(results)
