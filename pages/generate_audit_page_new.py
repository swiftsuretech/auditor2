"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Builds a Form to generate a new audit.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt, timedelta
from functions.count_audits import clear_out_audits
from pages.conduct_audit_page import AuditPage
from functions.build_an_audit import Audit


class AuditForm:
    """An audit form allowing the user to select to and from dates, a percentage of records to
    audit and add a note"""

    def __init__(self):
        clear_out_audits()
        self.page = (
                        html.Div(
                            children=[
                                dbc.Card(
                                    children=[
                                        dbc.CardHeader(
                                            children=[
                                                html.I(className="fal fa-lg fa-clipboard-check mr-2"),
                                                html.I("Generate a New Audit"),
                                            ],
                                        ),
                                        dbc.Collapse(
                                            dbc.CardBody(
                                                children=[
                                                    dbc.Row(
                                                        children=[
                                                            dbc.Col(
                                                                dbc.FormGroup(
                                                                    [
                                                                        dbc.Label("Start", width=3,
                                                                                  style={'color': 'grey'}),
                                                                        dcc.DatePickerSingle(
                                                                            id='audit-date-picker-start',
                                                                            date=dt.now() - timedelta(days=90),
                                                                            display_format='DD/MM/YY',
                                                                        ),
                                                                    ]
                                                                ),
                                                                width=3,
                                                            ),
                                                            dbc.Col(
                                                                dbc.FormGroup(
                                                                    [
                                                                        dbc.Label("Finish", width=3,
                                                                                  style={'color': 'grey'}),
                                                                        dcc.DatePickerSingle(
                                                                            id='audit-date-picker-end',
                                                                            date=dt.now(),
                                                                            display_format='DD/MM/YY',
                                                                        ),
                                                                    ],
                                                                ),
                                                                width=3,
                                                            ),
                                                            dbc.Col(
                                                                dbc.FormGroup(
                                                                    [
                                                                        dcc.Slider(
                                                                            min=0,
                                                                            max=100,
                                                                            step=5,
                                                                            value=10,
                                                                            marks={0: '0%', 10: '10%', 20: '20%',
                                                                                   30: '30%',
                                                                                   40: '40%', 50: '50%', 60: '60%',
                                                                                   70: '70%',
                                                                                   80: '80%', 90: '90%', 100: '100%'},
                                                                            id="audit-percentage",
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        no_gutters=True,
                                                        id='audit_options'
                                                    ),
                                                    dbc.Row(
                                                        children=[
                                                            dbc.Col(
                                                                dbc.FormGroup(
                                                                    [
                                                                        dbc.Textarea(
                                                                            id="audit-notes",
                                                                            rows=2,
                                                                            placeholder="Write a note",
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                    )
                                                ],
                                            ),
                                            id='top-collapse',
                                            is_open=True
                                        ),
                                        dbc.CardHeader(
                                            children=[
                                                html.I(className="fal fa-lg fa-microscope mr-2"),
                                                html.I("Audit Scope"),
                                            ],
                                            className='border-top',
                                        ),
                                        dbc.Collapse(
                                            children=[
                                                dbc.CardBody(
                                                    html.H5(
                                                        id='audit-scope',
                                                        style={'text-align': 'center'},
                                                    ),
                                                    id='body-bg',
                                                ),
                                                dbc.CardFooter(
                                                    children=[
                                                        dbc.Button(
                                                            "Execute Audit",
                                                            className='mr-1 float-right mb-1',
                                                            disabled=True,
                                                            id='btn-execute-audit'
                                                        ),
                                                        dbc.Button(
                                                            "Cancel",
                                                            className='mr-1 float-right mb-1',
                                                            disabled=False,
                                                            id='btn-cancel-audit'
                                                        ),
                                                    ],
                                                    style={'height': '60px'}
                                                ),
                                            ],
                                            id='bottom-collapse',
                                            is_open=True
                                        ),
                                    ],
                                    className='mt-4'
                                ),
                            ],
                            style={'width': '90%', 'margin': 'auto'},
                        ),
                        html.Div(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            children=[
                                                dbc.Button('Approve', id='btn-audit-approve', color='success',
                                                           className='mr-2'),
                                                dbc.Button('Reject', id='btn-audit-reject', color='danger'),
                                            ],
                                            className='mb-3',
                                            width=2,
                                        ),
                                        dbc.Col(
                                            dbc.Progress(id='audit-progress', color='info', className='m-3'),
                                        )
                                    ],
                                ),
                            ],
                            style={'width': '90%', 'margin': 'auto'},
                            id='audit-controls',
                            hidden=True,
                        ),
                        html.Div(
                            id='audit-detail'
                        ),
                        html.Div(
                            id='cont-audit-detail'
                        )
                    ),
