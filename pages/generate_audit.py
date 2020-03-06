"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Builds a Form to generate a new audit
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt, timedelta


class AuditForm:
    """An audit form allowing the user to select to and from dates, a percentage of records to
    audit and add a note"""

    def __init__(self):
        self.page = html.Div(
            children=[
                html.Br(),
                html.Br(),
                dbc.Row(
                    children=[
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    dbc.CardHeader(
                                        children=[
                                            html.I(className="fal fa-lg fa-clipboard-list-check mr-2"),
                                            html.I("Generate a New Audit")
                                        ]
                                    ),
                                    dbc.CardBody(
                                        children=[
                                            dbc.Col(
                                                children=[

                                                    dbc.FormGroup(
                                                        [
                                                            html.I(className="fal mr-2 fa-lg fa-calendar-times",
                                                                   style={'color': 'grey'}),
                                                            html.I("Select the date range you wish to check",
                                                                   style={'color': 'grey'}),
                                                        ]
                                                    ),

                                                    dbc.FormGroup(
                                                        [
                                                            dbc.Label("Start", width=3, style={'color': 'grey'}),
                                                            dcc.DatePickerSingle(
                                                                id='audit-date-picker-start',
                                                                date=dt.now() - timedelta(days=28),
                                                                display_format='DD/MM/YY',
                                                            ),
                                                        ]
                                                    ),

                                                    dbc.FormGroup(
                                                        [
                                                            dbc.Label("Finish", width=3, style={'color': 'grey'}),
                                                            dcc.DatePickerSingle(
                                                                id='audit-date-picker-end',
                                                                date=dt.now(),
                                                                display_format='DD/MM/YY',
                                                            ),
                                                        ],
                                                    ),
                                                    dbc.FormGroup(
                                                        [
                                                            html.I(className="fal mr-2 fa-lg fa-percent",
                                                                   style={'color': 'grey'}),
                                                            html.I("Percentage of Flight Plans to Check",
                                                                   style={'color': 'grey'}, className="mr-5"),
                                                        ]
                                                    ),

                                                    dbc.FormGroup(
                                                        [
                                                            dcc.Slider(
                                                                min=0,
                                                                max=100,
                                                                step=1,
                                                                value=10,
                                                                marks={0: '0%', 10: '10%', 20: '20%', 30: '30%',
                                                                       40: '40%', 50: '50%', 60: '60%', 70: '70%',
                                                                       80: '80%', 90: '90%', 100: '100%'},
                                                                id="audit-percentage",
                                                            ),
                                                        ],
                                                    ),

                                                    dbc.FormGroup(
                                                        [
                                                            html.Div(
                                                                id='percent-readout',
                                                                style={'color': 'grey'},
                                                                className='h4'
                                                            )
                                                        ],
                                                        style={'text-align': 'center'}
                                                    ),

                                                    dbc.FormGroup(
                                                        [
                                                            html.I(className="fal mr-2 fa-lg fa-sticky-note",
                                                                   style={'color': 'grey'}),
                                                            html.I("Note", style={'color': 'grey'}),
                                                        ]
                                                    ),
                                                    dbc.FormGroup(
                                                        [
                                                            dbc.Textarea(
                                                                id="audit-notes",
                                                                rows=3,
                                                                placeholder="Write a note",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    dbc.CardFooter(
                                        children=[
                                            dbc.Button('Cancel', className='', id='btn-cancel-audit',
                                                       style={'float': 'right'}),
                                            dbc.Button('Generate', className='mr-2', id='btn-generate-audit',
                                                       style={'float': 'right'}),
                                        ],
                                    )
                                ],
                            ),
                            width={'size': 4, 'offset': 4}
                        ),
                    ],
                    form=True,
                ),
            ],
            style={'width': '90%', 'margin': 'auto'},

        )
