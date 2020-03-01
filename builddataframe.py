import pandas as pd


class DataSet:
    def __init__(self):
        self.df = pd.read_csv("./testData/chatter.csv", parse_dates=['transactionTime'])
        self.last_date = self.df.transactionTime.max()
        self.first_date = self.df.transactionTime.min()
        self.t_times = self.df['transactionTime']
        self.spread = (self.last_date - self.first_date).days // 7
        self.ip = self.df.ip.unique()
        self.platforms = self.df.platform.unique()
        self.users = self.df.username.unique()
        self.df['dayOfWeek'] = self.df['transactionTime'].dt.day_name()
        self.df['hour'] = self.df['transactionTime'].dt.hour

    def filter(self, user_filter, ip_filter, plat_filter):
        newdf = self.df[
            (self.df.platform.str.contains(plat_filter)) &
            (self.df.username.str.contains(user_filter)) &
            (self.df.ip.str.contains(ip_filter))
            ]
        self.first_date = self.df.transactionTime.min()
        self.t_times = self.df['transactionTime']
        self.spread = (self.last_date - self.first_date).days // 7
        return newdf, self.spread
