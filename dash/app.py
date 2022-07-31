import logging
import os

from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

from layout import app_layout
from redis_helpers import init_redis_conn, load_values
from utils import get_ticker_names


LOG_LEVEL_ENV = os.getenv("LOG_LEVEL", "debug")
LOG_LEVEL_MAP = {"debug": logging.DEBUG, "info": logging.INFO}

logging.basicConfig(encoding="utf-8", level=LOG_LEVEL_MAP[LOG_LEVEL_ENV])


app = Dash(external_stylesheets=[dbc.themes.CYBORG])
server = app.server

tickers_names = get_ticker_names()
redis = init_redis_conn()


app.layout = app_layout()


@app.callback(Output("caption", "children"), Input("ticker-dropdown", "value"))
def set_caption(value, redis_conn=redis):
    redis_conn.set("current_ticker", value)

    return f"{value}"


@app.callback(
    Output("live-update-graph", "figure"), Input("interval-component", "n_intervals")
)
def update_graph_live(n, redis_conn=redis):
    ticker_name = redis_conn.get("current_ticker")
    ticker_prices = load_values(redis_conn, ticker_name)
    if not ticker_prices:
        fig = go.Figure(go.Scatter())
    else:
        df = pd.DataFrame(ticker_prices, columns=["Timestamp", "Value"])
        df["Value"] = pd.to_numeric(df["Value"]).astype(int)
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='s')
        df = df.sort_values(by="Timestamp")
        logging.info(df)

        fig = go.Figure(data=go.Scatter(x=df["Timestamp"], y=df["Value"],
                                        hovertemplate='Value: %{y}'+'<br>Timestamp: %{x}'))

    logging.info(ticker_prices)

    return fig
