from models.client import Client

client = Client()
client.auth()

client.bank.fetch_data('credit')
client.bank.fetch_data('account')