"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Takes a polygon as an argument and returns an open map server tile using the x, y ,z model
"""

import plotly.graph_objects as go
import re
from settings.settings import map_server
import dash_core_components as dcc
import dash_html_components as html


# TODO multi polygon plotting


class MapBox:
    """Returns a map object"""

    def __init__(self, polygon):
        lat = re.findall('(?:\()([\-0-9.]{2,})', polygon)[:4]
        lon = re.findall('(?:[0-9], |[0-9],)([\-0-9.]{2,})', polygon)[:4]
        order = [0, 1, 3, 2]
        lat = [lat[i] for i in order]
        cent_lat = (float(lat[0]) + float(lat[1])) / 2
        cent_lon = (float(lon[0]) + float(lon[2])) / 2
        fig = go.Figure(go.Scattermapbox(
            fill="toself",
            lon=lon, lat=lat,
            marker={'size': 7, 'color': "red"},
            connectgaps=True
        ))
        fig.update_layout(
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "source": map_server,
                }
            ],
            mapbox={
                'style': "stamen-terrain",
                'center': {'lon': cent_lon, 'lat': cent_lat},
                'zoom': 5},
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            showlegend=False)
        self.map = html.Div(
            dcc.Graph(
                figure=fig
            ),
        )
