import matplotlib.pyplot as plt
import seaborn as sns
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates

class checker:
    overall_pos = 0
    overall_neg = 0

    def __init__(self, stock, data):
        self.data = data
        self.ticker = stock
    def volChecker(self):
        a = 0 
        b = 1
        pos = 0
        neg = 0
    
        length = len(self.data.index)
        counter = length - 1
        # print(self.data)
        while counter > 0 & b < length:
            counter -= 1
            if self.data["Volume"].loc[self.data.index[a]] < self.data["Volume"].loc[self.data.index[b]]:
                pos += 1
                checker.overall_pos += 1
                a += 1
                b += 1
            else:
                neg += 1
                checker.overall_neg += 1
                a += 1
                b += 1
        total = pos + neg
        percent = float(pos/total)*100
        print("Percent of Support:", self.ticker, "%.0f%%" % percent)
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
                checker.overall_pos += 1
                a += 1
                b += 1
            else:
                neg += 1
                checker.overall_neg += 1
                a += 1
                b += 1
        
        total = pos + neg
        percent = float(pos/total)*100
        print("Percent of Support:", self.ticker, "%.0f%%" % percent)
        print(f'For Close of {self.ticker}: {pos} positives , {neg} negatives')
        print(f'***PriceChecker Complete for {self.ticker}***')          
        
    def momentum(self):
        a = 0 
        b = 1
        pos = 0
        neg = 0
        length = len(self.data.index)
        counter = length - 1

        while counter > 0 & b < length:
            counter -= 1
            if self.data["Volume"].loc[self.data.index[a]] < self.data["Volume"].loc[self.data.index[b]] and self.data["Close"].loc[self.data.index[a]] < self.data["Close"].loc[self.data.index[b]]:
                pos += 1
                checker.overall_pos += 1
                a += 1
                b += 1
            else:
                neg += 1
                checker.overall_neg += 1
                a += 1
                b += 1
        total = pos + neg
        percent = float(pos/total)*100
        print("Percent of Support:", self.ticker, "%.0f%%" % percent)
        print(f'For Momentum of {self.ticker}: {pos} positives , {neg} negatives')
        print(f'***momentum Complete for {self.ticker}***')           
    
    def over_stats(self):
        total = checker.overall_pos + checker.overall_neg
        percent = float(checker.overall_pos/total)*100
        print("Overall sentiment: ", percent)


    #TODO: P/E For stock analysis
    def PEAnalysis(self):
        if "-USD" in self.ticker:
            print("This is a  crypto")
        else:
            (print("This is a stock!"))
            