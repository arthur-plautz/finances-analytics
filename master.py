from models.client import Client
from models.time_analysis import TimeAnalysis

client = Client()
client.set_credit()

df = client.credit.time_resample('5D')

t = TimeAnalysis(df)
t.plot_seasonal()
