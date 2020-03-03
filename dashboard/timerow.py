"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Build out the 'time' row of our dashboard. This consists of 4 cards. 2 are histograms showing the number
of queries by hour of day and the other by day of week. This is a safeguard to ensure that there is no
out of hours funny business. The middle column has 2 x columns. The top one is a date picker and the lower
one is card to show the number of records in the current set. This is mainly an exercise in layout.
"""

# Import our Dash libraries
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc

# Pull in some externalised settings for re-usable layout.
from settings.settings import hist_day_settings, hist_hour_settings


def build_time_row(df, start_date, end_date, count):
    """Build a row of widgets. Takes dataframe, start date, end date and record count as arguments"""

    # Instantiate our day histogram in vertical format.
    hist_day = px.histogram(df, y=df["dayOfWeek"], orientation='h', x=df['hour'], )
    # Pull the layout dictionary from settings and apply.
    hist_day.update_layout(**hist_day_settings),

    # Same as above but for the hour histogram.
    hist_hour = px.histogram(df, y=df["hour"], orientation='h', x=df['hour'], )
    hist_hour.update_layout(**hist_hour_settings),

    # Define the Bootstrap container that represents the entire row.
    time_row = dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-lg fa-calendar-alt"),
                                html.I(" Activity Days")
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Loading(
                                dcc.Graph(
                                    figure=hist_day,
                                    id='day_hist',
                                    style={'height': 250, 'padding': 0},
                                    config={
                                        'displayModeBar': False}
                                ),
                                style={'margin-top': '0rem'},
                            )
                        )
                    ]
                ),
                width={"size": 4, 'order': 1}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-lg fa-user-clock"),
                                html.I(" Activity Hours")
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Loading(
                                dcc.Graph(
                                    figure=hist_hour,
                                    id="hour_hist",
                                    style={'height': 250, 'padding': 0},
                                    config={
                                        'displayModeBar': False}
                                ),
                                style={'margin-top': '0rem'},
                            )
                        )
                    ]
                ),
                width={"size": 4, 'order': 3}
            ),
            dbc.Col(
                children=[
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                [
                                    html.I(className="fal fa-alarm-clock"),
                                    html.I(" Time Select")
                                ]
                            ),
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.P('Choose a start and end date to filter the data'),
                                        dcc.DatePickerRange(
                                            id='date-picker-range',
                                            display_format='DD/MM/YY',
                                            start_date=start_date,
                                            end_date=end_date,
                                            end_date_placeholder_text='Select a date!',
                                        ),
                                    ],
                                    style={'text-align': 'center'},
                                ),
                            )
                        ]
                    ),
                    html.Br(),
                    dbc.Card(
                        [
                            dcc.Loading(
                                dbc.CardBody(
                                    html.Div(
                                        children=[
                                            html.P(
                                                html.H2(
                                                    children=[
                                                        html.I(className="fal fa-lg fa-cabinet-filing"),
                                                        html.I(' '),
                                                        html.I(count,
                                                               id='counter'),
                                                        html.I(" Records")
                                                    ]
                                                )
                                            ),
                                        ],
                                        style={'text-align': 'center', 'height': '99px', 'padding': '20px'},
                                    ),
                                ),
                            ),
                        ]
                    ),
                ],
                width={"size": 4, 'order': 2}
            ),
        ]
    )
    return time_row
