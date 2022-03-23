import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

##########

mystocks = ['AAVE-USD', 'BTC-USD', 'MATIC-USD', 'DOT-USD', 'VGX-USD', 'ADA-USD', 'XLM-USD']
d = {}

#####
def getData(coin):
    period1 = int(time.mktime(datetime.datetime(2021, 1, 1, 00, 00).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2022, 3, 17, 23, 59).timetuple()))
    interval = '1d' #1d, 1m, 1wk

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
    print(df.head())
    print('Printing Graph')
    mpf.plot(df, type='candle', show_nontrading=True, title = coin)

#Kicker for program
for item in mystocks:
    print(' ' * 5)
    print('---Getting data for: ' + item + '---')
    print(' ' * 5)

    getData(item)

    print('---Completed data for: ' + item + '---')

print('***Run Complete***')

#How to access each coin DF outside of getData() function
##print(d['XLM-USD'])

x=[]
for i in df:
    y = [df.index(i), df['Close']]
    x.append(y)

print(x)
print('--------------------')

L = []
for time in pd.date_range(begin1, stop1):    
    print (pd.date_range(time, freq='D', periods=30).strftime("%Y-%m-%d %H:%M:%S").tolist())
    if time in L:
        print('already have it')
    else:
        L.append(pd.date_range(time, freq='D', periods=31).strftime("%Y-%m-%d").tolist())


print('--------------------')

print(L)

print('--------------------')
groups = []
datepair = [(d1,d2) for d1, d2, in zip(L[0],L[1:])]
print(datepair)
print('--------------------')
print('--------------------')
print(L[0])
print('--------------------')
print('--------------------')
groups = []
uniquekeys = []
data = L[0]
for k, g in groupby(data, key=lambda x: x[5]):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

print(groups)

print(uniquekeys)