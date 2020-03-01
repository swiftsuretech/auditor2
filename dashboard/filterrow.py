import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def Filterrow(users, platforms, ip):
    filterrow = dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-filter fa-lg text-black"),
                                html.I("  Filter by Operator"),
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Dropdown(
                                id="user-filter",
                                options=[{"label": i, "value": i} for i in users],
                                multi=False,
                                placeholder="Select Operator to Filter by"
                            )
                        )
                    ]
                ),
                width={'size': 4}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-filter fa-lg text-black"),
                                html.I("  Filter by Platform"),
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Dropdown(
                                options=[{"label": i, "value": i} for i in platforms],
                                multi=False,
                                placeholder="Select Platform to Filter by"
                            )
                        )
                    ]
                ),
                width={'size': 4}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className="fal fa-filter fa-lg text-black"),
                                html.I("  Filter by IP Address"),
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Dropdown(
                                options=[{"label": i, "value": i} for i in ip],
                                multi=False,
                                placeholder="Select IP Address to Filter by"
                            )
                        )
                    ]
                ),
                width={'size': 4}
            ),
        ]
    )
    return filterrow