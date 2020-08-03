import pandas as pd

def callthisfunc(x):

    df = pd.read_csv('callfile/itc.csv')
    cdate = df['Date']
    close = df['Close']
    sma = df['Close'].rolling(window = x).mean()
    context = {
        'cdate': cdate,
        'close': close,
        'sma': sma
    }
    return context
