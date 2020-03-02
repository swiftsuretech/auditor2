import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
from datetime import datetime as dt

diagMargins = dict(t=10, b=10, l=10, r=10)


def Timerow(df, start_date, end_date):
    hist_day = px.histogram(df, y=df["dayOfWeek"], orientation='h', x=df['hour'],
                            labels={'Monday': 'Mon', 'Tuesday': 'Tue',
                                    'Wednesday': 'Wed', 'Thursday': 'Thu',
                                    'Friday': 'Fri', 'Saturday': 'Sat',
                                    'Sunday': 'Sun'})

    hist_day.update_layout(
        height=350,
        xaxis_title_text='Number of Queries',
        yaxis_title_text='Day of Week',
        bargap=0.3,
        barmode='stack',
        margin=diagMargins,
        yaxis=dict(categoryorder='array',
                   categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday',
                                  'Tuesday', 'Monday'])
    ),

    hist_hour = px.histogram(df, y=df["hour"], orientation='h', x=df['hour'],
                             )

    hist_hour.update_layout(
        height=350,
        xaxis_title_text='Number of Queries',
        yaxis_title_text='Hour of Day',
        bargap=0.3,
        barmode='stack',
        margin=diagMargins,
        yaxis_type='category',
        yaxis=dict(categoryorder='array',
                   categoryarray=[24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,
                                  12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    ),

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
                width={"size": 4, 'order': 2}
            ),
        ]
    )
    return timerow
