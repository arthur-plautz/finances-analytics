import os
from models.client import Client

users = str(os.getenv('USERS', '')).split(",")
for user in users:
    credentials = f"credentials/{user}.json"

    client = Client(credentials)
    client.auth()

    client.bank.fetch_data('credit')
    client.bank.fetch_data('account')
