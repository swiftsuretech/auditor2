"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
This function build out the side navigation bar of the app.
"""

import dash_html_components as html
import dash_core_components as dcc
from functions.get_all_records import FlightPlanList, DataSet
import dash_bootstrap_components as dbc

# Build a dictionary of labels and values to populate our search box.
flight_plan_list = [{'label': item, 'value': item} for item in FlightPlanList().df]
flight_plan_list2 = [{'label': label, 'value': value} for value, label in DataSet().flight_plan_dict.items()]

button_class = "btn btn-dark btn-block bg-primary border-0 text-left mb-1"
button_style = {'font-size': '16px', 'border': 'none'}
separator = html.Hr(style={'color': '#95a5a6', 'background-color': '#95a5a6', 'padding': 0})


def build_sidebar():
    """Build the sidebar of the app."""
    sidebar = html.Div(
        children=[
            # Logo and app name
            dbc.Row(
                html.Div(
                    children=[
                        html.Img(src='../assets/logos/atom.svg', style={'height': '40px', 'vertical-align': 'middle',
                                                                        'float': 'left', 'padding-left': '7px'}),
                        html.Span(html.H4("GossipAuditor2"),
                                  style={'color': 'white', 'float': 'left', 'margin-top': '7px',
                                         'margin-left': '15px'},
                                  ),
                    ],
                ),
            ),
            separator,
            html.Div(
                children=[
                    dbc.Row(
                        "Search Flight Plans",
                        id='lbl_search_flightplan', style=button_style, className='text-secondary'
                    ),
                ],
                style={'padding-left': '10px', 'padding-bottom': '10px'}
            ),

            # Search bar
            dbc.Row(
                dbc.Col(
                    dcc.Dropdown(id='sidebar_search', options=flight_plan_list2,
                                 placeholder='Quick Search', style={'color': 'black'})
                ),
                className="row justify-content-center"
            ),
            separator,
            html.Div(
                children=[
                    dbc.Row(
                        "Navigation",
                        id='lbl_navigation', style=button_style, className='text-secondary'
                    ),
                ],
                style={'padding-left': '10px', 'padding-right': '10px'},
            ),

            # Navigation Buttons
            html.Div(
                children=[
                    dbc.Row(
                        dbc.Button(
                            (html.I(className='fal fa-lge fa-fw fa-home-lg-alt mr-2'),
                             " Home"),
                            id='btn_home',
                            style=button_style, className=button_class
                        )
                    ),
                    dbc.Row(
                        dbc.Button(
                            (html.I(className='fal fa-lge fa-fw fa-tachometer-alt mr-2'),
                             " Dashboard"),
                            id='btn_dashboard',
                            style=button_style, className=button_class
                        )
                    ),
                    dbc.Row(
                        dbc.Button(
                            (html.I(className='fal fa-lge fa-fw fa-plane-departure mr-2'),
                             " Flight Plans"),
                            id='btn_flightplan',
                            style=button_style, className=button_class
                        )
                    ),
                ],
                style={'padding-left': '10px', 'padding-right': '10px'}
            ),
            html.Div(
                children=[
                    separator,
                    dbc.Row(
                        "Audit Functions",
                        id='lbl_audit', style=button_style, className='text-secondary'
                    ),
                    dbc.Row(
                        dbc.Button(
                            (html.I(className='fal fa-lge fa-fw fa-clipboard-check mr-2'),
                             " Generate Audit"),
                            id='btn_new_audit',
                            style=button_style, className=button_class
                        )
                    ),
                    dbc.Row(
                        dbc.Button(
                            (html.I(className='fal fa-lge fa-fw fa-cabinet-filing mr-2'),
                             " View Complete Audits"),
                            id='btn_all_audits',
                            style=button_style, className=button_class
                        )
                    ),
                    # Hidden input
                    dcc.Input(value=None, type='number', id='test', style={'display': 'none'}),
                ],
                style={'padding-left': '10px'}
            ),
        ],
        style={'margin': '20px'}
    ),
    return sidebar
