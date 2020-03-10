"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Build an audit Class. Takes a date range and percentage as arguments and returns that percentage of available
records for audit, nominating them by their index.
"""

# Import libraries
import pandas as pd
from settings.settings import test_data
from datetime import datetime as dt
import json


class Audit:
    """Build an audit Class"""

    def __init__(self, start, end, percentage, note):
        # Load up all our records into a dataframe.
        try:
            df = pd.read_csv(test_data[0], dayfirst=True,
                             parse_dates=['transactionTime', 'startTime', 'endTime'])
        except FileNotFoundError:
            df = pd.read_csv(test_data[1], dayfirst=True,
                             parse_dates=['transactionTime', 'startTime', 'endTime'])
        # Filter it down with our given dates
        filtered_data_frame = df[
            (df.transactionTime > pd.Timestamp(start)) &
            (df.transactionTime < pd.Timestamp(end))]
        # Count the total records
        self.total_count = len(filtered_data_frame.axes[0])
        # Apply our percentage
        self.audit_count = round(self.total_count * (percentage / 100))
        # Sample the data (take a random sample according to 'audit_count' variable
        self.start = start
        self.end = end
        self.note = note
        self.df = filtered_data_frame.sample(n=self.audit_count)
        if self.audit_count < 1:
            self.status = 'Your search has yielded no results. Either increase the date range or percentage'
        else:
            self.status = ['The audit has now been built. There were {} flight plans found between selected dates \
            . {} of them have been selected for audit.'.format(self.total_count, self.audit_count)]
            selection = self.df.id.tolist()
            selection = dict(zip(selection, ['gen' for i in selection]))
            timestamp = dt.now().timestamp()
            self.filename = 'audits/generated/G_AUDIT|{}|{}|{}|{}.json'.format(timestamp, self.start, self.end,
                                                                            percentage)
            self.audit_file = json.dumps({"filename": self.filename, "status": "gen", "timestamp": timestamp,
                                          "note": self.note,
                                          "start": self.start, "end": self.end, "percentage": percentage,
                                          "selection": selection})
            f = open(self.filename, 'w+')
            f.write(self.audit_file)
            f.close()