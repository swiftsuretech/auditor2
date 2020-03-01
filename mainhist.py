import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
from settings import *


def Mainhist(df, spread):
    mainhist = px.histogram(df, x="transactionTime", color="username", nbins=spread)
    mainhist.update_layout(
        height=350,
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
                            html.I(" Queries by Week")
                        ]
                    ),
                    dbc.CardBody(
                        [
                            dcc.Graph(
                                figure=mainhist,
                                id="bighist",
                                config={'displayModeBar': False}
                            )
                        ]
                    )
                ]
            ),
            width={"size": 12}
        )
    )
    return bighist
