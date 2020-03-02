from dash.dependencies import Output, Input, State
import plotly.express as px
from settings.settings import diagMargins
from datetime import datetime as dt


def register_callbacks(app, data):
    @app.callback(
        [
            Output('ring_ip', 'figure'),
            Output('dtable', 'data'),
            Output('ring_user', 'figure'),
            Output('ring_plat', 'figure'),
            Output('bighist', 'figure'),
            Output('day_hist', 'figure'),
            Output('hour_hist', 'figure'),
        ],
        [
            Input('operator-filter', 'value'),
            Input('ip-filter', 'value'),
            Input('platform-filter', 'value'),
            Input('date-picker-range', 'start_date'),
            Input('date-picker-range', 'end_date'),
        ]
    )
    def update_dashboard(user_filter, ip_filter, platform_filter, start_pick, end_pick):
        if not user_filter:
            user_filter = '.*'
        if not ip_filter:
            ip_filter = '.*'
        if not platform_filter:
            platform_filter = '.*'
        start_pick = dt.strptime(start_pick, '%Y-%m-%d').date()
        end_pick = dt.strptime(end_pick, '%Y-%m-%d').date()
        newdf, new_spread = data.filter(user_filter, ip_filter, platform_filter, start_pick, end_pick)

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

        hist_hour = px.histogram(newdf, y=newdf["hour"], orientation='h', x=newdf['hour'],
                                 )

        hist_hour.update_layout(
            height=250,
            xaxis_title_text='Number of Queries',
            yaxis_title_text='Hour of Day',
            bargap=0.3,
            barmode='stack',
            margin=diagMargins,
            yaxis_type='category',
            yaxis=dict(categoryorder='array',
                       categoryarray=[24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,
                                      12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        ),

        data_table = newdf.to_dict('records')

        pieuser = px.pie(newdf, names='username', hole=0.6)
        pieuser.update_layout(
            margin=diagMargins,
        )

        pieip = px.pie(newdf, names='ip', hole=0.6)
        pieip.update_layout(
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
            height=250,
            xaxis_title_text='Query Date',
            yaxis_title_text='Number of Queries',
            bargap=0.1,
            barmode='stack',
            margin=diagMargins,
            legend_title="Operator"
        )

        return pieip, data_table, pieuser, pieplat, df_updated, hist_day, hist_hour

    # @app.callback(
    #     Output("hist_collapse", "is_open"),
    #     [Input("hist_collapse-button", "n_clicks")],
    #     [State("hist_collapse", "is_open")],
    # )
    # def toggle_collapse(n, is_open):
    #     if not n:
    #         return not is_open
    #     return not is_open
