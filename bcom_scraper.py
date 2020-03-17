
# This is a Py Scraper to obtain the values of BCOM:IND for the last five years, extracting the data from https://www.bloomberg.com/quote/BCOM:IND
# Manuel Quintana 3/3/20

import json
import requests
#import plotly.express as px
import sqlalchemy
import pandas as pd


# Local DB
DB_USER = 'manuel'
DB_PASS = 'jevi1717'
DB_ADDR = 'localhost'
DB_NAME = 'bloomberg'
DB_CONN = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(DB_USER, DB_PASS, DB_ADDR, DB_NAME))

#url = 'https://www.bloomberg.com/markets2/api/history/BCOM:IND/PX_LAST?timeframe=5_YEAR&period=weekly&volumePeriod=weekly'
ticker = 'BCOM:IND'
timeframe = '5_YEAR'
period = 'weekly' # acepta daily!
volume_period = 'weekly'
url = f'https://www.bloomberg.com/markets2/api/history/{ticker}/PX_LAST?timeframe={timeframe}'\
      f'&period={period}&volumePeriod={volume_period}'

#page = urlopen(url)
#html = page.read()
#soup = BeautifulSoup(html)
#print(soup.prettify('latin-1'))
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
data = requests.get(url, headers=headers).content
data_json = json.loads(data)

#print(data_json)
values = [x['value'] for x in data_json[0]['price']]
datetime = [x['dateTime'] for x in data_json[0]['price']]

data = pd.DataFrame(columns = ['ticker', 'date','value'])
for i in range (0, len(values)):
    currentval = values[i]
    currentdate = datetime[i]
    data = data.append({'ticker': ticker, 'date': currentdate, 'value': currentval}, ignore_index=True)

print (data)

data.to_sql(con=DB_CONN, name='bloomberg_values', if_exists='append', index = False)



#fig = px.line(x=datetime, y=values, labels={'x':'x', 'y':ticker})
#fig.show()
