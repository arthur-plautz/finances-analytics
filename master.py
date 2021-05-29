from models.client import Client

client = Client()
client.set_credit()

client.set_year('2020')
df_2020 = client.credit.time_resample_for_category('month')

client.set_year('2021')
df_2021 = client.credit.time_resample_for_category('month')
