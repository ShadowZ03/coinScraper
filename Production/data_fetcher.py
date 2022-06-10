import matplotlib.pyplot as plt
import seaborn as sns
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

class data_fetcher:
    d = {}        
    def __init__(self, stock) -> None:
        self.ticker = stock
        self.data = None
        
    def getData(self, ticker, year, year2, month, month2, day, day2, interval):

        print(" ")
        print("---------- Pulling data for: ", self.ticker, "----------")
        print(" ")

        #print('---This is Data for: '+ ticker + '---')
        period1 = int(time.mktime(datetime.datetime(year, month, day, 00, 00).timetuple()))
        period2 = int(time.mktime(datetime.datetime(year2, month2, day2, 23, 59).timetuple()))
        interval = interval #1d, 1m, 1wk
         
        
        stock = f'https://query1.finance.yahoo.com/v7/finance/download/{self.ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

        #Conditioning Data    
        df = pd.read_csv(stock, index_col=0, parse_dates=True)
       
        del df['Adj Close']
        
        #Creating external Dictionary for external reference
        self.data = df
        df.index.name = 'Date'
        df.shape
             
    # TODO: Export for data
    # def exporter(self, type):
    #     if "csv" in type:
    #         self.df.to_csv()
    #     elif "excel" in type:
    #         self.df.to_excel()
    #     else:
    #         print("I'm not sure how to handle: " f{type})

    # TODOL TAIL Function 
    def data_tail(self):
        print("This is the tail of data for: ", self.ticker)
        self.last_ten = self.data[["Close", "Volume"]].tail(10)
        print(self.data[["Close", "Volume"]].tail(10))
    

    def get_data(self):
        print("this is data for: ", self.ticker)
        print(self.data)
        return self.data