import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

##########

d = {}
period1 = int(time.mktime(datetime.datetime(2022, 1, 1, 00, 00).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 1, 10, 23, 59).timetuple()))
interval = '1d' #1d, 1m, 1wk
#####

def getData(coin):

    stock= f'https://query1.finance.yahoo.com/v7/finance/download/{coin}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    
    print(' ' * 5)
    print('---This is Data for: '+ coin + '---')

    #Conditioning Data    
    df = pd.read_csv(stock, index_col=0, parse_dates=True)
    del df['Adj Close']
    
    #Creating external Dictionary for external reference
    d[coin] = df
    
    df.index.name = 'Date'
    df.shape
    
    # Extracting Data for plotting
    #df.to_csv()
    #df.to_excel()

