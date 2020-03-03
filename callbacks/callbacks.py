"""
GossipAudtor2
This is the callbacks module. It monitors pre-defined widgets for changes - normally in the form of
filters and carries out the required functions to update defined widgets, normally dashboard type items.

In our case, The main dashboard has a number of widgets and filters. The watch filters are defined in the
callback decorator as 'Inputs'. The inputs and outputs take takes 2 x arguments; the objectID and the value
of that object to set or get.
"""

# Import external libraries
from dash.dependencies import Output, Input
import plotly.express as px
from datetime import datetime as dt
# Import our externalised settings
from settings.settings import main_hist_settins, diagMargins, hist_day_settings, hist_hour_settings


# Set all of the callbacks into a function so they can be imported into relevant pages. This is to prevent clutter
# and keep the page files clean
def register_callbacks(app, data):
    # TODO add some notes
    @app.callback(
        [
            Output('ring_ip', 'figure'),
            Output('dtable', 'data'),
            Output('ring_user', 'figure'),
            Output('ring_plat', 'figure'),
            Output('bighist', 'figure'),
            Output('day_hist', 'figure'),
            Output('hour_hist', 'figure'),
            Output('counter', 'children')
        ],
        [
            Input('operator-filter', 'value'),
            Input('ip-filter', 'value'),
            Input('platform-filter', 'value'),
            Input('date-picker-range', 'start_date'),
            Input('date-picker-range', 'end_date'),
        ]
    )
    # Ths function will take the dashboard in existing state and call a filter method from the 'data' class
    # It will take it's filter parameters from the 'Input' arguments defined above.
    def update_dashboard(user_filter, ip_filter, platform_filter, start_pick, end_pick):
        if not user_filter:
            user_filter = '.*'
        if not ip_filter:
            ip_filter = '.*'
        if not platform_filter:
            platform_filter = '.*'
        start_pick = dt.strptime(start_pick, '%Y-%m-%d').date()
        end_pick = dt.strptime(end_pick, '%Y-%m-%d').date()
        newdf, new_spread, counter = data.filter(user_filter, ip_filter, platform_filter, start_pick, end_pick)

        hist_day = px.histogram(newdf, y=newdf["dayOfWeek"], orientation='h', x=newdf['dayOfWeek'])
        hist_day.update_layout(**hist_day_settings)

        hist_hour = px.histogram(newdf, y=newdf["hour"], orientation='h', x=newdf['hour'])
        hist_hour.update_layout(**hist_hour_settings)

        data_table = newdf.to_dict('records')

        pie_user = px.pie(newdf, names='username', hole=0.6)
        pie_user.update_layout(margin=diagMargins,)

        pie_ip = px.pie(newdf, names='ip', hole=0.6)
        pie_ip.update_layout(margin=diagMargins)

        pie_platform = px.pie(newdf, names='platform', hole=0.6)
        pie_platform.update_layout(margin=diagMargins)

        if newdf.empty:
            df_updated = px.histogram(newdf)
        else:
            df_updated = px.histogram(newdf, x='transactionTime', nbins=new_spread, color='username')

        df_updated.update_layout(**main_hist_settins)

        return pie_ip, data_table, pie_user, pie_platform, df_updated, hist_day, hist_hour, counter