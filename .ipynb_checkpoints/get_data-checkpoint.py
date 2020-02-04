from os import listdir
from os.path import isfile, join
import pandas as pd

def get_data(symbol, interval='daily'):
    
    # Get data and make a datetime index
    data = pd.read_csv(f'./Stock Data/{symbol}_{interval}_adjusted.csv')
    data.set_index(pd.to_datetime(data['date']), inplace=True)
    data.drop(columns='date', inplace=True)
    
    mypath = './Stock Data/TI'
    onlyfiles = [f for f in listdir('./Stock Data/TI') if isfile(join(mypath, f))]

    ti_fn = []
    for f in onlyfiles:
        prefix = symbol + f'_{interval}'
        if prefix == f[:len(prefix)]:
            ti_fn.append(f)

    for f in ti_fn:
        d = pd.read_csv(f'./Stock Data/TI/{f}')
        d.set_index(pd.to_datetime(d['date']), inplace=True)
        d.drop(columns='date', inplace=True)
        if f[len(prefix) + 1:] == 'macdext.csv':
            data.join(d, rsuffix='ext')
        elif f[len(prefix) + 1:] == 'stochris.csv':
            data.join(d, rsuffix='ris')
        else:
            data = data.join(d)

    data.dropna(inplace=True)
    
    return data
    
    