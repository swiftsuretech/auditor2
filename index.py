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

# Instantiate our App and give it a name
app = dash.Dash("__name__")
app.title = "GossipAuditor2"

# Grab our main layout components
sidebar = Sidebar()
navbar = Navbar()
dashboard = Dashboard()

# Define our layout
app.layout = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    # Sidebar will be 2 / 12 of the page in Bootstrap format. We'll fix the position so it doesn't
                    # scroll with the rest of the page
                    sidebar,
                    width={'size': 2},
                    style={'background-color': '#2C3E50', 'position': 'fixed', 'height': '100%'}
                ),
                dbc.Col(
                    children=[
                        dbc.Row(
                            # Drop in the Dashboard page
                            dashboard.page
                        ),
                    ],
                    # As the sidebar is 2 / 12 we set the content page to 10 / 12 and offset it by 2 / 12
                    width={'size': 10, 'offset': 2}
                ),
            ],
            no_gutters=True
        ),
    ],
    # For some reason, Firefox renders and unnecessary x scroll bar. This gets rid of it.
    style={'overflow-x': 'hidden'}
)

# I put the callbacks in a separate file to avoid clutter. It needs to be called with the app and data object to work
register_callbacks(app, d)

# Fire the bad boy up here. If 'debug=True' is set as an argument you get debug info when running the app
# TODO disable debug mode before production
if __name__ == "__main__":
    app.run_server(debug=True)
