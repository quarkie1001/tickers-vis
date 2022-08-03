from dash import html, dcc

from utils import get_ticker_names

tickers_names = get_ticker_names()


def app_layout():
    layout = html.Div(
        children=[
            html.H1(children="Dummy tickers"),
            html.H3(children="Test assignment"),
            html.Div(id="hidden-div", style={"display": "none"}),
            dcc.Dropdown(
                tickers_names,
                tickers_names[0],
                id="ticker-dropdown",
                style={"margin-top": "40px"},
            ),
            dcc.Graph(id="live-update-graph"),
            dcc.Interval(
                id="interval-component",
                interval=1 * 1000,  # in milliseconds
                n_intervals=0,
            ),
            html.H2(id="caption", style={"text-align": "center"}),
        ]
    )

    return layout
