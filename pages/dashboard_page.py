from dashboard.ringrow import build_ring_row
from dashboard.filterrow import Filterrow
from dashboard.timerow import Timerow
from dashboard.mainhist import Mainhist
from dashboard.table import Dtable
from functions.gossip_data_frame import DataSet
from settings.settings import *

data = DataSet()
start_date = data.first_date
end_date = data.last_date
df = data.df
spread = data.spread
users = data.users
platforms = data.platforms
ip = data.ip
count = data.count

dtable = Dtable(df)
ring_row = build_ring_row(df)
main_histogram = Mainhist(df, spread)
filter_row = Filterrow(users, platforms, ip)
time_row = Timerow(df, start_date, end_date, count)

Dashboard_Page = html.Div(
    [sp, filter_row, sp, time_row, sp,
     main_histogram, sp, ring_row, sp, dtable, sp],
    style={'width': '90%', 'margin': 'auto'}
)
