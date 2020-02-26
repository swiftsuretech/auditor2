import dash
import plotly.graph_objects as go
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
users = df.username.unique()
randText = html.I(className="fas fa-quote-left fa-2x fa-pull-left text-white")

app = dash.Dash("__name__")

navbar = dbc.Row(
    dbc.Col(
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(randText),
                dbc.NavItem(dbc.NavLink("Settings", href="#")),
                dbc.NavItem(dbc.NavLink("Logout", href='#'))
            ],
            brand="Chatter Audit",
            brand_href="#",
            color="primary",
            fluid=True,
            dark=True,
        ), width=12
    )
)

x = df['transactionTime']
fig = go.Figure(data=[go.Histogram(x=x, xbins=dict(
    size=604800000),
                                   autobinx=False)])
fig.update_layout(
    xaxis_title_text='Query Date',
    yaxis_title_text='Number of Queries',
    bargap=0.1,
    barmode='stack'
)

bighist = dbc.Row(
    dbc.Col(
        dcc.Graph(
            figure=fig,
            id="bighist",
        )
        , width={"size": 12}
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

drop1 = dbc.Row(
    dbc.Col(
        dcc.Dropdown(
            options=[{"label": i, "value": i} for i in users],
            multi=True,
            placeholder="Select Users to Filter by"
        )
        , width={'size': 4}
    )
)

app.layout = html.Div([navbar, bighist, drop1, dtable])

if __name__ == "__main__":
    app.run_server(debug=True)
