from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from navbars.sidebar import Sidebar
from navbars.navbar import Navbar
from dashboard.ringrow import Ringrow
from dashboard.filterrow import Filterrow
from dashboard.mainhist import Mainhist
from dashboard.table import Dtable
from settings.settings import *
from gossip_data_frame import DataSet

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
    [
        Output('ring_day', 'figure'),
        Output('dtable', 'data'),
        Output('ring_user', 'figure'),
        Output('ring_plat', 'figure'),
        Output('bighist', 'figure'),
    ],
    [
        Input('operator-filter', 'value'),
        Input('ip-filter', 'value'),
        Input('platform-filter', 'value'),
    ]
)
def update_dashboard(user_filter, ip_filter, platform_filter):
    if not user_filter:
        user_filter = '.*'
    if not ip_filter:
        ip_filter = '.*'
    if not platform_filter:
        platform_filter = '.*'
    newdf, new_spread = data.filter(user_filter, ip_filter, platform_filter)

    hist_day = px.histogram(newdf, y=newdf["dayOfWeek"], orientation='h', x=newdf['dayOfWeek'])
    hist_day.update_layout(
        height=250,
        xaxis_title_text='Number of Queries',
        yaxis_title_text='Day of Week',
        bargap=0.3,
        barmode='stack',
        margin=diagMargins,
        yaxis=dict(categoryorder='array',
                   categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday',
                                  'Tuesday', 'Monday'])
    )

    data_table = newdf.to_dict('records')

    pieuser = px.pie(newdf, names='username', hole=0.6)
    pieuser.update_layout(
        margin=diagMargins,
    )

    pieplat = px.pie(newdf, names='platform', hole=0.6)
    pieplat.update_layout(
        margin=diagMargins,
    )

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

    return hist_day, data_table, pieuser, pieplat, df_updated


if __name__ == "__main__":
    app.run_server(debug=True)
