"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Builds our row of 3 x filters for the Dashboard to allow the user to navigate the data. This is a simple layout
that returns a Bootstrap container ready to drop into a row of the dashboard.
"""

# Import some Dash libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


class FilterRow:
    """Returns the filtering row as class object"""
    def __init__(self, user, platform, ip):
        self.row = build_filter_row(user, platform, ip)


def build_columns(topic):
    """Takes a list of unique entities and returns them as a KV pair with the same name"""
    return [{"label": i, "value": i} for i in topic]


def build_filter_row(users, platforms, ip):
    """Builds out a Bootstrap container containing 3 x dropdown filters. The filters are populated by providing
    a list of unique values for that particular filter. The function takes 3 x arguments; list of unique operator
    name, list of unique platform names and list of unique IP addresses."""
    filter_icon = "fal mr-2 fa-filter fa-lg text-black"
    filter_row = dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className=filter_icon),
                                html.I("  Filter by Operator"),
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Dropdown(
                                # These dropdown objects are the same throughout the module
                                # Comments for this one apply to all 3.
                                id="operator-filter",
                                # List comprehension to drop all values of users as options
                                # for the user to select.
                                options=build_columns(users),
                                # We only want our user to be able to select a single filter
                                # to keep things simple.
                                multi=False,
                                # Placeholder test when nothing selected yet.
                                placeholder="Select Operator to Filter by"
                            )
                        )
                    ],
                    className='shadow',
                ),
                width={'size': 4}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className=filter_icon),
                                html.I("  Filter by Platform"),
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Dropdown(
                                id='platform-filter',
                                options=build_columns(platforms),
                                multi=False,
                                placeholder="Select Platform to Filter by"
                            )
                        )
                    ],
                    className='shadow',
                ),
                width={'size': 4}
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            [
                                html.I(className=filter_icon),
                                html.I("  Filter by IP Address"),
                            ]
                        ),
                        dbc.CardBody(
                            dcc.Dropdown(
                                id='ip-filter',
                                options=build_columns(ip),
                                multi=False,
                                placeholder="Select IP Address to Filter by"
                            )
                        )
                    ],
                    className='shadow',
                ),
                width={'size': 4}
            ),
        ]
    )
    return filter_row
