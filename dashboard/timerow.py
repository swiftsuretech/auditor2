import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
from settings.settings import hist_day_settings, hist_hour_settings


def build_time_row(df, start_date, end_date, count):
    hist_day = px.histogram(df, y=df["dayOfWeek"], orientation='h', x=df['hour'],)

    hist_day.update_layout(**hist_day_settings),

    hist_hour = px.histogram(df, y=df["hour"], orientation='h', x=df['hour'],)
    hist_hour.update_layout(**hist_hour_settings),

    timerow = dbc.Row(
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
    return timerow
