"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
These functions count the number of audits in the 'audit folder. These can be classified as either
'generated' or 'complete'.
"""

import os
import os.path


class Audits:
    def __init__(self):
        self.completed = count_completed_audits()
        self.generated = count_generated_audits()


def count_generated_audits():
    try:
        return len([name for name in os.listdir('audits/generated')])
    except FileNotFoundError:
        return len([name for name in os.listdir('../audits/generated')])


def count_completed_audits():
    try:
        return len([name for name in os.listdir('audits/completed')])
    except FileNotFoundError:
        return len([name for name in os.listdir('../audits/completed')])
