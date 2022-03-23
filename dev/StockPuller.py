import time
import datetime
import pandas as pd
ticker = 'AAPL'
period1 = int(time.mktime(datetime.datetime(2021, 12, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 12, 31, 23, 59).timetuple()))
interval = '1d' #1d, 1m, 1wk

stock= f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(stock)
#df.to_csv()
#df.to_excel()
print(df)