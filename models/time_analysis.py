import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

class TimeAnalysis:
    def __init__(self, series:pd.DataFrame):
        self.series = series
    
    def rolling_mean(self):
        return self.series.rolling(window=10).mean()

    def model(self):
        pass

    def plot_seasonal(self):
        y = self.series.amount
        decomposition = sm.tsa.seasonal_decompose(y, model='additive')
        fig = decomposition.plot()
        plt.show()

    def plot_rolling_mean(self):
        x = self.series.index
        y = self.rolling_mean()
        figure, graph = plt.subplots(figsize=(20, 10), dpi=100)
        graph.plot(
            x, y,
            color='gray'
        )
        plt.show()
