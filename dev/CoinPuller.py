import time
import datetime
from unittest import skip
import pandas as pd
from itertools import groupby

begin = [2022, 1, 1, 00, 00]
year = begin[0]
month = begin[1]
day = begin[2]
hour = begin[3]
min = begin[4]

begin1 = str(year)+'-'+str(month)+'-'+str(day)+' '+str(hour)+':'+str(min)+':'+'00'

stop = [2022, 1, 3, 23, 59]
year2 = stop[0]
month2 = stop[1]
day2 = stop[2]
hour2 = stop[3]
min2 = stop [4]

stop1 = str(year2)+'-'+str(month2)+'-'+str(day2)+' '+str(hour2)+':'+str(min2)+':'+'00'

print(begin1, stop1)

coin = 'MATIC-USD'
period1 = int(time.mktime(datetime.datetime(year, month, day, hour, min).timetuple()))
period2 = int(time.mktime(datetime.datetime(year2, month2, day2, hour2, min2).timetuple()))
interval = '1wk' #1d, 1m, 1wk

stock= f'https://query1.finance.yahoo.com/v7/finance/download/{coin}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(stock, index_col=0, parse_dates=True)
#df.to_csv()
#df.to_excel()
#print(df.index)
