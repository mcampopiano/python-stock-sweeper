from keys import ameritrade
import requests, time, re
import pandas as pd
import pickle as pkl
from pprint import pprint

url = 'https://api.tdameritrade.com/v1/instruments'

df = pd.read_excel('Complete_List.xlsx')
symbols = list(df['Symbol'].values)

start = 0
end = 500

while start < len(symbols):
    tickers = symbols[start:end]

    payload = {'apikey': ameritrade,
            'symbol': tickers,
            'projection': 'fundamental'}

    results = requests.get(url,params=payload)
    data = results.json()
    f_name = time.asctime() + '.pkl'
    f_name = re.sub('[ :]','_',f_name)
    with open(f_name, 'wb') as file:
        pkl.dump(data,file)
    start = end
    end += 500
    time.sleep(1)

    
