import pandas as pd
from pandas import DataFrame
from datetime import datetime

class Bill:
    def __init__(self, data:DataFrame):
        self.data = data
        self.qualitative_time = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        data.amount = [a/100 for a in data.amount]
        self.__data = data

    @property
    def categories(self):
        return self.__data.title.unique()

    @property
    def qualitative_time(self):
        return self.__qualitative_time

    @qualitative_time.setter
    def qualitative_time(self, df):
        df.time = pd.to_datetime(df.time)
        df['t_year'] = [dt.year for dt in df.time]
        df['t_month'] = [dt.month for dt in df.time]
        df['t_day'] = [dt.day for dt in df.time]
        df['t_hour'] = [dt.hour for dt in df.time]
        self.__qualitative_time = df

    def qtime_resample_for_amount(self, group_by:str):
        """
        :param group_by: time scale [year, month, day, hour]
        :type str

        Returns the amount spend by qualitative time scale.
        """
        raw = self.qualitative_time.groupby(f"t_{group_by}", as_index=False).sum('amount')
        df = pd.DataFrame()
        df['amount'] = raw['amount']
        df[group_by] = raw[f"t_{group_by}"]
        df.set_index(group_by)
        return df

    def qtime_resample_for_category(self, group_by:str):
        """
        :param group_by: time scale [year, month, day, hour]
        :type str

        Returns the amount spend by qualitative time scale grouped by category.
        """
        raw = self.qualitative_time
        columns = self.categories
        df = pd.DataFrame(columns=columns)
        for time in raw[f"t_{group_by}"].unique():
            df_group = raw.query(f"t_{group_by} == {time}").set_index(['title']).groupby('title').sum()
            df_time = {}
            df_time[group_by] = int(time)
            for cat in columns:
                row = df_group.query(f'index == "{cat}"')
                if not row.empty:
                    df_time[cat] = row['amount'][0]
            df = df.append(df_time, ignore_index=True)
        df.set_index(group_by)
        return df
    
    def time_resample(self, period:str):
        """
        :param period: time scale [1D, 3W, 2M, 1Y]
        """
        df = self.__data.set_index('time').resample(period).sum()
        return df[['amount']]

    def amount_per_category(self):
        df = self.__data.groupby('title').sum()
        return df[['amount']]
    
    
