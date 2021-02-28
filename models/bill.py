import pandas as pd
from pandas import DataFrame
from datetime import datetime

class Bill:
    def __init__(self, data:DataFrame):
        self.__data = data
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
        self.__time_serie = df

    def time_resample_for_amount(self, groub_by:str):
        """
        :param group_by: time scale [year, month, day, hour]
        :type str
        """
        raw = self.time_serie.groupby(f"t_{groub_by}", as_index=False).sum('amount')
        df = pd.DataFrame()
        df['amount'] = raw['amount']
        df[groub_by] = raw[f"t_{groub_by}"]
        return df

    def time_resample_for_category(self, group_by:str):
        raw = self.time_serie
        columns = ["time"] + raw.title.unique()
        df = pd.DataFrame(columns=columns)
        for time in raw[f"t_{group_by}"].unique():
            print(raw.query(f"t_{group_by} == {time}").set_index(['title']).groupby('title').sum())
