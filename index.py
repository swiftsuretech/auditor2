import dash
from pages.dashboard_page import data, Dashboard_Page
import dash_bootstrap_components as dbc
from callbacks.callbacks import register_callbacks
from navbars.sidebar import Sidebar
from navbars.navbar import Navbar
import dash_html_components as html

app = dash.Dash("__name__")
app.title = "GossipAuditor2"

sidebar = Sidebar()
navbar = Navbar()
dashboard = Dashboard_Page

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
                            dashboard
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

register_callbacks(app, data)

if __name__ == "__main__":
    app.run_server(debug=True)
