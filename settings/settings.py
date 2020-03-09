"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Some Settings that apply / might in the future apply to numerous modules
"""
# TODO Decide whether to implement as a .yaml file or perhaps a settings page in the app.

# Import some Plotly libraries
import plotly.io as pio
import dash_html_components as html

# Define our Map server
# TODO this will need changing to the production Map Server
# map_server = "http://docker:8080/styles/klokantech-basic/{z}/{x}/{y}.png"
map_server = "http://localhost:8080/styles/klokantech-basic/{z}/{x}/{y}.png"
test_data = ["testdata/chatter.csv", "../testdata/chatter.csv"]

# Define a template for visualisations.
pio.templates.default = "simple_white"
space = html.Br()
diagMargins = dict(t=10, b=10, l=10, r=10)
y_axis_title = 'Number of Queries'

pie_style = {'height': 250, 'padding': 0}
pie_config = {'displayModeBar': False}

main_hist_settings = {'height': 250, 'xaxis_title_text': 'Query Date', 'yaxis_title_text': y_axis_title,
                      'bargap': 0.1, 'barmode': 'stack', 'margin': diagMargins,
                      'legend_title': 'Operator'}

hist_day_settings = {'height': 250, 'xaxis_title_text': y_axis_title,
                     'yaxis_title_text': 'Day of Week', 'bargap': 0.3, 'barmode': 'stack',
                     'margin': diagMargins, 'yaxis': dict(categoryorder='array',
                                                          categoryarray=['Sunday', 'Saturday', 'Friday', 'Thursday',
                                                                         'Wednesday',
                                                                         'Tuesday', 'Monday'])}
hist_hour_settings = {'height': 250, 'xaxis_title_text': y_axis_title,
                      'yaxis_title_text': 'Hour of Day', 'bargap': 0.3, 'barmode': 'stack',
                      'margin': diagMargins, 'yaxis_type': 'category',
                      'yaxis': dict(categoryorder='array',
                                    categoryarray=[i for i in range(24, -1, -1)])}

field_mapping = dict({'id': 'Record Number', 'username': 'Operator', 'ip': 'IP Address',
                      'transactionTime': 'Query Time', 'startTime': 'Search From',
                      'endTime': 'Search To', 'authorizationID': 'Flight Plan', 'platform': 'Platform',
                      'usernames': 'User Names', 'day': 'Search Day', 'polygon': 'Search Area',
                      'dayOfWeek': 'Search Day of Week', 'hour': 'Search Hour', 'lat': 'Latitude',
                      'long': 'Longitude', 'city': 'Nearest City', 'cc': 'Country Code',
                      'transactionDate': 'Query Date', 'geo': 'geo'})
