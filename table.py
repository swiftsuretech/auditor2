import dash_bootstrap_components as dbc
import dash_table as dt
import dash_html_components as html
import re


def Dtable(df):
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
                            columns=[{"name": i, "id": i} for i in df.columns if
                                     not re.search('^lat.*|^long.*|^polygon|^usernames|^start|^end|^day|^id|^hour', i)],
                            data=df.to_dict('records'),
                            page_action="native",
                            page_size=10,
                            sort_action="native",
                        ),
                        style={'margin-top': '0rem'}
                    )
                ]
            ),
            width={'size': 12},
        )
    )
    return dtable
