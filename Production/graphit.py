import mplfinance as mpf

class graphit:
        def candleGraph(self,ticker, data):
    
            mpf.plot(data, type='candle', show_nontrading=True, title = ticker)
            print(' ' * 5)
            print('--- Printed Graph ---')
            print(' ' * 5)

        # TODO: LINEPLOT

        # TODO:
        # TODO:
        # TODO:
        # TODO:
        # TODO: