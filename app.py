from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from sidebar import Sidebar
from navbar import Navbar
from ringrow import Ringrow
from filterrow import Filterrow
from mainhist import Mainhist
from settings import *
from table import Dtable

df = pd.read_csv("./testData/chatter.csv", parse_dates=['transactionTime'])
df['dayOfWeek'] = df['transactionTime'].dt.day_name()
df['hour'] = df['transactionTime'].dt.hour
users = df.username.unique()
platforms = df.platform.unique()
ip = df.ip.unique()
x = df['transactionTime']
sp = html.Br()
firstDate = df.transactionTime.min()
lastDate = df.transactionTime.max()
spread = (lastDate - firstDate).days // 7
sidebar = Sidebar()
navbar = Navbar()
dtable = Dtable(df)
ringrow = Ringrow(df)
mainhist = Mainhist(df, spread)
filterrow = Filterrow(users, platforms, ip)

app.layout = html.Div(
    children=[
        dbc.Row(
            children=[
                sidebar,
                dbc.Col(
                    children=[
                        navbar,
                        html.Div(
                            [sp, filterrow, sp, mainhist, sp, ringrow, sp, dtable, sp],
                            style={'width': '90%', 'margin': 'auto'}
                        ),
                    ],
                    style={'padding': '0px'}
                ),
            ],
        ),
    ],
    style={'overflow-x': 'hidden'}
)


@app.callback(
    Output(component_id='bighist', component_property='figure'),
    [Input('user-filter', 'value')]
)
def filter_big_histogram(options):
    if not options:
        df_updated = px.histogram(df, x="transactionTime", color="username", nbins=spread)
    else:
        df_updated = px.histogram(df[df['username'] == options], x="transactionTime", color="username", nbins=spread)
    df_updated.update_layout(
        height=350,
        xaxis_title_text='Query Date',
        yaxis_title_text='Number of Queries',
        bargap=0.1,
        barmode='stack',
        margin=diagMargins,
        legend_title="Operator"
    )
    return df_updated


if __name__ == "__main__":
    app.run_server(debug=True)
