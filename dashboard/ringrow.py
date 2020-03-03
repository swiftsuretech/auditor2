import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
from settings.settings import diagMargins


def build_ring_row(df):
    pie_platform = px.pie(df, names='platform', hole=0.6)
    pie_platform.update_layout(
        margin=diagMargins,
    )

    pie_user = px.pie(df, names='username', hole=0.6)
    pie_user.update_layout(
        margin=diagMargins,
    )

    pie_ip = px.pie(df, names='ip', hole=0.6)
    pie_ip.update_layout(
        margin=diagMargins,
    ),

    ring_row = dbc.Row(
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
                                    figure=pie_platform,
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
                                    figure=pie_user,
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
                                        figure=pie_ip,
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
    return ring_row
