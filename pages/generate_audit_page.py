"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Builds a Form to generate a new audit.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt, timedelta
from functions.count_audits import clear_out_audits


class AuditForm:
    """An audit form allowing the user to select to and from dates, a percentage of records to
    audit and add a note"""

    def __init__(self):
        clear_out_audits()
        self.page = (
                        html.Div(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
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
                                                                                        date=dt.now() - timedelta(
                                                                                            days=90),
                                                                                        display_format='DD/MM/YY',
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            width=6,
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
                                                                            width=6,
                                                                        ),
                                                                    ],
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(
                                                                        dbc.FormGroup(
                                                                            [
                                                                                dcc.Slider(
                                                                                    min=0,
                                                                                    max=100,
                                                                                    step=5,
                                                                                    value=10,
                                                                                    marks={0: '0%', 10: '10%',
                                                                                           20: '20%',
                                                                                           30: '30%',
                                                                                           40: '40%', 50: '50%',
                                                                                           60: '60%',
                                                                                           70: '70%',
                                                                                           80: '80%', 90: '90%',
                                                                                           100: '100%'},
                                                                                    id="audit-percentage",
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
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
                                                            style={'height': '220px'}
                                                        ),
                                                        id='top-collapse',
                                                        is_open=True
                                                    ),
                                                ],
                                                className='mt-4 mb-4'
                                            ),
                                        ),
                                        dbc.Col(
                                            dbc.Card(
                                                children=[
                                                    dbc.CardHeader(
                                                        children=[
                                                            html.I(className="fal fa-lg fa-microscope mr-2"),
                                                            html.I("Define Scope"),
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
                                                                style={'height': '160px'}
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
                                                className='mb-4 mt-4',
                                            ),
                                        ),
                                    ],
                                ),

                            ],
                            style={'width': '90%', 'margin': 'auto'},
                        ),
                        html.Div(
                            children=[
                                dbc.Card(
                                    children=[
                                        dbc.CardHeader(
                                            children=[
                                                html.I(className='fal fa-lg fa-user-hard-hat mr-2'),
                                                html.I('Conducting Audit'),
                                            ]
                                        ),
                                        dbc.Collapse(
                                            dbc.CardBody(
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Button('Approve', id='btn-audit-approve',
                                                                           color='success',
                                                                           className='mr-2 '),
                                                                dbc.Button('Reject', id='btn-audit-reject',
                                                                           color='danger'),
                                                            ],
                                                            className='mb-1',
                                                            width=2,
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Progress(id='audit-progress', color='info',
                                                                             className='mt-3')
                                                            ],
                                                            width=8,
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Button('Cancel Audit', color='secondary',
                                                                           className='mr-2 float-right',
                                                                           id='btn-audit-cancel')
                                                            ],
                                                            width=2,
                                                        )
                                                    ],
                                                    className='my-auto'
                                                ),
                                            ),
                                            id='tools-collapse',
                                            is_open=True
                                        ),
                                    ],
                                    className='mb-4'
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
                            children=[
                                dbc.Card(
                                    children=[
                                        dbc.CardHeader(
                                            children=[
                                                html.I(className='fal fa-lg fa-flag-checkered mr-2'),
                                                html.I('Finalise Audit'),
                                            ]
                                        ),
                                        dbc.Collapse(
                                            dbc.CardBody(
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            html.H5("Finalise this audit? Once this is done it "
                                                                    "will be saved and you will be unable to change"
                                                                    " it"),
                                                            width=9,
                                                            className='float-left'
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Button('Finalise', id='btn-audit-finalise',
                                                                           color='success',
                                                                           className='mr-2 float-right'),
                                                                dbc.Button('Cancel', id='btn-final-cancel',
                                                                           color='danger',
                                                                           className='mr-2 float-right'),
                                                            ],
                                                            className='float-right'
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            id='final-collapse',
                                            is_open=True
                                        ),
                                    ],
                                    className='mb-4'
                                ),
                            ],
                            style={'width': '90%', 'margin': 'auto'},
                            id='finalise-audit',
                            hidden=True,
                        ),
                        html.Div(
                            dbc.Alert(
                                color='secondary',
                                id="alert",
                                is_open=False,
                                fade=True,
                                duration=1000,
                                style={'opacity': 0.6}
                            ),
                            style={'width': '90%', 'margin': 'auto'},
                        ),
                    ),
