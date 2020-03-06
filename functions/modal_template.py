"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Build a simple modal template for providing feedback to the user. We'll build this as a function which
we'll import on the index page so we can call it anywhere in the app.
"""

# Import Libraries
import dash_html_components as html
import dash_bootstrap_components as dbc

info = "fal fa-info mr-2"


class Modal:
    """Build a simple modal to provide user feedback"""

    def __init__(self, header='Header', body='Body'):
        self.modal = dbc.Modal(
            [
                dbc.ModalHeader(
                    children=[
                        html.I(className=info),
                        html.I(header)
                    ]
                ),
                dbc.ModalBody(body),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-modal", className="ml-auto"
                    )
                ),
            ],
            id="modal-open",
            centered=True,
            is_open=True
        )
