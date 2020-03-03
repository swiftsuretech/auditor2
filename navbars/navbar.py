"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
"""

# Import Libraries
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt


def build_navbar():
    """Builds out the Navigation Bar at the top of the page"""
    navbar = html.Div(
        dbc.Navbar(
            children=[
                dbc.Row(
                    children=[
                        dbc.Col(
                            html.Div(
                                html.H4(
                                    children=[
                                        html.I(className="fal fa-analytics"),
                                        html.I(" Main Dashboard", style={'font-style': 'italic', 'padding': '10px'})
                                    ],
                                ),
                                style={'padding-top': '12px', 'float': 'left'},
                            ),
                            style={'float': 'left'},
                            width={'size': 6},
                        ),
                        dbc.Col(
                            html.Div(
                                dcc.DatePickerRange(
                                    id='date-picker-range',
                                    start_date=dt(1997, 5, 3),
                                    end_date_placeholder_text='Select a date!'
                                ),
                            ),
                            style={'float': 'left'},
                            width={'size': 2, 'offset': 4},
                        ),
                    ],
                ),
            ],
            color="light",
            dark=True,
            style={'height': '60px', 'border-bottom': '1px solid rgba(0, 0, 0, 0.125)'},
        ),
    ),
    return navbar
