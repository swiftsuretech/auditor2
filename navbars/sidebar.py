"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
"""


import dash_html_components as html


def build_sidebar():
    """

    :return:
    """
    sidebar = html.Div(
            [
                html.Img(src='../assets/logos/atom.svg',
                         style={'height': '60px',
                                'padding': '15px',
                                'float': 'left'}),
                html.H5("GossipAuditor2",
                        style={'padding': '17px',
                               'color': 'white'}),
            ],
            style={'vertical-align': 'middle'}
        ),
    return sidebar
