"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Defines a Single_Record Class  (page) consisting of an html Div with all the components
laid out in order.  We divide the record page up using the Bootstrap Grid system.
This defines the static layout with an initial record, 'r', which is returned by instantiating a
'Record' object.
"""

# Import our libraries
from settings.settings import space, html, field_mapping
from functions.get_single_record import Record
from functions.build_map import MapBox
import dash_bootstrap_components as dbc

# Some reusable styling:
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
        ]
    )
    return card


class SingleRecordPage:
    """Generates our Single Record layout. Build the data card from the sub cards created
    in the build_card function"""

    def __init__(self, authid):
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
        country_flag = 'assets/flags/' + str(r.dict['Country Code'][0]) + '.svg'
        self.page = html.Div(
            children=[
                html.Br(),
                html.Br(),
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
                        )
                    ],
                ),
            ],
            style={'width': '90%', 'margin': 'auto'},
        )
