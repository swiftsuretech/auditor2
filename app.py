from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
from navbars.sidebar import Sidebar
from navbars.navbar import Navbar
from dashboard.ringrow import Ringrow
from dashboard.filterrow import Filterrow
from dashboard.mainhist import Mainhist
from dashboard.table import Dtable
from settings.settings import *
from builddataframe import DataSet


data = DataSet()
df = data.df
spread = data.spread
users = data.users
platforms = data.platforms
ip = data.ip
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
    [
        Input('operator-filter', 'value'),
        Input('ip-filter', 'value'),
        Input('platform-filter', 'value')
    ]
)
def filter_big_histogram(user_filter, ip_filter, platform_filter):
    if not user_filter:
        user_filter = '.*'
    if not ip_filter:
        ip_filter = '.*'
    if not platform_filter:
        platform_filter = '.*'
    newdf, new_spread = data.filter(user_filter, ip_filter, platform_filter)
    if newdf.empty:
        df_updated = px.histogram(newdf)
    else:
        df_updated = px.histogram(newdf, x='transactionTime', nbins=new_spread, color='username')
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
