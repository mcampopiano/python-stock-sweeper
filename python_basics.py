from keys import ameritrade
import requests
import pandas as pd

url = 'https://api.tdameritrade.com/v1/instruments'

df = pd.read_excel('Complete_List.xlsx')

payload = {'apikey': ameritrade,
           'symbol': 'GOOG',
           'projection': 'fundamental'}

results = requests.get(url,params=payload)

print(results.json())
