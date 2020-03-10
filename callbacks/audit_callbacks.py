from dash.dependencies import Output, Input, State
import os
import os.path
from functions.count_audits import Audits
from functions.modal_template import Modal
import dash


def register_audit_callbacks(app, data):
    """Set all of the callbacks into a function so they can be imported into relevant pages. This is to prevent clutter
    and keep the page files clean"""

    @app.callback(
        [Output('audit-count', 'children'),
         Output('audit-count', 'className')],
        [Input('btn-generate-audit', 'n_clicks')]
    )
    def update_audit_count_badge(click):
        """Update the count badge on the sidebar"""
        file_count = len([name for name in os.listdir('audits/generated')]) + 1
        return file_count, 'visible ml-2'
