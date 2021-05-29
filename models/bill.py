import pandas as pd
from pandas import DataFrame
from datetime import datetime

class Bill:
    def __init__(self, data:DataFrame, year=None):
        self.__data = data
        self.__year = year
        self.time_serie = data

    @property
    def categories(self):
        return self.__data.title.unique()

    @property
    def time_serie(self):
        return self.__time_serie

    @time_serie.setter
    def time_serie(self, df):
        df.time = [datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ") for dt in df.time]
        df['t_year'] = [dt.year for dt in df.time]
        df['t_month'] = [dt.month for dt in df.time]
        df['t_day'] = [dt.day for dt in df.time]
        df['t_hour'] = [dt.hour for dt in df.time]
        if self.__year: df = df.query(f"t_year == {self.__year}")
        self.__time_serie = df

    def time_resample_for_amount(self, group_by:str):
        """
        :param group_by: time scale [year, month, day, hour]
        :type str

        Returns the amount spend by time scale.
        """
        raw = self.time_serie.groupby(f"t_{group_by}", as_index=False).sum('amount')
        df = pd.DataFrame()
        df['amount'] = raw['amount']
        df[group_by] = raw[f"t_{group_by}"]
        df.set_index(group_by)
        return df

    def time_resample_for_category(self, group_by:str):
        """
        :param group_by: time scale [year, month, day, hour]
        :type str

        Returns the amount spend by time scale grouped by category.
        """
        raw = self.time_serie
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
    
    def amount_per_category(self):
        df = self.__data.groupby('title').sum()
        return df[['amount']]
    
    