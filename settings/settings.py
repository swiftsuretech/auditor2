import plotly.io as pio
import dash_html_components as html

pio.templates.default = "simple_white"
sp = html.Br()
diagMargins = dict(t=10, b=10, l=10, r=10)

main_hist_settins = {'height': 250, 'xaxis_title_text': 'Query Date', 'yaxis_title_text': 'Number of Queries',
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
