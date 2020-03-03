"""
*** Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team ***
Some Settings that apply / might in the future apply to numerous modules
"""
# TODO Decide whether to implement as a .yaml file or perhaps a settings page in the app.

# Import some Plotly libraries
import plotly.io as pio
import dash_html_components as html

# Define a template for visualisations.
pio.templates.default = "simple_white"
space = html.Br()
diagMargins = dict(t=10, b=10, l=10, r=10)

pie_style = {'height': 250, 'padding': 0}
pie_config = {'displayModeBar': False}

main_hist_settings = {'height': 250, 'xaxis_title_text': 'Query Date', 'yaxis_title_text': 'Number of Queries',
                      'bargap': 0.1, 'barmode': 'stack', 'margin': diagMargins,
                      'legend_title': 'Operator'}

hist_day_settings = {'height': 250, 'xaxis_title_text': 'Number of Queries',
                     'yaxis_title_text': 'Day of Week', 'bargap': 0.3, 'barmode': 'stack',
                     'margin': diagMargins, 'yaxis': dict(categoryorder='array',
                                                          categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday',
                                                                         'Wednesday',
                                                                         'Tuesday', 'Monday'])}
hist_hour_settings = {'height': 250, 'xaxis_title_text': 'Number of Queries',
                      'yaxis_title_text': 'Hour of Day', 'bargap': 0.3, 'barmode': 'stack',
                      'margin': diagMargins, 'yaxis_type': 'category',
                      'yaxis': dict(categoryorder='array',
                                    categoryarray=[i for i in range(24, -1, -1)])}
