"""
*** Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team ***
Build out the 'ring' row of our dashboard. This consists of 3 rows, all of which are simple pie charts to
show the breakdown of operators, platforms and IP addresses for the current dataset. This  module is
mainly an exercise in layout.
"""

# Import our dash libraries and a locally defined setting
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
from settings.settings import diagMargins, pie_style, pie_config


def build_ring_row(df):
    """Build out a container consisting of 3 pie charts, IP addresses, Operators and Platforms"""

    # Instantiate a platform pie chart object. I like my donuts with holes in them.
    pie_platform = px.pie(df, names='platform', hole=0.6)
    # Add some styling
    pie_platform.update_layout(
        margin=diagMargins,
    )

    # As above but for the operators.
    pie_user = px.pie(df, names='username', hole=0.6)
    pie_user.update_layout(
        margin=diagMargins,
    )

    # As above but the IP addresses.
    pie_ip = px.pie(df, names='ip', hole=0.6)
    pie_ip.update_layout(
        margin=diagMargins,
    ),

    # Build the layout container and return it to the calling function.
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
                                    style=pie_style,
                                    config=pie_config
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
                                    style=pie_style,
                                    config=pie_config,
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
                                        style=pie_style,
                                        config=pie_config,
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
