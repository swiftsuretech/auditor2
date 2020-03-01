import dash_html_components as html
import dash_bootstrap_components as dbc


def Sidebar():
    sidebar = dbc.Col(
        html.Div(
            [
                html.Img(src='../assets/logos/atom.svg',
                         style={'height': '60px',
                                'padding': '15px',
                                'float': 'left'}),
                html.H4("Gossip Auditor 2",
                        style={'padding': '17px',
                               'color': 'white'}),
            ],
            style={'vertical-align': 'middle'}
        ),
        width=2,
        style={'background-color': '#2C3E50'}
    )
    return sidebar
