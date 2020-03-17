# This is a Py Scraper to obtain the values of BCOM:IND for the last five years, extracting the data from https://www.bloomberg.com/quote/BCOM:IND

import json
import requests
import plotly.express as px
import pandas as pd

ticker = 'BCOM:IND'
timeframe = '5_YEAR'
period = 'weekly' # acepta daily!
volume_period = 'weekly'
url = f'https://www.bloomberg.com/markets2/api/history/{ticker}/PX_LAST?timeframe={timeframe}'\
      f'&period={period}&volumePeriod={volume_period}'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
data = requests.get(url, headers=headers).content
data_json = json.loads(data)

values = [x['value'] for x in data_json[0]['price']]
datetime = [x['dateTime'] for x in data_json[0]['price']]

data = pd.DataFrame(columns = ['ticker', 'date','value'])
for i in range (0, len(values)):
    currentval = values[i]
    currentdate = datetime[i]
    data = data.append({'ticker': ticker, 'date': currentdate, 'value': currentval}, ignore_index=True)

print ('Recovered data:')
print (data)

respuesta = input("\nIngrese 1 para exportar como CSV, 2 para graficar: ")
if int(respuesta) == 1:
    data.to_csv(ticker+'.csv', sep=',', encoding='utf-8')
    print("Se generó el archivo ", ticker, '.csv')
else:
    fig = px.line(x=datetime, y=values, labels={'x':'x', 'y':ticker})
    fig.show()