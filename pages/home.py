"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
The home page gives an overview of the application and some links to the functional pages
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

cards = html.Div(
    dbc.CardGroup(
        [
            dbc.Card(
                children=[
                    dbc.CardHeader(
                        html.H5("Dashboards", className="card-title"),
                    ),
                    dbc.CardImg(
                        src='/assets/dash.jpg',
                        bottom=True,
                        style={'opacity': 0.5, 'height': '150px'}
                    ),
                    dbc.CardBody(
                        [

                            html.P(
                                "View the access dashboards.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="success", className="mt-auto"
                            ),
                        ]
                    )
                ],
            ),
            dbc.Card(
                children=[
                    dbc.CardHeader(
                        html.H5("New Audit", className="card-title"),
                    ),
                    dbc.CardImg(
                        src='/assets/create.jpg',
                        bottom=True,
                        style={'opacity': 0.5, 'height': '150px', 'background-size': 'contain'}
                    ),
                    dbc.CardBody(
                        [
                            html.P(
                                "Generate a new audit.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="warning", className="mt-auto"
                            ),
                        ]
                    ),
                ],
            ),
            dbc.Card(
                children=[
                    dbc.CardHeader(
                        html.H5("Completed Audits", className="card-title"),
                    ),
                    dbc.CardImg(
                        src='/assets/complete.jpg',
                        bottom=True,
                        style={'opacity': 0.5, 'height': '150px'}
                    ),
                    dbc.CardBody(
                        [
                            html.P(
                                "View previously completed audits",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    ),
                ],
            ),
        ],
        className='shadow',
    ),
    className='mt-3',
    style={'width': '90%', 'margin': 'auto'},
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
                                        className='ml-5'),
                                    html.P(
                                        "Chatter Auditor 2",
                                        className='ml-2'),
                                ],
                                className="display-4 ml-20"),
                            html.Hr(
                                className="m-2"
                            ),
                            html.P(
                                "A Chatter flight plan audit and log analysis tool",
                                className="lead",
                            ),
                        ],
                        fluid=True,
                        className='shadow border',
                    ),
                    className='mt-3',
                    style={'width': '90%', 'margin': 'auto'},
                ),
                html.Div(
                    cards
                ),
            ],
            width=12,
        )
