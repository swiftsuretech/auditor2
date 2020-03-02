import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
from settings.settings import *


def Mainhist(df, spread):
    mainhist = px.histogram(df, x="transactionTime", color="username", nbins=spread)
    mainhist.update_layout(
        height=250,
        xaxis_title_text='Query Date',
        yaxis_title_text='Number of Queries',
        bargap=0.1,
        barmode='stack',
        margin=diagMargins,
        legend_title="Operator"
    )
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
                                        id="bighist",
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
