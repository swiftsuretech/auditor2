import pandas as pd


class DataSet:
    """This is the DataSet class. It builds a dataframe and does some other bits. """
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
        from the DataSet class."""
        new_data_frame = self.df[
            (self.df.platform.str.contains(plat_filter)) &
            (self.df.username.str.contains(user_filter)) &
            (self.df.ip.str.contains(ip_filter)) &
            (self.df.transactionTime > pd.Timestamp(start_pick)) &
            (self.df.transactionTime < pd.Timestamp(end_pick))
            ]
        self.last_date = new_data_frame.transactionTime.max()
        self.first_date = new_data_frame.transactionTime.min()
        self.spread = ((self.last_date - self.first_date).days // 7) + 1
        self.count = len(new_data_frame.axes[0])
        return new_data_frame, self.spread, self.count
