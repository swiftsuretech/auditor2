import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from settings.settings import *


def build_main_histogram(df, spread):
    mainhist = px.histogram(df, x="transactionTime", color="username", nbins=spread)
    mainhist.update_layout(**main_hist_settings)
    bighist = dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-lg fa-chart-bar"),
                            html.I(" Queries by Week"),
                            # html.I(
                            #     dbc.Button(
                            #         html.I(className="fas fa-chevron-double-up color-black"),
                            #         id="hist_collapse-button",
                            #         color="secondary",
                            #         style={'height': '25px', 'width': '25px', 'padding': '0px', 'margin': '0px'},
                            #         outline=True
                            #     ),
                            #     style={'float': 'right'},
                            # ),
                        ],
                        style={'height': '50px'},
                    ),
                    dbc.CardBody(
                        # dbc.Collapse(
                            dcc.Loading(
                                [
                                    dcc.Graph(
                                        figure=mainhist,
                                        id="big_histogram",
                                        config={'displayModeBar': False}
                                    )
                                ]
                            ),
                        #     id='hist_collapse'
                        # )
                    )
                ]
            ),
            width={"size": 12},
        ),
    )
    return bighist
