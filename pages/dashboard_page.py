"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Defines a Dashboard Class consisting of an html Div with all the dashboard widgets laid out in order.
We divide the dashboard page into rows. There's a row of filters, a wide row with a time / activity
histogram, a row of pie charts and a row of time related widgets. Finally there is a data table.
This defines the static layout with an initial dataset, 'd', which is returned by instantiating a
'DataSet' object. Interactivity is built out in the callbacks.py module.
"""

# Import our functions - generally set out in row modules in the dashboard directory.
from dashboard.ringrow import build_ring_row
from dashboard.filterrow import build_filter_row
from dashboard.timerow import build_time_row
from dashboard.mainhist import build_main_histogram
from dashboard.table import build_data_table
from functions.gossip_data_frame import DataSet
# Also pull in some settings
from settings.settings import space, html


# Instantiate our initial, unfiltered dataset
d = DataSet()

# Fire the dataset at our widget building functions to define them ready to render
data_table = build_data_table(d.df)
ring_row = build_ring_row(d.df)
main_histogram = build_main_histogram(d.df, d.spread)
filter_row = build_filter_row(d.users, d.platforms, d.ip)
time_row = build_time_row(d.df, d.first_date, d.last_date, d.count)


class Dashboard:
    """A dashboard page full of fun and exciting widgets for your wonderment
    Returns a 'Dashboard' object, dropping all the widgets we just built
    into an html Div as the 'page' attribute."""

    def __init__(self):
        self.page = html.Div(
            [space, filter_row, space, time_row, space,
             main_histogram, space, ring_row, space, data_table, space],
            style={'width': '90%', 'margin': 'auto'})
