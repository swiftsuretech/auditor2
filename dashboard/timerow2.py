import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc


day_hist_settings = [350, 'Number of Queries', 'Day of Week', 0.3, 'stack', dict(t=10, b=10, l=10, r=10),
                   dict(categoryorder='array',
                        categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday',
                                       'Tuesday', 'Monday'])
                   ]
day_hist_params = ['height', 'xaxis_title_text', 'yaxis_title_text', 'bargap', 'barmode', 'margin',
                   'yaxis']

class Timerow:
    def __init__(self, df, start_date, end_date, count):
        '''Instantiate a Timerow class. This is a formatted row containing 4 cards:
        A day histogram - Showing which days searches took place
        An hour histogram - Showing the hours the searches took place
        Additionally, there is a column of 2 rows; the first being a data selector
        and the second, an info card showing the number of records returned.
        '''
        # Instantiate day histogram
        self.hist_day = px.histogram(df, y=df["dayOfWeek"], orientation='h', x=df['hour'],
                                     labels={'Monday': 'Mon', 'Tuesday': 'Tue',
                                             'Wednesday': 'Wed', 'Thursday': 'Thu',
                                             'Friday': 'Fri', 'Saturday': 'Sat',
                                             'Sunday': 'Sun'})
        # Style the day histogram
        self.hist_day.update_layout(
            height=350,
            xaxis_title_text='Number of Queries',
            yaxis_title_text='Day of Week',
            bargap=0.3,
            barmode='stack',
            margin=diagMargins,
            yaxis=dict(categoryorder='array',
                       categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday',
                                      'Tuesday', 'Monday'])
        )

        # Instantiate the hour histogram
        self.hist_hour = px.histogram(df, y=df["hour"], orientation='h', x=df['hour'])
        # Style the hour histogram
        self.hist_hour.update_layout(
            height=350,
            xaxis_title_text='Number of Queries',
            yaxis_title_text='Hour of Day',
            bargap=0.3,
            barmode='stack',
            margin=diagMargins,
            yaxis_type='category',
            yaxis=dict(categoryorder='array',
                       categoryarray=[i for i in range(24, -1, -1)])
        )

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