"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
This page leads the user through a pre-defined audit. For each selected record in the audit, the user will
be shown the flight plan details and plot. They will be given the opportunity to tick or cross each flight
plan in the audit. Each audit is represented by a file stored in 'audits' directory which is a simple json
blob containing some high level details of the audit, as well as the plans selected and their status
"""

# Import our libraries
from settings.settings import space, html, field_mapping
from functions.get_single_record import Record
from functions.get_all_records import DataSet
from functions.build_map import MapBox
from functions.count_audits import return_audit_ids
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from functions import get_all_records

# There should be a single audit file in the 'audits/generated' directory, the return_audit_ids function
# will read it in as a json and extract a list of indexes of the flight plans we need to audit as well
# as a count
audit_id, id_count, filename = return_audit_ids()

# Define some styling variables as we are going to iteratively build out our page
header_style = {'margin-bottom': '5px', 'margin-top': '5px'}

# Define our cards here. list[0] is the list of headers, [1] is the font awesome icon and
# [2] is the column width.
user_card = [
    ['Operator', 'IP Address', 'Query Date', 'Query Time'],
    [html.I(className="fal fa-lg fa-id-badge fa-2x", style=header_style)],
    [4]
]

query_card = [
    ['Search From', 'Search To', 'Platform', 'User Names'],
    [html.I(className="fal fa-lg fa-telescope fa-2x", style=header_style)],
    [4]
]

geo_card = [
    ['Search Area', 'Nearest City'],
    [html.I(className="fal fa-lg fa-map-marked-alt fa-2x", style=header_style)],
    [4]
]


def build_card(card_lists, r):
    """Build our Cards. A function to take the card definitions above and return a Div with a card header and body"""
    all_rows = list()
    for item in card_lists[0]:
        col_left = dbc.Col(html.B(item), width=4, className="border-right", style={'margin': '0px'})
        col_right = dbc.Col(html.P(r.dict[item], className="text-info", style={'margin': '0px'}), width=8)
        single_row = dbc.Row([col_left, col_right], style={'padding': '2px', 'margin': '0px'})
        all_rows.append(single_row)
    title = html.I(card_lists[1])
    card = html.Div(
        children=[
            dbc.CardHeader(title, style={'text-align': 'center', 'padding': '0px'}, className='border-top'),
            dbc.CardBody(all_rows, style={'margin': '3px', 'height': '100%'})
        ],
    )
    return card


def build_geo(flag, r, polygon):
    """This will build out and return the right hand side column of the page which will show the
    flag of the record nation and the tile map displaying the polygon(s)"""
    card = html.Div(
        children=[
            dbc.CardHeader(
                children=[
                    html.I(className="fal fa-lg fa-plane-departure fa-2x", style=header_style),
                ],
                style={'text-align': 'center', 'padding': '0px'}
            ),
            dbc.CardBody(
                children=[
                    html.Img(src=flag, width=40, className='border', style={
                        'text-align': 'center', 'float': 'right'}),
                    html.H3("Flight Plan:", style={'float': 'left'}),
                    html.Pre('             ', style={'float': 'left'}),
                    html.H3(r.dict['Flight Plan'], style={'float': 'center'}, className='text-info'),
                ],
                className="border-bottom"
            ),
            dbc.CardHeader(
                children=[
                    html.I(className="fal fa-lg fa-globe-stand fa-2x", style=header_style)
                ],
                style={'text-align': 'center', 'padding': '0px'}
            ),
            dbc.CardBody(
                MapBox(polygon).map
            )
        ],
    )
    return card


class AuditPage:
    """Generates our Single Record layout. Build the data card from the sub cards created
    in the build_card function. First we load up the first audit selected item."""

    def __init__(self, authid=7):
        # FIXME need a better way to handle default authid
        # Pull our record by instantiating the 'Record" class with a record ID argument.
        r = Record(authid)
        # Ensure that we return a record, otherwise trap the error gracefully.
        if not r.found:
            print('Record not found')
            exit()
        polygon = r.dict['polygon'][0]
        # Change the filed names to something easier on the eye. The mapping file is in settings.py
        r.dict = dict((field_mapping[key], value) for key, value in r.dict.items())
        # Build a url reference to a flag that sits in the 'flags' directory in our site assets
        country_flag = 'assets/flags/{0}.svg'.format(str(r.dict['Country Code'][0]))
        self.order = 0
        self.page = html.Div(
            id='audit-page',
            children=[
                dbc.Card(className='shadow', 
                    children=[
                        dbc.CardBody(
                            dbc.Row(
                                children=[
                                    dbc.Col(
                                        dbc.Card(className='shadow', 
                                            children=[
                                                build_card(user_card, r),
                                                build_card(query_card, r),
                                                build_card(geo_card, r),
                                            ],
                                            style={'padding': '0px', 'height': '100%'},
                                        ),
                                        width=5,
                                    ),
                                    dbc.Col(
                                        dbc.Card(className='shadow', 
                                            children=[
                                                build_geo(country_flag, r, polygon),
                                            ],
                                            style={'padding': '0px', 'height': '100%'},
                                        ),
                                        width=7,
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ],
            style={'width': '90%', 'margin': 'auto'},
        )
