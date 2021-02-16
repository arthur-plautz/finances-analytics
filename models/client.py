from models.bank import Bank
import os

class Client:
    def __init__(self):
        self.__user = str(os.environ.get('AUTH_USER'))
        self.__pass = str(os.environ.get('AUTH_PASS'))
        self.__cert_path = f"{os.getcwd()}/{os.environ.get('AUTH_PATH')}"
        self.__bank = Bank()

    def auth(self):
        self.__bank.auth(self.__user, self.__pass, self.__cert_path)

    @property
    def bank(self):
        return self.__bank
