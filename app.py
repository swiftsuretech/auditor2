import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import plotly.io as pio

pio.templates.default = "seaborn"
logo = base64.b64encode(open("logos/cii-logo.png", 'rb').read()).decode('ascii')
df = pd.read_csv("./testData/chatter.csv")
stylesheets = [dbc.themes.SPACELAB]
app = dash.Dash(__name__, external_stylesheets=stylesheets)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Settings", href="#")),
        dbc.NavItem(dbc.NavLink("Logout", href='#'))
    ],
    brand="Chatter Logger",
    brand_href="#",
    color="primary",
    dark=True,
)

histo = dbc.Row(
    [
        dbc.Col(
            html.Div(
                html.Img(src='data:image/png;base64,{}'.format(logo), height=200)
            ),
            width={"size": 2, "offset": 1}
        ),
        dbc.Col(
            dcc.Graph(
                id="main-histogram",
                figure=px.histogram(df, x=df['transactionTime'],
                                    color=df['username'],
                                    labels={"transactionTime": "Query Time",
                                            "username": "User"}),
            )
            , width={"size": 8})
    ]
)

app.layout = html.Div([navbar, histo])

if __name__ == "__main__":
    app.run_server(debug=True)
