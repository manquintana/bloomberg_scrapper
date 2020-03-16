
# This is a Py Scraper to obtain the values of BCOM:IND for the last five years, extracting the data from https://www.bloomberg.com/quote/BCOM:IND
# Manuel Quintana 3/3/20

import json
import requests
import plotly.express as px
import sqlalchemy
import pandas as pd

# Local DB
DB_USER = 'manuel'
DB_PASS = 'jevi1717'
DB_ADDR = 'localhost'
DB_NAME = 'bloomberg'
DB_CONN = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(DB_USER, DB_PASS, DB_ADDR, DB_NAME))


ticker = 'BCOM:IND'
timeframe = '5_YEAR'
period = 'weekly' # acepta daily!
volume_period = 'weekly'

#https://www.bloomberg.com/markets2/api/history/BCOM:IND/PX_LAST?timeframe=5_YEAR&period=weekly&volumePeriod=weekly

url = f'https://www.bloomberg.com/markets2/api/history/{ticker}/PX_LAST?timeframe={timeframe}'\
      f'&period={period}&volumePeriod={volume_period}'

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#data = requests.get(url, headers=headers).content
r = requests.get(url, headers={'Accept': 'application/json'}).content
data = pd.DataFrame(r.json())


print(type(data))


#y = [x['value'] for x in data[0]['price']]
#x = [x['dateTime'] for x in data[0]['price']]

#fig = px.line(x=x, y=y, labels={'x':'x', 'y':ticker})
#fig.show()
