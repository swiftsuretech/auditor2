"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
The home page gives an overview of the application and some links to the functional pages
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


class Home:
    """Returns the Home Page"""

    def __init__(self):
        self.page = dbc.Col(
            html.Div(
                dbc.Jumbotron(
                    [
                        html.H1(
                            children=[
                                html.Img(src='../assets/logos/atom.svg',
                                         style={'height': '120px', 'vertical-align': 'middle',
                                                'float': 'left'},
                                         className='ml-5'),
                                html.P("Chatter Auditor 2",
                                       className='ml-2'),
                            ],
                            className="display-4 ml-20"),
                        html.Hr(className="m-2"),
                        html.P(
                            "A Chatter flight plan audit and log analysis tool",
                            className="lead",
                        ),
                    ],
                    fluid=True,
                    className='shadow border'
                ),
                className='mt-3',
                style={'width': '90%', 'margin': 'auto'},
            ),
            width=12,
        )
