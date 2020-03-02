from dashboard.ringrow import Ringrow
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
ringrow = Ringrow(df)
mainhist = Mainhist(df, spread)
filterrow = Filterrow(users, platforms, ip)
timerow = Timerow(df, start_date, end_date, count)

Dashboard_Page = html.Div(
        [sp, filterrow, sp, timerow, sp,
         mainhist, sp, ringrow, sp, dtable, sp],
        style={'width': '90%', 'margin': 'auto'}
)
