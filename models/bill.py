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
