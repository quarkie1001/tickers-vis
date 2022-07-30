import logging
import os

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import redis

from dash import Dash, html, dcc, Input, Output


tickers_names = [1,2,34,5,6,7,8,9]


LOG_LEVEL_ENV = os.getenv("LOG_LEVEL", "debug")
LOG_LEVEL_MAP = {"debug": logging.DEBUG,
                 "info": logging.INFO}

logging.basicConfig(encoding='utf-8', level=LOG_LEVEL_MAP[LOG_LEVEL_ENV])


app = Dash(external_stylesheets=[dbc.themes.CYBORG])
server = app.server

r = redis.from_url('redis://redis', decode_responses=True)
# ticker_prices = r.hgetall("ticker_05")
# print(ticker_prices)
# prices = dict(sorted(ticker_prices.items()))
# logging.info(prices)
#
# ticker_data = list(zip(prices.values(), prices.keys()))
#
# df = pd.DataFrame(ticker_data, columns = ["Value", "Step"])

ticker_prices = r.lrange("ticker_05", 0, -1)
logging.info(ticker_prices)

fig = go.Figure(data=go.Scatter(x=df["Step"], y=df["Value"]))

app.layout = html.Div(children=[
    html.H1(children='Dummy tickers'),

    html.H3(children='''
        Test assignment for Skanestas Investments Ltd.
    '''),
  #  dcc.Dropdown(tickers_names, tickers_names[0], id='ticker-dropdown', style={"margin-top" : "40px"}),
    dcc.Graph(
        id='graph',
        figure=fig,
    ),
    html.H2(id="caption", style={"text-align": "center"}),
])

def update_output(value):
    return f'{value}'
