
import yfinance as yf

import plotly.express as px

def plot(ticker: str):
    '''
    Plot a time series

    args: 
        ticker(str): the company ticker

    return:
        a plotly time series

    '''
    data = yf.download(ticker, period='max', multi_level_index = False)
    df = data.reset_index()[['Date','Close']]

    fig = px.line(df,x='Date',y='Close', title= f'Historico de {ticker}')

    return fig