from dashboard.ringrow import Ringrow
from dashboard.filterrow import Filterrow
from dashboard.mainhist import Mainhist
from dashboard.table import Dtable
from functions.gossip_data_frame import DataSet
from settings.settings import *

data = DataSet()
df = data.df
spread = data.spread
users = data.users
platforms = data.platforms
ip = data.ip

dtable = Dtable(df)
ringrow = Ringrow(df)
mainhist = Mainhist(df, spread)
filterrow = Filterrow(users, platforms, ip)

Dashboard_Page = html.Div(
    html.Div(
        [sp, filterrow, sp,
         mainhist, sp, ringrow, sp, dtable, sp],
        style={'width': '90%', 'margin': 'auto'}
    ),
)
