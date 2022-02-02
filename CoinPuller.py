import time
import datetime
import pandas as pd
coin = 'MATIC-USD'
period1 = int(time.mktime(datetime.datetime(2022, 1, 1, 00, 00).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 1, 31, 23, 59).timetuple()))
interval = '1wk' #1d, 1m, 1wk

stock= f'https://query1.finance.yahoo.com/v7/finance/download/{coin}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(stock, index_col=0, parse_dates=True)
#df.to_csv()
#df.to_excel()
print(df)