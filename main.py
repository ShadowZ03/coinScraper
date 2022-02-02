import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

##########

mystocks = ['AAVE-USD', 'BTC-USD', 'MATIC-USD', 'DOT-USD', 'VGX-USD', 'ADA-USD', 'XLM-USD']

#####
def getData(coin):
    period1 = int(time.mktime(datetime.datetime(2021, 1, 1, 00, 00).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2022, 2, 2, 23, 59).timetuple()))
    interval = '1d' #1d, 1m, 1wk

    stock= f'https://query1.finance.yahoo.com/v7/finance/download/{coin}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    
    print(' ' * 5)
    print('---This is Data for: '+ coin + '---')
        
    df = pd.read_csv(stock, index_col=0, parse_dates=True)
    #df.to_csv()
    #df.to_excel()
    # Extracting Data for plotting
    del df['Adj Close']

    df.index.name = 'Date'
    df.shape
    print(df.head())
    mpf.plot(df, type='candle', show_nontrading=True, title = coin)


for item in mystocks:
    print(' ' * 5)
    print('---Getting data for: ' + item + '---')
    print(' ' * 5)

    getData(item)

    print('---Completed data for: ' + item + '---')

