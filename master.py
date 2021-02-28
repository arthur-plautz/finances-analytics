from models.client import Client

client = Client()

client.set_credit()
client.credit.time_resample_for_category('hour')