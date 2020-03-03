"""
*** Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team ***
Build out our Data table for the Dashboard. Returns Bootstrap row with the table rendered across the whole
Dashboard page in a card style.
"""

# Import our dash libraries and regex
import dash_bootstrap_components as dbc
import dash_table as dt
import dash_html_components as html
import re


def build_data_table(df):
    """Builds out a formatted data table in a Bootstrap layout from the single 'df' argument. The function
    is mainly a styling exercise."""
    dtable = dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        [
                            html.I(className="fal fa-lg fa-table"),
                            html.I(" Queries Table")
                        ]
                    ),
                    dbc.CardBody(
                        dt.DataTable(
                            style_data={
                            },
                            style_cell={
                                'textAlign': 'left',
                            },
                            style_table={
                                'maxHeight': '600px',
                            },
                            # Define some custom table widths for our table
                            style_cell_conditional=[
                                {'if': {'column_id': 'id'},
                                 'width': '10%'},
                                {'if': {'column_id': 'username'},
                                 'width': '15%'},
                                {'if': {'column_id': 'platform'},
                                 'width': '25%'},
                                {'if': {'column_id': 'authorizationID'},
                                 'width': '25%'},
                            ],
                            id="dtable",
                            # This list comprehension statement will load up the columns we want to render in our
                            # table. We'll load up by exception, excluding those we don't want to see with a
                            # regex 'OR' statement.
                            columns=[{"name": i, "id": i} for i in df.columns if
                                     not re.search('^lat.*|^long.*|^polygon|^usernames|^start|^end|^day|^id|^hour', i)],
                            data=df.to_dict('records'),
                            # Sorting and single row selection are enabled. Paging is set to 10 records.
                            page_action="native",
                            page_size=10,
                            sort_action="native",
                            row_selectable='single',
                        ),
                        style={'margin-top': '0rem'}
                    )
                ]
            ),
            width={'size': 12},
        )
    )
    return dtable
