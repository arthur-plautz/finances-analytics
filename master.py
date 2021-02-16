from models.client import Client

client = Client()
client.auth()

print(client.bank.credit_history())