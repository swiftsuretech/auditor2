"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
This is the callbacks module. It monitors pre-defined widgets for changes - normally in the form of
filters and carries out the required functions to update defined widgets, normally dashboard type items.

In our case, The main dashboard has a number of widgets and filters. The watch filters are defined in the
callback decorator as 'Inputs'. The inputs and outputs take takes 2 x arguments; the objectID and the value
of that object to set or get.
"""

# Import external libraries
from dash.dependencies import Output, Input, State
import dash_html_components as html
import plotly.express as px
from datetime import datetime as dt
import dash
import os
from pages.single_record_page import SingleRecordPage
from pages.select_record_page import SelectRecordPage
from pages.dashboard_page import Dashboard
from pages.generate_audit_page import AuditForm
from functions.build_an_audit import Audit
from pages.home import Home
from functions.modal_template import Modal
from pages.conduct_audit_page import AuditPage
from dash.exceptions import PreventUpdate
from functions.count_audits import return_audit_ids, bin_last_audit

# Import some externalised settings
from settings.settings import main_hist_settings, diagMargins, hist_day_settings, hist_hour_settings


def register_functional_callbacks(app, data):
    """Set all of the callbacks into a function so they can be imported into relevant pages. This is to prevent clutter
    and keep the page files clean"""

    @app.callback(
        Output('reset', 'children'),
        [Input('btn-cancel-audit', 'n_clicks'),
         Input('btn-final-cancel', 'n_clicks'),
         Input('btn-audit-finalise', 'n_clicks'),
         Input('btn-audit-cancel', 'n_clicks')]
    )
    def cancel_audit(cancel_at_scope, final_cancel, finalise, cancel_during_audit):
        """Captures button click events for 'audit cancel' - The user cancels mid audit. We will need to write
        to the 'reset' hidden div to divert to the home page. If the user clicks the 'final-cancel' button then
        we will also need to delete the completed audit we have just written. The finalise button actually does
        nothing other than divert away from the page as the audit is already saved by that stage."""
        # Determine which button was pushed and assign it to a variable
        ctx = dash.callback_context
        btn_id = ctx.triggered[0]['prop_id'].split('.')[0]
        return btn_id

    @app.callback(
        Output('modal-open', 'is_open'),
        [Input('close-modal', 'n_clicks')]
    )
    def close_modal(click):
        """Close the modal when user hits the button"""
        if click:
            return False
        return True

    @app.callback(
        Output('audit-progress', 'value'),
        [Input('change-page', 'children')]
    )
    def update_progress_bar(record_number):
        """Update the progress bar whilst conducting an audit"""
        audit_id, count, filename = return_audit_ids()
        try:
            completion = record_number / count * 100
        except ZeroDivisionError:
            completion = 100
        return completion

    @app.callback(
        [Output('change-page', 'children'),
         Output('reset-flag', 'children'),
         Output('alert', 'is_open'),
         Output('alert', 'children'),
         Output('alert', 'color')],
        [Input('btn-audit-reject', 'n_clicks'),
         Input('btn-audit-approve', 'n_clicks')]
    )
    def register_audit_buttons(reject_click, approve_click):
        """Update the hidden div in the sidebar when approve or reject buttons pressed"""
        # Calculate the number of flight plans complete regardless of whether they were approved or rejected
        clicks = (approve_click or 0) + (reject_click or 0)
        cont = True
        # Define a scratch file to build a json string. It will not be valid json until it is complete, hence
        # we will build it separately in a temporary file.
        scratch = 'audits/scratch/scratch.txt'
        ctx = dash.callback_context
        # Determine which button was pushed and assign it to a variable
        btn_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if btn_id == 'btn-audit-reject':
            choice = 'rej'
            alert = 'Flight Plan has been Rejected'
            color = 'danger'
        else:
            choice = 'app'
            alert = 'Flight Plan has been Audited Correct'
            color = 'success'
        audit_id, count, filename = return_audit_ids()
        rec_num = clicks - 1
        flight_plan = audit_id[rec_num]
        # Build the json to append to the tmp file showing the flight plan number as key and auditors decision
        # as the value (either approve or reject).
        json_return = ('\"' + str(flight_plan) + '\": \"' + choice + '\",')
        if clicks >= count:
            # We have completed our audit, set our cont flag to false
            cont = False
        if json_return:
            # Append the json we have just built to a scratch file
            with open(scratch, 'a') as f:
                f.write(json_return)
        if cont:
            # Not at the last record yet so keep iterating through
            return clicks, json_return, True, alert, color
        else:
            # We have captured the full audit. We will grab the json string we wrote to the scratch file, append
            # it to the original scope as a new dictionary field called 'results' and turn it into valid json.
            # Once that's done, delete the scratch file and move our completed audit record to the 'completed'
            # directory where it will be stored as immutable, but viewable through our 'View Complete Audits'
            # page.
            with open(filename, 'r') as f:
                original = f.read()
            with open(scratch, 'r') as g:
                append = g.read()
            amended = '{\"audit\": ' + original + ', \"results\": {' + append + '}}'
            with open(filename, 'w') as f:
                f.write(amended)
            os.remove(scratch)
            new_name = filename.replace('tmp', 'completed')
            os.rename(filename, new_name)
            return clicks, json_return, True, alert, color

    @app.callback(
        [Output('audit-detail', 'children'),
         Output('top-collapse', 'is_open'),
         Output('bottom-collapse', 'is_open'),
         Output('audit-controls', 'hidden'),
         Output('tools-collapse', 'is_open'),
         Output('finalise-audit', 'hidden')],
        [Input('btn-execute-audit', 'n_clicks'),
         Input('audit-date-picker-start', 'date'),
         Input('audit-date-picker-end', 'date'),
         Input('audit-percentage', 'value'),
         Input('change-page', 'children')],
        [State('audit-notes', 'value')]
    )
    def load_audit(click_audit, start, stop, percent, next_page, notes):
        """The user has defined a valid audit, collapse the form cards, build the audit and load the
        auditing page"""
        ctx = dash.callback_context
        btn_id = ctx.triggered[0]['prop_id'].split('.')[0]
        try:
            if btn_id == 'btn-execute-audit':
                Audit(start, stop, percent, notes)
                audit_id, count, filename = return_audit_ids()
                return AuditPage(audit_id[0]).page, False, False, False, True, True
            elif btn_id == 'change-page':
                audit_id, count, filename = return_audit_ids()
                return AuditPage(audit_id[next_page]).page, False, False, False, True, True
        except TypeError:
            # TODO We've finished the audit - do something
            return None, False, False, False, False, False

        else:
            raise PreventUpdate

    @app.callback(
        [Output('audit-scope', 'children'),
         Output('body-bg', 'className'),
         Output('btn-execute-audit', 'disabled'),
         Output('btn-execute-audit', 'className')],
        [Input('audit-date-picker-start', 'date'),
         Input('audit-date-picker-end', 'date'),
         Input('audit-percentage', 'value')],
        [State('audit-notes', 'value')]
    )
    def show_audit_scope(start, end, percent, note):
        """Instantiate an audit object with start date, end date and percentage arguments"""
        audit = Audit(start, end, percent, note)
        msg_success = '{} flight plans were conducted between your selected dates. ' \
                      'With a {}% audit ratio, {} will be subject to audit. '.format(audit.total_count, percent,
                                                                                     audit.audit_count)
        msg_failure = msg_success + ' Try broadening your search dates.'
        if audit.total_count == 0:
            return msg_failure, 'bg-danger text-white', True, 'float-right'
        else:
            return msg_success, None, False, 'bg-success float-right'

    @app.callback(
        Output('show-record-from-table', 'disabled'),
        [Input('dtable', 'selected_row_ids')]
    )
    def disable_button(selected):
        """Disable the 'show record' button if there's no row selected in the table"""
        if selected is None:
            return True
        else:
            return False

    @app.callback(
        Output('placeholder', 'value'),
        [Input('show-record-from-table', 'n_clicks')],
        [State('dtable', 'selected_row_ids')]
    )
    def show_table_record(n_clicks, table_val):
        """Writes the selected Table row from the dashboard to a hidden Div in the Sidebar"""
        return table_val[0]

    @app.callback(
        Output('main_page', 'children'),
        [Input('btn_dashboard', 'n_clicks'),
         #Input('btn_flightplan', 'n_clicks'),
         Input('sidebar_search', 'value'),
         Input('btn_new_audit', 'n_clicks'),
         Input('placeholder', 'value'),
         Input('reset', 'children'),
         Input('btn_home', 'n_clicks')]
    )
    def load_page(dash_click, authid, new_audit_click,
                  table_val, reset, home_click):
        """Returns the relevant page if user clicks a menu button"""
        ctx = dash.callback_context
        btn_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if ctx.triggered[0]['value'] is None:
            # The app is newly loaded. Define the start page
            return Home().page
        if btn_id == 'btn_dashboard':
            return Dashboard().page
        elif btn_id == 'btn_home':
            return Home().page
        # elif btn_id == 'btn_flightplan':
        #     return SelectRecordPage().page
        elif btn_id == 'placeholder':
            return SingleRecordPage(table_val).page
        elif btn_id == 'btn_new_audit':
            return AuditForm().page[0]
        elif btn_id == 'sidebar_search':
            if authid:
                return SingleRecordPage(authid).page
            else:
                return SelectRecordPage().page
        # Another event has been triggered which we have not captured.
        elif btn_id == 'reset' and reset == 'btn-final-cancel':
            bin_last_audit()
            return Home().page
        else:
            return Home().page

    @app.callback(
        # Define our getters and setters
        [
            Output('ring_ip', 'figure'),
            Output('dtable', 'data'),
            Output('ring_user', 'figure'),
            Output('ring_plat', 'figure'),
            Output('big_histogram', 'figure'),
            Output('day_hist', 'figure'),
            Output('hour_hist', 'figure'),
            Output('counter', 'children')
        ],
        [
            Input('operator-filter', 'value'),
            Input('ip-filter', 'value'),
            Input('platform-filter', 'value'),
            Input('date-picker-range', 'start_date'),
            Input('date-picker-range', 'end_date'),
        ]
    )
    def update_dashboard(user_filter, ip_filter, platform_filter, start_pick, end_pick):
        """Ths function will take the dashboard in existing state and call a filter method from the 'data' class
        It will take it's filter parameters from the 'Input' arguments defined above in the order they are
        defined. The function will return the output parameters for the 'Outputs'."""
        # If no filters are applied then we'll send a wildcard filter to pull all records
        if not user_filter:
            user_filter = '.*'
        if not ip_filter:
            ip_filter = '.*'
        if not platform_filter:
            platform_filter = '.*'

        # Start and End times from the date picker are returned as strings. We will need to convert them to date
        # objects to work
        start_pick = dt.strptime(start_pick, '%Y-%m-%d').date()
        end_pick = dt.strptime(end_pick, '%Y-%m-%d').date()

        # Call the 'filter' method of the data object (get_all_records.py). Send our list of filters
        # and return our new dataset and some other variables that include the number of distinct days and
        # record count from our newly filtered data frame.
        new_data_frame, new_spread, counter = data.filter(user_filter, ip_filter, platform_filter, start_pick, end_pick)

        # Re-instantiate our 'days histogram' and apply styling
        hist_day = px.histogram(new_data_frame, y=new_data_frame["dayOfWeek"], orientation='h',
                                x=new_data_frame['dayOfWeek'])
        hist_day.update_layout(**hist_day_settings)

        # Re-instantiate our 'hours histogram' and apply styling
        hist_hour = px.histogram(new_data_frame, y=new_data_frame["hour"], orientation='h', x=new_data_frame['hour'])
        hist_hour.update_layout(**hist_hour_settings)

        # Re-instantiate our 'data table'
        data_table = new_data_frame.to_dict('records')

        # Re-instantiate our 'user pie chart' and apply styling
        pie_user = px.pie(new_data_frame, names='username', hole=0.6)
        pie_user.update_layout(margin=diagMargins, )

        # Re-instantiate our 'IP address pie chart' and apply styling
        pie_ip = px.pie(new_data_frame, names='ip', hole=0.6)
        pie_ip.update_layout(margin=diagMargins)

        # Re-instantiate our 'platform pie chart' and apply styling
        pie_platform = px.pie(new_data_frame, names='platform', hole=0.6)
        pie_platform.update_layout(margin=diagMargins)

        # The main histogram that shows queries by day, bucketed by user is defined here. If we return an
        # empty dataframe, ie, no records, then the spread of days used to calculate the bins is 0, we
        # need to capture this to avoid throwing a / 0 exception
        if new_data_frame.empty:
            df_updated = px.histogram(new_data_frame)
        # Some records are returned, define a bin count and categorise by username
        else:
            df_updated = px.histogram(new_data_frame, x='transactionTime', nbins=new_spread, color='username')
        # Add our styling to the table
        df_updated.update_layout(**main_hist_settings)

        # Now we have defined all of our updated outputs, return them all for rendering
        return pie_ip, data_table, pie_user, pie_platform, df_updated, hist_day, hist_hour, counter
