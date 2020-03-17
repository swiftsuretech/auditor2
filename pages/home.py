"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
The home page gives an overview of the application and some links to the functional pages
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

cards = html.Div(
    dbc.Row(
        children=[
            dbc.Col(
                [
                    dbc.Card(
                        children=[
                            dbc.CardHeader(
                                html.H5("Dashboards", className="card-title"),
                            ),
                            dbc.CardImg(
                                src='/assets/dashboard.png',
                                bottom=True,
                                style={'opacity': 0.5, 'width': '100px', 'height': '100px'}
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
                        className='shadow'
                    ),
                ],
            ),
            dbc.Col(
                [
                    dbc.Card(
                        children=[
                            dbc.CardHeader(
                                html.H5("New Audit", className="card-title"),
                            ),
                            dbc.CardImg(
                                src='/assets/new.png',
                                bottom=True,
                                style={'opacity': 0.5, 'width': '100px', 'height': '100px'}
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
                        className='shadow'
                    ),
                ],
            ),
            dbc.Col(
                [
                    dbc.Card(
                        children=[
                            dbc.CardHeader(
                                html.H5("Completed Audits", className="card-title"),
                            ),
                            dbc.CardImg(
                                src='/assets/completed.png',
                                bottom=True,
                                style={'opacity': 0.5, 'width': '100px', 'height': '100px'}
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
                        className='shadow'
                    ),
                ],
            ),
            dbc.Col(
                [
                    dbc.Card(
                        children=[
                            dbc.CardHeader(
                                html.H5("About", className="card-title"),
                            ),
                            dbc.CardImg(
                                src='/assets/about.png',
                                bottom=True,
                                style={'opacity': 0.5, 'width': '100px', 'height': '100px'},
                                className='align-center'
                            ),
                            dbc.CardBody(
                                [

                                    html.P(
                                        "About this application",
                                        className="card-text",
                                    ),
                                    dbc.Button(
                                        "Click here", color="secondary", className="mt-auto"
                                    ),
                                ]
                            )
                        ],
                        className='shadow'
                    ),
                ],
            ),
        ],
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
                                        "ChatterAuditor2",
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
