import dash
import plotly.express as px
import dash_core_components as dcc
import dash_table as dt
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import plotly.io as pio
import re

pio.templates.default = "seaborn"
logo = base64.b64encode(open("logos/cii-logo.png", 'rb').read()).decode('ascii')
df = pd.read_csv("./testData/chatter.csv")
app = dash.Dash("__name__")

navbar = dbc.Row(
    dbc.Col(
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Settings", href="#")),
                dbc.NavItem(dbc.NavLink("Logout", href='#'))
            ],
            brand="Chatter Logger",
            brand_href="#",
            color="primary",
            fluid=True,
            dark=True,
        ), width=12
    )
)

histo = dbc.Row(
    [
        # dbc.Col(
        #     html.Div(
        #         html.Img(src='data:image/png;base64,{}'.format(logo), height=100)
        #     ),
        #     width={"size": 2, "offset": 1}
        # ),
        dbc.Col(
            dcc.Graph(
                id="main-histogram",
                figure=px.histogram(df, x=df['transactionTime'],
                                    color=df['username'],
                                    labels={"transactionTime": "Query Time",
                                            "username": "User"}),
            )
            , width={"size": 12})
    ]
)

dtable = dbc.Row(
    dbc.Col(
        dt.DataTable(
            id="dtable",
            columns=[{"name": i, "id": i} for i in df.columns if not re.search('lat.*|long.*', i)],
            data=df.to_dict('records'),
            page_action="native",
            page_size=10
        )
        , width={'size': 10, "offset": 1}
    )
)

app.layout = html.Div([navbar, histo, dtable])

if __name__ == "__main__":
    app.run_server(debug=True)
