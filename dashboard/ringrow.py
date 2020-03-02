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

    pieip = px.pie(df, names='ip', hole=0.6)
    pieip.update_layout(
        margin=diagMargins,
    ),

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
                width={"size": 4, 'order': 2}
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
                width={"size": 4, 'order': 1}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-lg fa-desktop-alt"),
                                html.I(" IP Addresses")
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Loading(
                                [
                                    dcc.Graph(
                                        figure=pieip,
                                        id="ring_ip",
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
                width={"size": 4, 'order': 3}
            ),
        ]
    )
    return ringrow
