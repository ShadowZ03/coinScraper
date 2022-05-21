# import investpy
# import trendet
import matplotlib.pyplot as plt
import seaborn as sns
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

class TrendAnalysis:
    
    ##########
    #Change Variables below
   

    #End of Change Variables
    #Variables needed within the functions
   
    def __init__(self, ticker):
        self.ticker = ticker
    
    def getData(self):
        graph = False
        period1 = int(time.mktime(datetime.datetime(2022, 1, 1, 00, 00).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2022, 5, 20, 23, 59).timetuple()))
        interval = '1d' #1d, 1m, 1wk

        
        
        d = {}

        stock = f'https://query1.finance.yahoo.com/v7/finance/download/{self.ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    
        print(' ' * 5)
        print('---This is Data for: '+ self.ticker + '---')

        #Conditioning Data    
        df = pd.read_csv(stock, index_col=0, parse_dates=True)
        del df['Adj Close']
        
        #Creating external Dictionary for external reference
        d[self.ticker] = df
        self.data = d[self.ticker]
        df.index.name = 'Date'
        df.shape
        
        # Extracting Data for plotting
        #df.to_csv()
        #df.to_excel()

        self.last_ten = self.data[["Close", "Volume"]].tail(10)
        print(self.data[["Close", "Volume"]].tail(10))

    def getGraph(self):

        mpf.plot(self.data, type='candle', show_nontrading=True, title = self.ticker)
        print(' ' * 5)
        print('--- Printed Graph ---')
        print(' ' * 5)


    def volChecker(self):
        a = 0 
        b = 1
        pos = 0
        neg = 0

        length = len(self.data.index)
        counter = length - 1

        while counter > 0 & b < length:
            counter -= 1
            if self.data["Volume"].loc[self.data.index[a]] < self.data["Volume"].loc[self.data.index[b]]:
                pos += 1
                a += 1
                b += 1
            else:
                neg += 1
                a += 1
                b += 1

        print(f'For Volume of {self.ticker}: {pos} positives , {neg} negatives')
        print(f'***VolChecker Complete for {self.ticker}***')                 

    def priceChecker(self):
        a = 0 
        b = 1
        pos = 0
        neg = 0

        length = len(self.data.index)
        counter = length - 1

        while counter > 0 & b < length:
            counter -= 1
            if self.data["Close"].loc[self.data.index[a]] < self.data["Close"].loc[self.data.index[b]]:
                pos += 1
                a += 1
                b += 1
            else:
                neg += 1
                a += 1
                b += 1

        print(f'For Close of {self.ticker}: {pos} positives , {neg} negatives')
        print(f'***PriceChecker Complete for {self.ticker}***')          

    #Starter for program
def run():
    mystocks = ["PSEC", "AAPL", "VGX-USD", "APE-USD", "BTC-USD"]
    for stock in mystocks:
        t = TrendAnalysis(stock)
        t.getData()  
        t.volChecker()
        t.priceChecker()
        t.getGraph()
        print('***Run Complete***')

if __name__ == "__main__":
    run()