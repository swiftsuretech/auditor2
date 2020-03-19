"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
The home page gives an overview of the application and some links to the functional pages
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

check = html.I(className='fal fa-lge fa-check-circle mr-2', style={'color': 'green'})

cards = html.Div(
    dbc.Row(
        dbc.CardDeck(
            children=[
                dbc.Card(className='shadow',
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
                                             html.Br(),
                                             check,
                                             html.B('View all flight plans'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('High level overview'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('Usage monitoring'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('Advanced filtering and analytics'),
                                         ],
                                     ),
                                 ]
                             ),
                             dbc.CardFooter(
                                 dbc.Button(
                                     "Click here",
                                     color="success",
                                     className="mt-auto float-right",
                                     id='btn-home-dashboards'
                                 ),
                             ),
                         ],
                         ),
                dbc.Card(className='shadow',
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
                                         children=[
                                             html.Br(),
                                             check,
                                             html.B('Create new audits'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('Select date ranges'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('Determine audit percentages'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('View enhanced geo data'),
                                         ],
                                     ),

                                 ]
                             ),
                             dbc.CardFooter(
                                 dbc.Button(
                                     "Click here",
                                     color="warning",
                                     className="mt-auto float-right",
                                     id='btn-home-new-audit'
                                 ),
                             ),
                         ],
                         ),
                dbc.Card(className='shadow',
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
                                         children=[
                                             html.Br(),
                                             check,
                                             html.B('View completed audits'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('Check audited flight plans'),
                                             html.Br(),
                                             html.Br()
                                         ],
                                     ),
                                 ]
                             ),
                             dbc.CardFooter(
                                 dbc.Button(
                                     "Click here",
                                     color="danger",
                                     className="mt-auto float-right",
                                     id='btn-home-completed-audits'
                                 ),
                             ),
                         ],
                         ),
                dbc.Card(className='shadow',
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
                                         children=[
                                             html.Br(),
                                             check,
                                             html.B('Get application help'),
                                             html.Br(),
                                             html.Br(),
                                             check,
                                             html.B('View support details'),
                                             html.Br(),
                                             html.Br(),
                                         ],
                                     ),
                                 ]
                             ),
                             dbc.CardFooter(
                                 dbc.Button(
                                     "Click here",
                                     color="info",
                                     className="mt-auto float-right",
                                     id='btn-home-about'
                                 ),
                                 ()),
                         ],
                         ),
            ],
            style={'width': '100%', 'margin': 'auto'}
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
                                        className='ml-5'
                                    ),
                                ],
                                className="display-4 ml-20"),
                            html.Hr(
                                className="m-2 mr-5",
                                style={'width': '600px'}
                            ),
                            html.P(
                                "< A Chatter flight plan auditing and log analysis tool >",
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
