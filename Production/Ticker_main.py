# import investpy
# import trendet
from data_fetcher import data_fetcher
from graphit import graphit
from checker import checker

class TrendAnalysis:

    def __init__(self, ticker):
        self.ticker = ticker


#TODO: Add momentum Calc; where 3+ days of increase for population and price = +1
    #Starter for program
def run():
    mystocks = ["PSEC", "AAPL", "VGX-USD", "BTC-USD"]
    for stock in mystocks:
        ta = TrendAnalysis(stock)
        df = data_fetcher(stock)
        #graph = graphit()
       
        x = df.getData(stock, 2022, 2022, 1, 6, 1, 8, "1d")
        # df.data_tail()
        # df.data_tail()
        A = df.get_data()
        #graph.candleGraph(stock, df.get_data())
        k = checker(stock, A)
        k.volChecker()
        k.priceChecker()
        k.momentum()
        k.over_stats()
        # print(df)



if __name__ == "__main__":
    run()