"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
The home page gives an overview of the application and some links to the functional pages
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

cards = html.Div(
    dbc.Row(
        dbc.CardDeck(
            children=[
                dbc.Card(
                    children=[
                        dbc.CardHeader(
                            html.H5("Dashboards", className="card-title"),
                        ),
                        dbc.CardBody(
                            [
                                html.Div(
                                    html.I(className='fad fa-chart-pie-alt fa-10x'),
                                    style={'text-align': 'center',
                                           '--fa-secondary-color': '#149A80',
                                           '--fa-secondary-opacity': '0.5'},
                                    className='mb-4 mt-3'
                                ),
                                html.P(
                                    children=[
                                        html.P('View all flight plans'),
                                        html.P('High level Overview'),
                                        html.P('Usage Monitoring'),
                                        html.P('Advanced Filtering and Analytics'),
                                    ],
                                ),
                            ]
                        ),
                        dbc.CardFooter(
                            dbc.Button(
                                "Click here", color="success", className="mt-auto float-right"
                            ),
                        ),
                    ],
                    className='shadow',
                ),
                dbc.Card(
                    children=[
                        dbc.CardHeader(
                            html.H5("New Audit", className="card-title"),
                        ),
                        dbc.CardBody(
                            [
                                html.Div(
                                    html.I(className='fad fa-check fa-10x'),
                                    style={'text-align': 'center',
                                           '--fa-secondary-color': '#D4860B',
                                           '--fa-secondary-opacity': '0.5'},
                                    className='mb-4 mt-3'
                                ),
                                html.P(
                                    "Generates an audit based upon user selection of date range and percentage of "
                                    "records to audit.",
                                ),
                                html.P(
                                    "Presents an auditor with a random selection of flight plans "
                                    "to audit based upon all search criteria, augmented with a map display and "
                                    "other information regarding geographical location.",
                                ),

                            ]
                        ),
                        dbc.CardFooter(
                            dbc.Button(
                                "Click here", color="warning", className="mt-auto float-right"
                            ),
                        ),
                    ],
                    className='shadow',
                ),
                dbc.Card(
                    children=[
                        dbc.CardHeader(
                            html.H5("Completed Audits", className="card-title"),
                        ),
                        dbc.CardBody(
                            [
                                html.Div(
                                    html.I(className='fad fa-flag-checkered fa-10x'),
                                    style={'text-align': 'center',
                                           '--fa-secondary-color': '#E12E1C',
                                           '--fa-secondary-opacity': '0.5'},
                                    className='mb-4 mt-3'
                                ),
                                html.P(
                                    "All completed audits are stored in the system and, once finalised, are not "
                                    "editable.",
                                ),
                                html.P(
                                    "Completed records contain details of date range, percentage and selected "
                                    "flight plans for audit purposes.",
                                ),
                            ]
                        ),
                        dbc.CardFooter(
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto float-right"
                            ),
                        ),
                    ],
                    className='shadow',
                ),
                dbc.Card(
                    children=[
                        dbc.CardHeader(
                            html.H5("About", className="card-title"),
                        ),
                        dbc.CardBody(
                            [
                                html.Div(
                                    html.I(className='fad fa-question fa-10x'),
                                    style={'text-align': 'center',
                                           '--fa-secondary-color': '#2384C6',
                                           '--fa-secondary-opacity': '0.5'},
                                    className='mb-4 mt-3'
                                ),
                                html.P(
                                    "Further information about the application, including instructions for "
                                    "getting support.",
                                    className="card-text",
                                ),

                            ]
                        ),
                        dbc.CardFooter(
                            dbc.Button(
                                "Click here", color="info", className="mt-auto float-right"
                            ),
                        ),
                    ],
                    className='shadow',
                ),
            ],
        ),
        className='mt-3',
        style={'width': '95%', 'margin': 'auto'},
    ),
)


class Home:
    """Returns the Home Page"""

    def __init__(self):
        self.page = dbc.Col(
            children=[
                html.Div(
                    dbc.Jumbotron(
                        [
                            html.H1(
                                children=[
                                    html.Img(
                                        src='../assets/logos/atom.svg',
                                        style={'height': '120px', 'vertical-align': 'middle',
                                               'float': 'left'},
                                        className='ml-5 mr-3'),
                                    html.P(
                                        " ChatterAuditor2",
                                        className='ml-5'),
                                ],
                                className="display-4 ml-20"),
                            html.Hr(
                                className="m-2"
                            ),
                            html.P(
                                "A Chatter flight plan audit and log analysis tool",
                                className="lead ml-5",
                            ),
                        ],
                        fluid=True,
                        className='',
                    ),
                    className='',
                    style={'width': '100%', 'margin': 'auto'},
                ),
                html.Div(
                    cards
                ),
            ],
            width=12,
        )
