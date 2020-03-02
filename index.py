import dash
from pages.dashboard_page import data, Dashboard_Page
import dash_bootstrap_components as dbc
from callbacks.callbacks import register_callbacks
from navbars.sidebar import Sidebar
from navbars.navbar import Navbar
import dash_html_components as html

app = dash.Dash("__name__")
app.title = "Gossip Auditor 2"

sidebar = Sidebar()
navbar = Navbar()
dashboard = Dashboard_Page

app.layout = html.Div(
    children=[
        dbc.Row(
            children=[
                sidebar,
                dbc.Col(
                    children=[
                        navbar,
                        dashboard
                    ],
                    style={'padding': '0px'}
                ),
            ],
        ),
    ],
    style={'overflow-x': 'hidden'}
)

register_callbacks(app, data)


if __name__ == "__main__":
    app.run_server(debug=True)