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
    print('***VolChecker Complete for {coin}***')                 

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
    print('***PriceChecker Complete for {coin}***')          






