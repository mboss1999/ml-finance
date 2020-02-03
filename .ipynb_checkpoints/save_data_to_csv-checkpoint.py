from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import json

api_key = 'WS8K5VM8FZL52BTH'


def save_dataset(symbol, timeframe='daily'):      
    
    ts = TimeSeries(key=api_key, output_format='pandas')
    
    if timeframe == 'daily':        
        data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')
        data.to_csv(f'./Stock Data/{symbol}_daily_adjusted.csv')
    elif timeframe == 'intraday':
        data, meta_data = ts.get_intraday(symbol, '1min', 'full')
        data.to_csv(f'./Stock Data/{symbol}_intraday_adjusted.csv')
    else:
        raise Exception('Unacceptable timeframe. Only daily and intraday are acceptable.')

def save_digital_dataset(symbol, market):
    
    cc = CryptoCurrencies(key=api_key, output_format='pandas')
    
    data, meta_data = cc.get_digital_currency_daily(symbol, market)
    
    data.to_csv(f'./Crypto Data/{symbol}_daily')