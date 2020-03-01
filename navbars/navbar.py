import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    navbar = dbc.Navbar(
        children=[
            dbc.Row(
                dbc.Col(
                    html.H4(
                        children=[
                            html.I(className="fal fa-analytics"),
                            html.I(" Main Dashboard", style={'font-style': 'italic', 'padding': '10px'})
                        ],
                    ),
                ),
                style={'padding-top': '12px'}
            ),
        ],
        color="light",
        dark=True,
        style={'height': '60px', 'border-bottom': '1px solid rgba(0, 0, 0, 0.125)'}
    )
    return navbar
