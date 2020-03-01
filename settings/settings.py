import plotly.io as pio
import dash
import dash_html_components as html

pio.templates.default = "simple_white"
app = dash.Dash("__name__")
app.title = "Gossip Auditor 2"
diagMargins = dict(t=10, b=10, l=10, r=10)
sp = html.Br()
