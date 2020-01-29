from alpha_vantage.timeseries import TimeSeries
import json


def save_dataset(symbol):
    api_key = 'WS8K5VM8FZL52BTH'

    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol, outputsize='full')

    data.to_csv(f'./Stock Data/{symbol}_daily.csv')