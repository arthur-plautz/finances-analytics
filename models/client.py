from models.bank import Bank
from models.bill import Bill
import json
import os

class Client:
    def __init__(self, credentials_path):
        self.__read_credentials(credentials_path)
        self.__bank = Bank(self.user)

    def __read_credentials(self, credentials_path):
        credentials_file = open(f'{os.getcwd()}/{credentials_path}', 'r')
        credentials = json.load(credentials_file)
        self.__id = credentials.get('id')
        self.__user = credentials.get('user')
        self.__pass = credentials.get('pass')
        self.__cert_path = f"{os.getcwd()}/{credentials.get('cert')}"

    def auth(self):
        self.__bank.auth(self.__user, self.__pass, self.__cert_path)

    def set_credit(self):
        data = self.bank.credit_history()
        self.__credit = Bill(data)

    def set_account(self):
        data = self.bank.account_history()
        self.__account = Bill(data)

    @property
    def user(self):
        return self.__id

    @property
    def credit(self):
        return self.__credit

    @property
    def account(self):
        return self.__account

    @property
    def bank(self):
        return self.__bank
