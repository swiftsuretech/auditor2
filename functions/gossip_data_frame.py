"""
Define the DataSet class and filter method. We init a dataset consisting of the whole dataset,
currently from our test data directory in .csv format. We use pandas to build a dataframe
which will make our lives easier for mungeinig operations
"""

# Import Pandas
import pandas as pd

# TODO - Need to implement data ingestion from Elastic for production
# TODO - Consider how much data we can work with
#  in memory. We can consider either paging data or restricting user to only 3 months worth


class DataSet:
    """This is the DataSet class. It builds a dataframe and does some other bits.
    It returns a dataframe as df as well as some other useful variables. These
    include lists of unique IP addresses, users etc so we can build out our filters
    as well as the spread of days to calculate how we should lay out our histograms
    in neat buckets. We also send back a record count to display on a card for
    additional eye candy"""
    def __init__(self):
        self.df = pd.read_csv("testdata/chatter.csv", parse_dates=['transactionTime'])
        self.last_date = self.df.transactionTime.max().date()
        self.first_date = self.df.transactionTime.min().date()
        self.t_times = self.df['transactionTime']
        self.spread = ((self.last_date - self.first_date).days // 7) + 1
        self.ip = self.df.ip.unique()
        self.platforms = self.df.platform.unique()
        self.users = self.df.username.unique()
        self.df['dayOfWeek'] = self.df['transactionTime'].dt.day_name()
        self.df['hour'] = self.df['transactionTime'].dt.hour
        self.count = len(self.df.axes[0])

    def filter(self, user_filter, ip_filter, plat_filter, start_pick, end_pick):
        """Takes a bunch of filters and applies them to the current data object, instantiated
        from the DataSet class. They will generally come from the callback functions which
        will send a number of filters to apply to the existing dataframe and build out a
        new one. We also return the record count and the spread of days as described above"""
        filtered_data_frame = self.df[
            (self.df.platform.str.contains(plat_filter)) &
            (self.df.username.str.contains(user_filter)) &
            (self.df.ip.str.contains(ip_filter)) &
            (self.df.transactionTime > pd.Timestamp(start_pick)) &
            (self.df.transactionTime < pd.Timestamp(end_pick))
            ]
        self.last_date = filtered_data_frame.transactionTime.max()
        self.first_date = filtered_data_frame.transactionTime.min()
        self.spread = ((self.last_date - self.first_date).days // 7) + 1
        self.count = len(filtered_data_frame.axes[0])
        return filtered_data_frame, self.spread, self.count
