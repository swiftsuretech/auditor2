"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Presents a page to illustrate all audits that have been created buy not yet conducted
"""

# Import Libraries:
from functions.count_audits import Audits
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from datetime import datetime as dt
import os
import os.path


class MyAudits:
    def __init__(self):
        au = Audits()
        gen = au.generated_count
        if gen == 1:
            aud_corrected = 'audit'
            have_corrected = 'has'
        else:
            aud_corrected = 'audits'
            have_corrected = 'have'
        intro = 'The following {} {} {} yet to be completed.'.format(gen, aud_corrected, have_corrected)
        self.page = html.Div(
            children=[
                html.Br(),
                html.Br(),
                dbc.Card(
                    children=[
                        dbc.CardHeader(
                            children=[
                                html.I(className="fal fa-lg fa-clipboard-check mr-2"),
                                html.I("Incomplete Audits")
                            ]
                        ),
                        dbc.CardBody(
                            html.H4(intro),
                        ),
                    ],
                    className='ml-5 mr-5',
                ),
                html.Div(
                    dbc.Row(
                        dbc.Col(
                            eval(generate_new_audit_cards()),
                            width=12,
                        ),
                    ),
                )
            ],
            style={'width': '100%', 'margin': 'auto'},
        )


def generate_new_audit_cards():
    audits = [name for name in os.listdir('audits/generated')]
    card = ''
    for count, audit in enumerate(audits):
        header, timestamp, start, stop, percent = audit.split('|')
        percent = percent.split('.')[0]
        # TODO we need to munge the dates to get them to work with this data. Will likely need
        #  fettling when move up to production.
        audit_time = dt.fromtimestamp(float(timestamp)).strftime('%H:%M')
        audit_date = dt.fromtimestamp(float(timestamp)).strftime('%d/%m/%Y')
        start = (start.split('-')[2] + '/' + start.split('-')[1] + '/' + start.split('-')[0])
        stop = (stop.split('-')[2][0:2] + '/' + stop.split('-')[1] + '/' + stop.split('-')[0])
        this_card = ('dbc.Card('
                     'children=['
                     'dbc.CardHeader('
                     'html.H5('
                     '\"Audit {}\"'
                     '),'
                     '),'
                     'dbc.CardBody('
                     'children =['
                     'html.P(\"Audit Generated on {}\"),'
                     'html.P(\"At {}\"),'
                     'html.P(\"Search Start: {}\"),'
                     'html.P(\"Search End: {}\"),'
                     'html.P(\"Audit Percentage: {}\")'
                     '],'
                     '),'
                     'dbc.CardFooter('
                     'dbc.Button(\"Delete\", '
                     'className=\"float-right\", color=\"danger\", id=\"btn-delete-audit-{}\"'
                     '),'
                     '),'
                     '],'
                     'className=\"ml-5 mt-5 float-left\",'
                     ')'
                     .format(count + 1, audit_date, audit_time, start, stop, percent, count))
        if card:
            card += (', ' + str(this_card))
        else:
            card = str(this_card)
        card = 'dbc.Row(dbc.Col(html.Div(children=[' + card + '],),),)'
    return card
