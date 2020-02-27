import dash
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_table as dt
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import plotly.io as pio
import re

pio.templates.default = "seaborn"
logo = base64.b64encode(open("assets/logos/cii-logo.png", 'rb').read()).decode('ascii')
df = pd.read_csv("./testData/chatter.csv")
users = df.username.unique()
platforms = df.platform.unique()

app = dash.Dash("__name__")

## Define the Nav Bar

navbar = dbc.Row(
    dbc.Col(
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-tools fa-lg text-white"), href="#")),
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-sign-out-alt fa-lg text-white"), href="#")),
            ],
            brand="Chatter Auditor",
            brand_href="#",
            color="primary",
            fluid=True,
            dark=True,
        ), width=12
    )
)

## Define the Time / Activity Histogram

x = df['transactionTime']
histo = go.Figure(data=[go.Histogram
                        (x=x, xbins=dict
                        (size=604800000),
                         autobinx=False)
                        ])
histo.update_layout(
    xaxis_title_text='Query Date',
    yaxis_title_text='Number of Queries',
    bargap=0.1,
    barmode='stack'
)

bighist = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader("Queries by Week"),
                dbc.CardBody(
                    [
                        dcc.Graph(
                            figure=histo,
                            id="bighist",

                        )
                    ]
                )
            ]
        )
        , width={"size": 10, 'offset': 1}
    )
)

## Define the Data Table

dtable = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader("Query Table"),
                dbc.CardBody(
                    dt.DataTable(
                        style_data={
                        },
                        style_cell={
                            'textAlign': 'left',
                        },
                        style_table={
                            'maxHeight': '600px',
                        },

                        style_cell_conditional=[
                            {'if': {'column_id': 'id'},
                             'width': '10%'},
                            {'if': {'column_id': 'username'},
                             'width': '15%'},
                            {'if': {'column_id': 'platform'},
                             'width': '25%'},
                            {'if': {'column_id': 'authorizationID'},
                             'width': '25%'},
                        ],

                        id="dtable",
                        columns=[{"name": i, "id": i} for i in df.columns if
                                 not re.search('^lat.*|^long.*|^polygon|^usernames|^start|^end', i)],
                        data=df.to_dict('records'),
                        page_action="native",
                        page_size=10,
                        sort_action="native",
                    )
                )
            ]

        )
        , width={'size': 10, 'offset': 1},
    )
)

## Define the User Dropdown

drop1 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader("Filter by User"),
                    dbc.CardBody(
                        dcc.Dropdown(
                            options=[{"label": i, "value": i} for i in users],
                            multi=True,
                            placeholder="Select Users to Filter by"
                        )
                    )
                ]
            )
            , width={'size': 3, 'offset': 1}
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader("Filter by Platform"),
                    dbc.CardBody(
                        dcc.Dropdown(
                            options=[{"label": i, "value": i} for i in platforms],
                            multi=True,
                            placeholder="Select Users to Filter by"
                        )
                    )
                ]
            )
            , width={'size': 3}
        )
    ]
)

## Define the platform Pie Chart

pie = go.Figure(
    data=[go.Pie(labels=platforms, values=[2, 4, 5, 6, 8], hole=0.5)]
)

platring = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.I(className="fab fa-apple fa-lg text-black"),
                        html.I("  Platform")
                    ]),
            dbc.CardBody(
                dcc.Graph(
                    figure=pie,
                    id="platring",
                    style={'height': 350},
                )
            )
]
)
, width = {"size": 4, "offset": 1}
)
)

app.layout = html.Div(
    [navbar, html.Br(), bighist, html.Br(), platring, html.Br(), drop1, html.Br(), dtable],
)

if __name__ == "__main__":
    app.run_server(debug=True)
