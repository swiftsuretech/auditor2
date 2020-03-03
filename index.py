"""
*** Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team ***
Run the app from here. Defines a flask application based upon the dash framework. There are 3 x key parts:
1 - Instantiate a dash app called app.
2 - Define a layout.
3 - Run the server.
I have put the callbacks in a separate file to avoid clutter. I call these callback with a function called
"register_callbacks"
"""

# Import our Dash bits and pieces and some settings etc.
import dash
from pages.dashboard_page import Dashboard, d
import dash_bootstrap_components as dbc
from callbacks.callbacks import register_callbacks
from navbars.sidebar import Sidebar
from navbars.navbar import Navbar
import dash_html_components as html

app = dash.Dash("__name__")
app.title = "GossipAuditor2"

sidebar = Sidebar()
navbar = Navbar()
dashboard = Dashboard()

app.layout = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    sidebar,
                    width={'size': 2},
                    style={'background-color': '#2C3E50', 'position': 'fixed', 'height': '100%'}
                ),
                dbc.Col(
                    children=[
                        dbc.Row(
                            dashboard.page
                        ),
                    ],
                    width={'size': 10, 'offset': 2}
                ),
            ],
            no_gutters=True
        ),
    ],
    style={'overflow-x': 'hidden'}
)

register_callbacks(app, d)

if __name__ == "__main__":
    app.run_server(debug=True)
