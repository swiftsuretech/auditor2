import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc

diagMargins = dict(t=10, b=10, l=10, r=10)


def Ringrow(df):
    pieplat = px.pie(df, names='platform', hole=0.6)
    pieplat.update_layout(
        margin=diagMargins,
    )

    pieuser = px.pie(df, names='username', hole=0.6)
    pieuser.update_layout(
        margin=diagMargins,
    )

    histDay = px.histogram(df, y=df["dayOfWeek"], orientation='h', x=df['hour'],
                           labels={'Monday': 'Mon', 'Tuesday': 'Tue',
                                   'Wednesday': 'Wed', 'Thursday': 'Thu',
                                   'Friday': 'Fri', 'Saturday': 'Sat',
                                   'Sunday': 'Sun'})

    histDay.update_layout(
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
    ringrow = dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-lg fa-photo-video"),
                                html.I(" Platform")
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Loading(
                                dcc.Graph(
                                    figure=pieplat,
                                    id='ring_plat',
                                    style={'height': 250, 'padding': 0},
                                    config={
                                        'displayModeBar': False}
                                ),
                                style={'margin-top': '0rem'},
                            )
                        )
                    ]
                ),
                width={"size": 4}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-lg fa-users"),
                                html.I(" Operators")
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Loading(
                                dcc.Graph(
                                    figure=pieuser,
                                    id="ring_user",
                                    style={'height': 250, 'padding': 0},
                                    config={
                                        'displayModeBar': False}
                                ),
                                style={'margin-top': '0rem'},
                            )
                        )
                    ]
                ),
                width={"size": 4}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-calendar-alt"),
                                html.I(" Queries by Week Day")
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Loading(
                                [
                                    dcc.Graph(
                                        figure=histDay,
                                        id="ring_day",
                                        style={'height': 250, 'padding': 0},
                                        config={
                                            'displayModeBar': False}
                                    )
                                ],
                                style={'margin-top': '0rem'},
                            )
                        )
                    ]
                ),
                width={"size": 4}
            ),
        ]
    )
    return ringrow
