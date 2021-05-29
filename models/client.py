from models.bank import Bank
from models.bill import Bill
import os

class Client:
    def __init__(self):
        self.__user = str(os.environ.get('AUTH_USER'))
        self.__pass = str(os.environ.get('AUTH_PASS'))
        self.__cert_path = f"{os.getcwd()}/{os.environ.get('AUTH_PATH')}"
        self.__bank = Bank()
        self.__year = None
        self.__credit = None
        self.__account = None

    def auth(self):
        self.__bank.auth(self.__user, self.__pass, self.__cert_path)

    def set_credit(self):
        data = self.bank.credit_history()
        self.__credit = Bill(data, self.__year)

    def set_account(self):
        data = self.bank.account_history()
        self.__account = Bill(data, self.__year)
    
    def set_year(self, year):
        self.__year = year
        if self.__credit:
            self.set_credit()
        if self.__account:
            self.set_account()

    @property
    def credit(self):
        return self.__credit

    @property
    def account(self):
        return self.__account

    @property
    def bank(self):
        return self.__bank
    
    @property
    def year(self):
        return self.__year
