import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

##########
#Change Variables below
mystocks = ['PSEC']
graph = False
period1 = int(time.mktime(datetime.datetime(2022, 1, 1, 00, 00).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 5, 20, 23, 59).timetuple()))
interval = '1d' #1d, 1m, 1wk
#End of Change Variables

#Variables needed within the functions
d = {}

#####

def getData(coin):
    stock = f'https://query1.finance.yahoo.com/v7/finance/download/{coin}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
   
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

    self.last_ten = d[coin][["Close", "Volume"]].tail(10)
    print(d[coin][["Close", "Volume"]].tail(10))

def getGraph(coin):
    if graph == True:
       
        mpf.plot(d[coin], type='candle', show_nontrading=True, title = coin)
        print(' ' * 5)
        print('--- Printed Graph ---')
        print(' ' * 5)
    else:
        print(' ' * 5)
        print('--- Skipped Graph ---')
        print(' ' * 5)

def volChecker(coin):
    a = 0 
    b = 1
    pos = 0
    neg = 0

    length = len(d[coin].index)
    counter = length - 1

    while counter > 0 & b < length:
        counter -= 1
        if d[coin]["Volume"].loc[d[coin].index[a]] < d[coin]["Volume"].loc[d[coin].index[b]]:
            pos += 1
            a += 1
            b += 1
        else:
            neg += 1
            a += 1
            b += 1

    print(f'For Volume of {coin}: {pos} positives , {neg} negatives')
    print(f'***VolChecker Complete for {coin}***')                 

def priceChecker(coin):
    a = 0 
    b = 1
    pos = 0
    neg = 0

    length = len(d[coin].index)
    counter = length - 1

    while counter > 0 & b < length:
        counter -= 1
        if d[coin]["Close"].loc[d[coin].index[a]] < d[coin]["Close"].loc[d[coin].index[b]]:
            pos += 1
            a += 1
            b += 1
        else:
            neg += 1
            a += 1
            b += 1

    print(f'For Close of {coin}: {pos} positives , {neg} negatives')
    print(f'***PriceChecker Complete for {coin}***')          

#Starter for program
def run():
    for item in mystocks:
        print(' ' * 5)
        print('---Getting data for: ' + item + '---')
        print(' ' * 5)

        getData(item)
        getGraph(item)
        volChecker(item)
        priceChecker(item)
        print('---Completed data for: ' + item + '---')

print('***Run Complete***')

if __name__ == "__main__":
    run()