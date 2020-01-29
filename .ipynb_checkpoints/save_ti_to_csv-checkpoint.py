from alpha_vantage.techindicators import TechIndicators

def save_ti(ticker, interval='daily'):
    ti = TechIndicators(key='WS8K5VM8FZL52BTH', output_format='pandas')
    data, meta_data = ti.get_bbands(symbol=ticker, interval=interval, time_period=60)
    data.to_csv(f'./Stock Data/{ticker}_{interval}_ti.csv')