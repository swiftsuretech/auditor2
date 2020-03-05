"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
This is the callbacks module. It monitors pre-defined widgets for changes - normally in the form of
filters and carries out the required functions to update defined widgets, normally dashboard type items.

In our case, The main dashboard has a number of widgets and filters. The watch filters are defined in the
callback decorator as 'Inputs'. The inputs and outputs take takes 2 x arguments; the objectID and the value
of that object to set or get.
"""
# TODO - Do we need any error trapping in this module?

# Import external libraries
from dash.dependencies import Output, Input
import plotly.express as px
from datetime import datetime as dt

# Import some externalised settings
from settings.settings import main_hist_settings, diagMargins, hist_day_settings, hist_hour_settings


def register_callbacks(app, data):
    """Set all of the callbacks into a function so they can be imported into relevant pages. This is to prevent clutter
    and keep the page files clean"""
    @app.callback(
        # Define our getters and setters
        [
            Output('ring_ip', 'figure'),
            Output('dtable', 'data'),
            Output('ring_user', 'figure'),
            Output('ring_plat', 'figure'),
            Output('big_histogram', 'figure'),
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
    def update_dashboard(user_filter, ip_filter, platform_filter, start_pick, end_pick):
        """Ths function will take the dashboard in existing state and call a filter method from the 'data' class
        It will take it's filter parameters from the 'Input' arguments defined above in the order they are
        defined. The function will return the output parameters for the 'Outputs'."""
        # If no filters are applied then we'll send a wildcard filter to pull all records
        if not user_filter:
            user_filter = '.*'
        if not ip_filter:
            ip_filter = '.*'
        if not platform_filter:
            platform_filter = '.*'

        # Start and End times from the date picker are returned as strings. We will need to convert them to date
        # objects to work
        start_pick = dt.strptime(start_pick, '%Y-%m-%d').date()
        end_pick = dt.strptime(end_pick, '%Y-%m-%d').date()

        # Call the 'filter' method of the data object (get_all_records.py). Send our list of filters
        # and return our new dataset and some other variables that include the number of distinct days and
        # record count from our newly filtered data frame.
        new_data_frame, new_spread, counter = data.filter(user_filter, ip_filter, platform_filter, start_pick, end_pick)

        # Re-instantiate our 'days histogram' and apply styling
        hist_day = px.histogram(new_data_frame, y=new_data_frame["dayOfWeek"], orientation='h',
                                x=new_data_frame['dayOfWeek'])
        hist_day.update_layout(**hist_day_settings)

        # Re-instantiate our 'hours histogram' and apply styling
        hist_hour = px.histogram(new_data_frame, y=new_data_frame["hour"], orientation='h', x=new_data_frame['hour'])
        hist_hour.update_layout(**hist_hour_settings)

        # Re-instantiate our 'data table'
        data_table = new_data_frame.to_dict('records')

        # Re-instantiate our 'user pie chart' and apply styling
        pie_user = px.pie(new_data_frame, names='username', hole=0.6)
        pie_user.update_layout(margin=diagMargins, )

        # Re-instantiate our 'IP address pie chart' and apply styling
        pie_ip = px.pie(new_data_frame, names='ip', hole=0.6)
        pie_ip.update_layout(margin=diagMargins)

        # Re-instantiate our 'platform pie chart' and apply styling
        pie_platform = px.pie(new_data_frame, names='platform', hole=0.6)
        pie_platform.update_layout(margin=diagMargins)

        # The main histogram that shows queries by day, bucketed by user is defined here. If we return an
        # empty dataframe, ie, no records, then the spread of days used to calculate the bins is 0, we
        # need to capture this to avoid throwing a / 0 exception
        if new_data_frame.empty:
            df_updated = px.histogram(new_data_frame)
        # Some records are returned, define a bin count and categorise by username
        else:
            df_updated = px.histogram(new_data_frame, x='transactionTime', nbins=new_spread, color='username')
        # Add our styling to the table
        df_updated.update_layout(**main_hist_settings)

        # Now we have defined all of our updated outputs, return them all for rendering
        return pie_ip, data_table, pie_user, pie_platform, df_updated, hist_day, hist_hour, counter
