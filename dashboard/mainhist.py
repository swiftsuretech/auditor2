"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Builds the main histogram that spans the dashboard showing activity by date
"""

#  Import some Dash libraries and settings.
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from settings.settings import *


def build_main_histogram(df, spread):
    """Builds a Boostrap container with a page spanning histogram showing activity against date. Takes
    2 arguments; a dataframe and 'spread' variable - the number of days to plot. This allows the number
    of bins to be calculated accurately."""
    #  Instantiate the histogram, define the axis and spread and show a stacked layout, colour coding by operator name.
    main_histogram = px.histogram(df, x="transactionTime", color="username", nbins=spread)
    # Pull a library of styling variables from settings and apply.
    main_histogram.update_layout(**main_hist_settings)
    # Define the layout and return as an object.
    main_histogram_layout = dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal mr-2 fa-lg fa-chart-bar"),
                            html.I(" Queries by Week"),
                        ],
                        style={'height': '50px'},
                    ),
                    dbc.CardBody(
                        # dbc.Collapse(
                        dcc.Loading(
                            [
                                dcc.Graph(
                                    figure=main_histogram,
                                    id="big_histogram",
                                    config={'displayModeBar': False}
                                )
                            ],
                        ),
                    )
                ],
                className='shadow',
            ),
            width={"size": 12},
        ),
    )
    return main_histogram_layout
