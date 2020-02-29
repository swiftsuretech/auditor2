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
import plotly.express as px

pio.templates.default = "seaborn"
logo = base64.b64encode(open("assets/logos/cii-logo.png", 'rb').read()).decode('ascii')
df = pd.read_csv("./testData/chatter.csv", parse_dates=['transactionTime'])
df['dayOfWeek'] = df['transactionTime'].dt.day_name()
users = df.username.unique()
platforms = df.platform.unique()
diagMargins = dict(t=10, b=10, l=10, r=10)
x = df['transactionTime']
app = dash.Dash("__name__")
app.title = "Chatter Auditor"
sp = html.Br()

title = dbc.Row(
    [
        html.H1(html.Pre("   ")),
        html.I(className="fal fa-user-chart fa-lg",
               style={"font-size": "65px"}),
        html.H1(html.Pre("[Main Dashboard]", className='body',
                         style={"color": "#777777",
                                'margin-top': '0.4rem'
                                }
                         )
                )
    ]
)

## Define the Nav Bar

navbar = dbc.Row(
    dbc.Col(
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink(html.I(className="fal fa-cogs fa-lg"), href="#")),
                dbc.NavItem(dbc.NavLink(html.I(className="fal fa-sign-out-alt fa-lg"), href="#")),
            ],
            brand="Chatter Auditor",
            brand_href="#",
            color="primary",
            fluid=True,
            dark=True,
        ), width=12
    )
)

## Define Activity Histogram

firstDate = df.transactionTime.min()
lastDate = df.transactionTime.max()

spread = (lastDate - firstDate).days // 7

hist2 = px.histogram(df, x="transactionTime", color="username", nbins=spread)
hist2.update_layout(
    height=350,
    xaxis_title_text='Query Date',
    yaxis_title_text='Number of Queries',
    bargap=0.1,
    barmode='stack',
    margin=diagMargins,
    legend_title="Operator"
)

histDay = px.histogram(df, y=df["dayOfWeek"], orientation='h',
                       labels={'Monday': 'Mon', 'Tuesday': 'Tue',
                               'Wednesday': 'Wed', 'Thursday': 'Thu',
                               'Friday': 'Fri', 'Saturday': 'Sat',
                               'Sunday': 'Sun'})

histDay.update_layout(
    height=350,
    xaxis_title_text='Day of Week',
    yaxis_title_text='Number of Queries',
    bargap=0.3,
    barmode='stack',
    margin=diagMargins,
    yaxis=dict(categoryorder='array',
               categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday',
                              'Tuesday', 'Monday'])
)

bighist = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.I(className="fal fa-lg fa-chart-bar"),
                        html.I(" Queries by Week")
                    ]
                ),
                dbc.CardBody(
                    [
                        dcc.Graph(
                            figure=hist2,
                            id="bighist",
                        )
                    ]
                )
            ]
        )
        , width={"size": 12}
    )
)

littlehist = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.I(className="fal fa-lg fa-chart-bar"),
                        html.I(" Queries by Week")
                    ]
                ),
                dbc.CardBody(
                    [
                        dcc.Graph(
                            figure=histDay,
                            id="histDay",
                        )
                    ]
                )
            ]
        )
        , width={"size": 4}
    )
)

## Define the Data Table

dtable = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.I(className="fal fa-lg fa-table"),
                        html.I(" Queries Table")
                    ]
                ),
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
                    , style={'margin-top': '0rem'}
                )
            ]
        )
        , width={'size': 12},
    )
)

## Define the User Dropdown

drop1 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-filter fa-lg text-black"),
                            html.I("  Filter by Operator"),
                        ]
                    ),
                    dbc.CardBody(
                        dcc.Dropdown(
                            options=[{"label": i, "value": i} for i in users],
                            multi=True,
                            placeholder="Select Users to Filter by"
                        )
                    )
                ]
            )
            , width={'size': 4}
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-filter fa-lg text-black"),
                            html.I("  Filter by Platform"),
                        ]
                    ),
                    dbc.CardBody(
                        dcc.Dropdown(
                            options=[{"label": i, "value": i} for i in platforms],
                            multi=True,
                            placeholder="Select Users to Filter by"
                        )
                    )
                ]
            )
            , width={'size': 4}
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-filter fa-lg text-black"),
                            html.I("  Filter by IP Address"),
                        ]
                    ),
                    dbc.CardBody(
                        dcc.Dropdown(
                            options=[{"label": i, "value": i} for i in users],
                            multi=True,
                            placeholder="Select IP Address to Filter by"
                        )
                    )
                ]
            )
            , width={'size': 4}
        ),
    ]
)

## Define the platform Pie Chart


pieplat = px.pie(df, names='platform', hole=0.6)
pieplat.update_layout(
    margin=diagMargins,
)

pieuser = px.pie(df, names='username', hole=0.6)
pieuser.update_layout(
    margin=diagMargins,
)

platring = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-lg fa-photo-video"),
                            html.I(" Platform")
                        ]
                    ),
                    dbc.CardBody(
                        dcc.Graph(
                            figure=pieplat,
                            id="platring",
                            style={'height': 250, 'padding': 0},
                            config={
                                'displayModeBar': False}
                        ),
                        style={'margin-top': '0rem'},
                    )
                ]
            )
            , width={"size": 4}
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-lg fa-users"),
                            html.I(" Operators")
                        ]
                    ),
                    dbc.CardBody(
                        dcc.Graph(
                            figure=pieuser,
                            id="userring",
                            style={'height': 250, 'padding': 0},
                            config={
                                'displayModeBar': False}
                        ),
                        style={'margin-top': '0rem'},
                    )
                ]
            )
            , width={"size": 4}
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-lg fa-chart-bar"),
                            html.I(" Queries by Week Day")
                        ]
                    ),
                    dbc.CardBody(
                        [
                            dcc.Graph(
                                figure=histDay,
                                id="histogramDay",
                                style={'height': 250, 'padding': 0},
                                config={
                                    'displayModeBar': False}
                            )
                        ],
                        style={'margin-top': '0rem'},
                    )
                ]
            )
            , width={"size": 4}
        ),
    ]
)

app.layout = html.Div(
    children=[
        navbar,
        html.Div(
            [title],
            style={'width': '100%', "padding": "10px", "background-color": "#F7F7F7"}
        ),
        html.Div(
            [sp, drop1, sp, bighist, sp, platring, sp, dtable, sp],
            style={'width': '85%', 'margin': 'auto'}
        )
    ]
    , style={'overflow-x': 'hidden'}
)

if __name__ == "__main__":
    app.run_server(debug=True)
