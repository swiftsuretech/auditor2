"""A placeholder page where a single record has not been selected"""

import dash_bootstrap_components as dbc
import dash_html_components as html


class SelectRecordPage:
    """Returns a static page telling user to select a flightplan"""

    def __init__(self):
        self.page = html.Div(
            children=[
                html.Br(),
                html.Br(),
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            dbc.Card(
                                children=[
                                    dbc.CardHeader(
                                        children=[
                                            html.I(className="fal fa-lg mr-2 fa-info-circle"),
                                            html.I(" Info"),
                                        ],
                                    ),
                                    dbc.CardBody(
                                        html.H4('Select a Flight Plan from the search box on the left to continue'),
                                    ),
                                ],
                                className="ml-5 shadow",
                            ),
                        ),
                    ),
                ),
            ],
        )
